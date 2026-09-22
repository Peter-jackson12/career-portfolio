"""Regression checks for review findings, without private data or live network access."""

import json
import shutil
import subprocess
from pathlib import Path

import pytest
from check_portfolio import check, forbidden_path, local_path, sensitive_text, tracked_guard

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def copied(tmp_path):
    for name in [
        "README.md",
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


@pytest.mark.parametrize(
    "path",
    [
        "Data/private.json",
        "DATA/PUBLIC/portfolio.json",
        "notes/cover_letters/draft.md",
        "profile/info.json",
        "browser-data/storage.json",
        "state/storage_state.json",
    ],
)
def test_guard_case_and_runtime_paths(path):
    assert forbidden_path(path)


def test_nonsecret_environment_example_policy_is_consistent():
    assert not forbidden_path(".env.example")
    assert forbidden_path(".env.production")


def test_fullwidth_contact_in_narrative_is_rejected(copied):
    path = copied / "README.md"
    digits = "０１０" + "－" + "１２３４" + "－" + "５６７８"
    path.write_text(path.read_text(encoding="utf-8") + "\n" + digits, encoding="utf-8")
    with pytest.raises(ValueError, match="contact"):
        check(copied)


def test_non_sensitive_technical_strings_are_allowed():
    assert not sensitive_text("SHA-256 abc123, scikit-learn, CV/OOF, 100만 행")


def test_schema_still_matches_canonical_export():
    from public_contract import PublicPortfolio

    schema = json.loads((ROOT / "schemas/career-public-v1.schema.json").read_text(encoding="utf-8"))
    assert schema == PublicPortfolio.model_json_schema()


def test_symlink_narrative_is_not_read(copied, tmp_path):
    # Outside the copied root, but still inside pytest's temporary parent.
    external = tmp_path.parent / f"{tmp_path.name}-outside.md"
    external.write_text("private material", encoding="utf-8")
    path = copied / "projects/stock.md"
    path.unlink()
    try:
        path.symlink_to(external)
    except OSError:
        pytest.skip("symlink privilege not available")
    with pytest.raises(ValueError, match="symlink"):
        check(copied)
    with pytest.raises(ValueError):
        local_path(copied, external)


@pytest.mark.parametrize("url", ["file:///tmp/private", "javascript:alert", "//example.invalid/x"])
def test_unsupported_link_scheme(copied, url):
    path = copied / "README.md"
    path.write_text(path.read_text(encoding="utf-8") + f"\n[bad]({url})\n", encoding="utf-8")
    with pytest.raises(ValueError, match="HTTP"):
        check(copied)


def test_invalid_narrative_does_not_modify_generated_index(copied):
    path = copied / "README.md"
    path.write_text(
        path.read_text(encoding="utf-8") + "\n[missing](missing.md)\n", encoding="utf-8"
    )
    index = copied / "generated/PROJECT_INDEX.md"
    before = index.read_bytes()
    with pytest.raises(ValueError):
        check(copied, write=True)
    assert index.read_bytes() == before


def test_index_symlink_mode_is_blocked_even_on_plaintext_checkout(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    (tmp_path / "README.md").write_text("external-path")
    blob = (
        subprocess.run(
            ["git", "hash-object", "-w", "--stdin"],
            input=b"external-path",
            cwd=tmp_path,
            capture_output=True,
            check=True,
        )
        .stdout.decode()
        .strip()
    )
    subprocess.run(
        ["git", "update-index", "--add", "--cacheinfo", f"120000,{blob},README.md"],
        cwd=tmp_path,
        check=True,
    )
    with pytest.raises(ValueError, match="Git mode"):
        tracked_guard(tmp_path)
