import json
from pathlib import Path

from hva_collector.anonymize import Anonymizer, rating_band


def test_ids_are_stable_and_distinct(tmp_path: Path) -> None:
    first = Anonymizer(tmp_path)
    alice = first.author_id("alice")
    bob = first.author_id("bob")
    assert alice.startswith("author-")
    assert alice != bob
    second = Anonymizer(tmp_path)
    assert second.author_id("alice") == alice


def test_mapping_stays_in_the_private_directory(tmp_path: Path) -> None:
    anonymizer = Anonymizer(tmp_path)
    anonymizer.author_id("alice")
    mapping = json.loads((tmp_path / "mapping.json").read_text())
    assert "alice" in mapping
    assert (tmp_path / "anonymize.key").exists()


def test_rating_bands() -> None:
    assert rating_band(None) is None
    assert rating_band(1320) == "1200-1499"
    assert rating_band(2150) == "2100-2399"
    assert rating_band(800) == "600-899"
