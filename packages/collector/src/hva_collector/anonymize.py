"""Pseudonymous author identifiers.

The platform handle never enters the collected data. The keyed hash
and the mapping stay in a private directory outside git. See
docs/data-licensing-review.md.
"""

import hashlib
import hmac
import json
import secrets
from pathlib import Path


class Anonymizer:
    def __init__(self, private_dir: Path) -> None:
        private_dir.mkdir(parents=True, exist_ok=True)
        self._key_path = private_dir / "anonymize.key"
        self._map_path = private_dir / "mapping.json"
        if not self._key_path.exists():
            self._key_path.write_text(secrets.token_hex(32))
        self._key = bytes.fromhex(self._key_path.read_text().strip())
        self._mapping: dict[str, str] = {}
        if self._map_path.exists():
            self._mapping = json.loads(self._map_path.read_text())

    def author_id(self, handle: str) -> str:
        digest = hmac.new(self._key, handle.encode(), hashlib.sha256).hexdigest()
        author_id = f"author-{digest[:12]}"
        if self._mapping.get(handle) != author_id:
            self._mapping[handle] = author_id
            self._map_path.write_text(json.dumps(self._mapping, indent=2, sort_keys=True) + "\n")
        return author_id


def rating_band(rating: int | None) -> str | None:
    if rating is None:
        return None
    low = (rating // 300) * 300
    return f"{low}-{low + 299}"
