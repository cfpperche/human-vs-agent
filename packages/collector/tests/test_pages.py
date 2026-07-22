from pathlib import Path

import httpx
import pytest

from hva_collector.pages import ChallengeError, PageFetcher

FIXTURES = Path(__file__).parent / "fixtures"
CHALLENGE_HTML = (
    "<style>p{}</style><p>Please wait. Your browser is being checked. "
    "It may take a few seconds...</p><script>window.__CF$cv$params={};</script>"
)


def _fetcher(html: str, cache_dir: Path) -> tuple[PageFetcher, list[str]]:
    calls: list[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(str(request.url))
        return httpx.Response(200, text=html)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    return PageFetcher(cache_dir=cache_dir, client=client), calls


def test_fetch_caches_normal_pages(tmp_path: Path) -> None:
    html = (FIXTURES / "problem_page.html").read_text()
    fetcher, calls = _fetcher(html, tmp_path)
    first = fetcher.fetch("https://codeforces.com/contest/1/problem/A")
    second = fetcher.fetch("https://codeforces.com/contest/1/problem/A")
    assert first == second == html
    assert len(calls) == 1


def test_fetch_raises_on_challenge_and_does_not_cache(tmp_path: Path) -> None:
    fetcher, calls = _fetcher(CHALLENGE_HTML, tmp_path)
    with pytest.raises(ChallengeError):
        fetcher.fetch("https://codeforces.com/contest/1/submission/1")
    assert list(tmp_path.glob("*.html")) == []
    with pytest.raises(ChallengeError):
        fetcher.fetch("https://codeforces.com/contest/1/submission/1")
    assert len(calls) == 2
