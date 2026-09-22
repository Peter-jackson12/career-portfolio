"""Offline contract, generated-output, local-link and tracked-file checks."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import unicodedata
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

from public_contract import SENSITIVE, PublicPortfolio, load_portfolio

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "Problem",
    "Context",
    "My Role",
    "Approach",
    "Architecture / Pipeline",
    "Key Technical Decisions",
    "Validation",
    "Results",
    "Limitations",
    "What I Learned",
    "Repository / Evidence",
)
PRIVATE_DIRS = {
    "private",
    "profile",
    "resumes",
    "applications",
    "cover_letters",
    "exports",
    "raw",
    "cookies",
    "sessions",
    "browser-data",
    ".auth",
}


def plain(value: str) -> str:
    for char in "\\`*_{}[]<>()#!|":
        value = value.replace(char, "\\" + char)
    return value.replace("\n", " ").replace("\r", " ")


def render_index(portfolio: PublicPortfolio) -> str:
    lines = [
        "# 프로젝트 근거 인덱스",
        "",
        "자동 생성 파일입니다. 직접 수정하지 않습니다.",
        f"기준일: {portfolio.as_of} · 계약: {portfolio.schema_version}",
        "",
    ]
    for project in portfolio.projects:
        lines.extend(
            [
                f"## {plain(project.name)}",
                "",
                f"상태: `{project.status}` · 개인 기여: `{project.contribution_status}`",
                f"[사례 읽기](../{project.case_study})",
                "",
            ]
        )
        for evidence in project.evidence:
            lines.append(
                f"- `{evidence.evidence_id}` — {plain(', '.join(evidence.skills))} "
                f"— [{evidence.source.path}]({evidence.source.url})"
            )
        lines.append("")
    lines.extend(
        ["근거 링크는 파일 위치를 고정할 뿐 개인 기여나 성과를 자동 인증하지 않습니다.", ""]
    )
    return "\n".join(lines)


def forbidden_path(path: str) -> bool:
    if "\\" in path or ":" in path:
        return True
    parts = PurePosixPath(path).parts
    if not parts:
        return True
    name = parts[-1].lower()
    if any(part.lower() in PRIVATE_DIRS for part in parts[:-1]):
        return True
    if path.casefold().startswith("data/") and path != "data/public/portfolio.json":
        return True
    return (
        name.startswith((".env", "secrets.", "cookies.", "session.", "storage_state"))
        and name != ".env.example"
    ) or bool(re.search(r"\.(?:db|sqlite\d*)(?:$|[-.])|\.(?:pem|key|pdf|docx)$", name))


def local_path(root: Path, path: Path) -> Path:
    """Validate containment before reading; no external links through local paths."""
    root = root.resolve()
    relative = path.absolute().relative_to(root)
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError("repository paths must not be symlinks")
    if not path.resolve().is_relative_to(root):
        raise ValueError("repository path escapes the root")
    return path


def sensitive_text(content: str) -> bool:
    return bool(SENSITIVE.search(unicodedata.normalize("NFKC", content)))


def tracked_guard(root: Path) -> None:
    raw = subprocess.run(
        ["git", "ls-files", "--stage", "-z"], cwd=root, check=True, capture_output=True
    ).stdout
    for item in raw.split(b"\0"):
        if not item:
            continue
        metadata, relative = item.decode("utf-8").split("\t", 1)
        if metadata.split()[0] not in {"100644", "100755"} or forbidden_path(relative):
            raise ValueError("forbidden tracked path or Git mode")
        path = local_path(root, root / relative)
        if sensitive_text(path.read_text(encoding="utf-8")):
            raise ValueError("possible contact detail or secret in tracked text")


def check(root: Path, agent_root: Path | None = None, write: bool = False) -> PublicPortfolio:
    root = root.resolve()
    portfolio = load_portfolio(local_path(root, root / "data/public/portfolio.json"))
    contract = local_path(root, root / "scripts/public_contract.py").read_bytes()
    lock = json.loads(local_path(root, root / "contracts.lock.json").read_text(encoding="utf-8"))
    if not isinstance(lock, dict) or lock.get("sha256") != hashlib.sha256(contract).hexdigest():
        raise ValueError("vendored contract differs from lock")
    if agent_root is not None:
        canonical = agent_root / "src/career_agent/public_contract.py"
        if canonical.read_bytes() != contract:
            raise ValueError("Agent and Portfolio contracts differ")
    expected_schema = PublicPortfolio.model_json_schema()
    actual_schema = json.loads(
        local_path(root, root / "schemas/career-public-v1.schema.json").read_text(encoding="utf-8")
    )
    if actual_schema != expected_schema:
        raise ValueError("JSON Schema differs from executable contract")
    for project in portfolio.projects:
        narrative = local_path(root, root / project.case_study).read_text(encoding="utf-8")
        marker = (
            f"<!-- project: {project.project_id}; status: {project.status}; "
            f"as_of: {portfolio.as_of} -->"
        )
        if marker not in narrative or any(
            f"## {heading}\n" not in narrative for heading in REQUIRED
        ):
            raise ValueError("case study structure or status marker differs")
        for evidence in project.evidence:
            if f"`{evidence.evidence_id}`" not in narrative or evidence.source.url not in narrative:
                raise ValueError("case study is missing an evidence ID or pinned source")
    index = local_path(root, root / "generated/PROJECT_INDEX.md")
    if index.is_symlink() or not index.resolve().is_relative_to(root):
        raise ValueError("generated index must remain inside the repository")
    for path in [
        root / "README.md",
        *sorted((root / "docs").glob("*.md")),
        *sorted((root / "projects").glob("*.md")),
        index,
    ]:
        path = local_path(root, path)
        content = render_index(portfolio) if path == index else path.read_text(encoding="utf-8")
        if sensitive_text(content):
            raise ValueError("possible contact detail or secret in public narrative")
        for url in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", content):
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                if parts.scheme not in {"http", "https"} or not parts.netloc:
                    raise ValueError("only HTTP(S) external links are accepted")
                continue
            if not parts.path:
                continue
            target = (path.parent / unquote(parts.path)).resolve()
            if not target.is_relative_to(root) or not target.exists():
                raise ValueError("broken or escaping local Markdown link")
    if write:
        index.parent.mkdir(parents=True, exist_ok=True)
        index.write_text(render_index(portfolio), encoding="utf-8", newline="\n")
    if index.read_text(encoding="utf-8") != render_index(portfolio):
        raise ValueError("generated index is stale; run --write")
    return portfolio


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="refresh generated index only")
    parser.add_argument("--agent-root", type=Path, help="optional cross-repository byte comparison")
    parser.add_argument("--tracked", action="store_true", help="check Git tracked paths and text")
    args = parser.parse_args()
    try:
        portfolio = check(ROOT, args.agent_root, args.write)
        if args.tracked:
            tracked_guard(ROOT)
    except (ValueError, OSError, UnicodeError, subprocess.SubprocessError):
        print("Portfolio validation failed; check contract, source links and privacy boundaries.")
        return 1
    print(f"Portfolio checks passed: {len(portfolio.projects)} projects; {portfolio.content_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
