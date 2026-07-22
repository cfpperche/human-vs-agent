"""Extraction of the statement and the sample tests from problem HTML."""

from dataclasses import dataclass

from bs4 import BeautifulSoup, Tag


@dataclass
class ParsedStatement:
    text: str
    samples: list[tuple[str, str]]


def _pre_text(pre: Tag) -> str:
    text = pre.get_text("\n").strip()
    return text + "\n" if text else ""


def parse_problem_page(html: str) -> ParsedStatement:
    soup = BeautifulSoup(html, "html.parser")
    root = soup.find("div", class_="problem-statement")
    if not isinstance(root, Tag):
        raise ValueError("problem statement block not found")

    inputs: list[str] = []
    outputs: list[str] = []
    sample_block = root.find("div", class_="sample-test")
    if isinstance(sample_block, Tag):
        for div in sample_block.find_all("div", class_="input"):
            pre = div.find("pre")
            if isinstance(pre, Tag):
                inputs.append(_pre_text(pre))
        for div in sample_block.find_all("div", class_="output"):
            pre = div.find("pre")
            if isinstance(pre, Tag):
                outputs.append(_pre_text(pre))
    if len(inputs) != len(outputs):
        raise ValueError("sample inputs and outputs do not pair")

    text = " ".join(root.get_text(" ").split())
    return ParsedStatement(text=text, samples=list(zip(inputs, outputs, strict=True)))


def parse_submission_source(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    pre = soup.find(id="program-source-text")
    if not isinstance(pre, Tag):
        raise ValueError("submission source block not found")
    source = pre.get_text()
    return source if source.endswith("\n") else source + "\n"
