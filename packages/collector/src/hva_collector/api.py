"""Typed client for the official Codeforces API.

The client stays far under the documented platform limit of 5
requests in 1 second. See docs/data-licensing-review.md.
"""

import time
from collections.abc import Callable
from typing import Any

import httpx
from pydantic import BaseModel, Field

BASE_URL = "https://codeforces.com/api"
USER_AGENT = "hva-collector/0.1 (research; https://github.com/cfpperche/human-vs-agent)"


class ApiError(RuntimeError):
    pass


class ApiContest(BaseModel):
    id: int
    name: str
    phase: str
    startTimeSeconds: int | None = None


class ApiProblem(BaseModel):
    contestId: int | None = None
    index: str
    name: str
    rating: int | None = None
    tags: list[str] = Field(default_factory=list[str])


class ApiMember(BaseModel):
    handle: str


class ApiParty(BaseModel):
    members: list[ApiMember] = Field(default_factory=list[ApiMember])


class ApiSubmission(BaseModel):
    id: int
    contestId: int | None = None
    creationTimeSeconds: int
    problem: ApiProblem
    author: ApiParty
    programmingLanguage: str
    verdict: str | None = None
    timeConsumedMillis: int
    memoryConsumedBytes: int


class ApiUser(BaseModel):
    handle: str
    rating: int | None = None


class CodeforcesApi:
    def __init__(
        self,
        client: httpx.Client | None = None,
        min_interval_seconds: float = 1.0,
        sleep: Callable[[float], None] = time.sleep,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        self._client = client or httpx.Client(timeout=30, headers={"User-Agent": USER_AGENT})
        self._min_interval = min_interval_seconds
        self._sleep = sleep
        self._clock = clock
        self._last_request = float("-inf")

    def _get(self, method: str, params: dict[str, str]) -> Any:
        wait = self._min_interval - (self._clock() - self._last_request)
        if wait > 0:
            self._sleep(wait)
        last_error = "request failed"
        for attempt in range(3):
            self._last_request = self._clock()
            response = self._client.get(f"{BASE_URL}/{method}", params=params)
            if response.status_code in (429, 503):
                last_error = f"http {response.status_code}"
                self._sleep(2.0 * (attempt + 1))
                continue
            response.raise_for_status()
            payload = response.json()
            if payload.get("status") != "OK":
                comment = str(payload.get("comment", ""))
                if "limit" in comment.lower():
                    last_error = comment
                    self._sleep(2.0 * (attempt + 1))
                    continue
                raise ApiError(comment or "request failed")
            return payload["result"]
        raise ApiError(f"gave up after retries on {method}: {last_error}")

    def contest_list(self) -> list[ApiContest]:
        result = self._get("contest.list", {"gym": "false"})
        return [ApiContest.model_validate(item) for item in result]

    def problemset_problems(self) -> list[ApiProblem]:
        result = self._get("problemset.problems", {})
        return [ApiProblem.model_validate(item) for item in result["problems"]]

    def contest_status(self, contest_id: int, count: int = 200) -> list[ApiSubmission]:
        params = {"contestId": str(contest_id), "from": "1", "count": str(count)}
        result = self._get("contest.status", params)
        return [ApiSubmission.model_validate(item) for item in result]

    def user_info(self, handles: list[str]) -> list[ApiUser]:
        result = self._get("user.info", {"handles": ";".join(handles)})
        return [ApiUser.model_validate(item) for item in result]
