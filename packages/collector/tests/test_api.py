import json
from pathlib import Path
from typing import Any

import httpx
import pytest

from hva_collector.api import ApiError, CodeforcesApi

FIXTURES = Path(__file__).parent / "fixtures"


def _fixture(name: str) -> Any:
    return json.loads((FIXTURES / name).read_text())


class FakeTime:
    def __init__(self) -> None:
        self.now = 0.0
        self.sleeps: list[float] = []

    def clock(self) -> float:
        return self.now

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


def _api_transport() -> httpx.MockTransport:
    files = {
        "contest.list": "contest_list.json",
        "problemset.problems": "problemset_problems.json",
        "contest.status": "contest_status.json",
        "user.info": "user_info.json",
    }

    def handler(request: httpx.Request) -> httpx.Response:
        method = request.url.path.rsplit("/", 1)[-1]
        return httpx.Response(200, json={"status": "OK", "result": _fixture(files[method])})

    return httpx.MockTransport(handler)


def _api(fake: FakeTime) -> CodeforcesApi:
    client = httpx.Client(transport=_api_transport())
    return CodeforcesApi(client=client, sleep=fake.sleep, clock=fake.clock)


def test_parses_fixture_responses() -> None:
    api = _api(FakeTime())
    contests = api.contest_list()
    assert [c.id for c in contests] == [2100, 1500, 2101]
    problems = api.problemset_problems()
    assert problems[0].rating == 800
    submissions = api.contest_status(2100)
    assert submissions[0].author.members[0].handle == "alice"
    users = api.user_info(["alice", "bob"])
    assert {u.handle: u.rating for u in users} == {"alice": 2150, "bob": 1320}


def test_rate_limiter_spaces_requests() -> None:
    fake = FakeTime()
    api = _api(fake)
    api.contest_list()
    assert fake.sleeps == []
    api.contest_list()
    assert fake.sleeps == [1.0]


def test_retries_on_call_limit_then_succeeds() -> None:
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] == 1:
            payload = {"status": "FAILED", "comment": "Call limit exceeded"}
            return httpx.Response(200, json=payload)
        return httpx.Response(200, json={"status": "OK", "result": _fixture("contest_list.json")})

    fake = FakeTime()
    client = httpx.Client(transport=httpx.MockTransport(handler))
    api = CodeforcesApi(client=client, sleep=fake.sleep, clock=fake.clock)
    contests = api.contest_list()
    assert len(contests) == 3
    assert 2.0 in fake.sleeps


def test_raises_on_api_failure() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"status": "FAILED", "comment": "handles: field missing"})

    client = httpx.Client(transport=httpx.MockTransport(handler))
    api = CodeforcesApi(client=client, sleep=lambda s: None, clock=lambda: 0.0)
    with pytest.raises(ApiError, match="field missing"):
        api.user_info(["nobody"])
