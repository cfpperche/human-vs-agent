"""Fetch of problem and submission pages, with an on-disk cache.

Page access stays at low volume. The cache prevents repeat fetches.
See docs/data-licensing-review.md.
"""

import hashlib
from pathlib import Path

import httpx

from hva_collector.api import USER_AGENT


class ChallengeError(RuntimeError):
    """The page returned the Codeforces browser challenge, not content."""


_CHALLENGE_MARKERS = (
    "Your browser is being checked",
    "__CF$cv$params",
    "challenge-platform",
)


def _is_challenge(html: str) -> bool:
    head = html[:4000]
    return any(marker in head for marker in _CHALLENGE_MARKERS)


class PageFetcher:
    def __init__(self, cache_dir: Path, client: httpx.Client | None = None) -> None:
        self._cache_dir = cache_dir
        self._client = client or httpx.Client(
            timeout=30, follow_redirects=True, headers={"User-Agent": USER_AGENT}
        )

    def fetch(self, url: str) -> str:
        key = hashlib.sha256(url.encode()).hexdigest()
        path = self._cache_dir / f"{key}.html"
        if path.exists():
            cached = path.read_text()
            if not _is_challenge(cached):
                return cached
        response = self._client.get(url)
        response.raise_for_status()
        if _is_challenge(response.text):
            raise ChallengeError(f"browser challenge returned for {url}")
        self._cache_dir.mkdir(parents=True, exist_ok=True)
        path.write_text(response.text)
        return response.text


def problem_url(contest_id: int, index: str) -> str:
    return f"https://codeforces.com/contest/{contest_id}/problem/{index}"


def submission_url(contest_id: int, submission_id: int) -> str:
    return f"https://codeforces.com/contest/{contest_id}/submission/{submission_id}"
