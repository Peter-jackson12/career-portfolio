from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from check_portfolio import check, forbidden_path, plain, render_index, tracked_guard

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def copied(tmp_path):
    for name in ["README.md", "contracts.lock.json", "data", "schemas", "scripts",
                 "generated", "projects", "docs"]:
        source = ROOT / name
        if source.is_dir():
            shutil.copytree(source, tmp_path / name, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy2(source, tmp_path / name)
    return tmp_path


def test_real_public_contract_and_index():
    portfolio = check(ROOT)
    assert len(portfolio.projects) == 2
    assert sum(len(p.evidence) for p in portfolio.projects) == 4
    assert render_index(portfolio) == (ROOT / "generated/PROJECT_INDEX.md").read_text(encoding="utf-8")


@pytest.mark.parametrize("path", ["private/profile.json", "data/private.json", ".env",
                                  "docs/resume.pdf", "notes/history.sqlite3"])
def test_forbidden_runtime_paths(path):
    assert forbidden_path(path)


def test_public_data_allowed():
    assert not forbidden_path("data/public/portfolio.json")


@pytest.mark.parametrize("kind", ["index", "contract", "schema", "status", "source", "link"])
def test_corruption_is_rejected(copied, kind):
    paths = {"index": "generated/PROJECT_INDEX.md", "contract": "scripts/public_contract.py",
             "schema": "schemas/career-public-v1.schema.json", "status": "projects/stock.md",
             "source": "projects/stock.md", "link": "README.md"}
    path = copied / paths[kind]
    text = path.read_text(encoding="utf-8")
    if kind in {"index", "contract"}:
        text += "\nmodified\n"
    elif kind == "schema":
        text = "{}"
    elif kind == "status":
        text = text.replace("status: in_progress", "status: analysis_complete")
    elif kind == "source":
        text = text.replace("stock-sidecar-tests", "wrong-id")
    else:
        text += "\n[missing](does-not-exist.md)\n"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError):
        check(copied)


def test_cross_repository_contract_mismatch(copied, tmp_path):
    agent = tmp_path / "agent"
    path = agent / "src/career_agent/public_contract.py"
    path.parent.mkdir(parents=True)
    path.write_text("different")
    with pytest.raises(ValueError, match="contracts differ"):
        check(copied, agent_root=agent)


def test_public_contact_rejected(copied):
    path = copied / "data/public/portfolio.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["projects"][0]["summary"] = "person" + "@" + "example.invalid"
    path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(ValueError):
        check(copied)


def test_generator_does_not_change_narrative(copied):
    path = copied / "projects/stock.md"
    before = path.read_bytes()
    (copied / "generated/PROJECT_INDEX.md").write_text("stale")
    check(copied, write=True)
    assert path.read_bytes() == before


def test_literal_markdown_labels():
    assert "<script>" not in plain("<script>")
    assert "[text](url)" not in plain("[text](url)")


def test_tracked_guard_runs():
    tracked_guard(ROOT)
