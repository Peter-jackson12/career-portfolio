"""Public data and human-edited My Role must agree before generation."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest
from check_portfolio import check, render_index

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def copied(tmp_path):
    for name in [
        "README.md",
        "AGENTS.md",
        "contracts.lock.json",
        "data",
        "schemas",
        "scripts",
        "generated",
        "projects",
        "docs",
    ]:
        source = ROOT / name
        if source.is_dir():
            shutil.copytree(source, tmp_path / name, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(source, tmp_path / name)
    return tmp_path


def test_public_ownership_and_index():
    portfolio = check(ROOT)
    assert portfolio.schema_version == "career-public/v1.1"
    assert {project.project_id for project in portfolio.projects} == {"stock", "airplane"}
    for project in portfolio.projects:
        assert project.contribution_status == "owner_confirmed"
        assert project.ownership.model_dump() == {
            "project_type": "personal",
            "scope": "end_to_end",
            "development_mode": "ai_assisted",
            "basis": "owner_statement",
            "confirmed_on": "2026-09-22",
        }
    index = render_index(portfolio)
    assert "owner_review_required" not in index
    assert "owner_confirmed" in index and "AI-Assisted Development" in index


@pytest.mark.parametrize("kind", ["date", "marker", "label", "unconfirmed", "section"])
def test_role_mismatch_fails_before_writing(copied, kind):
    path = copied / "projects/stock.md"
    text = path.read_text(encoding="utf-8")
    if kind == "date":
        text = text.replace("confirmed_on: 2026-09-22", "confirmed_on: 2026-09-21")
    elif kind == "marker":
        text = text.replace("ownership: owner_confirmed", "ownership: owner_review_required")
    elif kind == "label":
        text = text.replace("AI-Assisted Development", "Manual Development")
    elif kind == "section":
        marker = (
            "<!-- ownership: owner_confirmed; basis: owner_statement; confirmed_on: 2026-09-22 -->"
        )
        text = text.replace(marker, "") + "\n" + marker
    else:
        data_path = copied / "data/public/portfolio.json"
        payload = json.loads(data_path.read_text(encoding="utf-8"))
        payload["projects"][0]["contribution_status"] = "owner_review_required"
        del payload["projects"][0]["ownership"]
        data_path.write_text(json.dumps(payload), encoding="utf-8")
    path.write_text(text, encoding="utf-8")
    index = copied / "generated/PROJECT_INDEX.md"
    before = index.read_bytes()
    with pytest.raises(ValueError, match="ownership"):
        check(copied, write=True)
    assert index.read_bytes() == before


def test_ownership_generation_preserves_narratives(copied):
    paths = [copied / name for name in ["README.md", "projects/stock.md", "projects/airplane.md"]]
    before = [path.read_bytes() for path in paths]
    check(copied, write=True)
    assert [path.read_bytes() for path in paths] == before
