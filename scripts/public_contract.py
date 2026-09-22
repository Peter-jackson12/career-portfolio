"""career-public/v1 and v1.1; ownership is separate from evidence verification.

The canonical copy lives in career-agent. career-portfolio vendors this file byte-for-byte.
No network, private fields, arbitrary metadata, or automatic publication is supported.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import unicodedata
from datetime import date
from pathlib import Path
from typing import Annotated, Literal
from urllib.parse import quote

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

Text = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=2000)]
Identifier = Annotated[str, StringConstraints(pattern=r"^[a-z][a-z0-9._-]{0,79}$")]
Repo = Annotated[str, StringConstraints(pattern=r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")]
RelativePath = Annotated[str, StringConstraints(pattern=r"^[A-Za-z0-9_./-]+$")]
SENSITIVE = re.compile(
    r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|"
    r"(?<!\w)(?:\+82[- .]?|0)1[016789][- .]?\d{3,4}[- .]?\d{4}(?!\w)|"
    r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
    r"sk-[A-Za-z0-9_-]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
)
MAX_INPUT_BYTES = 2_000_000


def canonical_term(value: str) -> str:
    value = " ".join(unicodedata.normalize("NFKC", value).casefold().split())
    aliases = {"sklearn": "scikit-learn", "postgres": "postgresql", "py.test": "pytest"}
    return aliases.get(value, value)


def safe_path(value: str) -> str:
    if value.startswith("/") or any(part in {"", ".", ".."} for part in value.split("/")):
        raise ValueError("repository-relative canonical file path required")
    return value


class PublicModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, hide_input_in_errors=True)


class SourceRef(PublicModel):
    repository: Repo
    commit: str = Field(pattern=r"^[0-9a-f]{40}$")
    path: RelativePath

    @model_validator(mode="after")
    def safe_reference(self) -> SourceRef:
        safe_path(self.path)
        if any(part in {".", ".."} for part in self.repository.split("/")):
            raise ValueError("invalid repository")
        return self

    @property
    def url(self) -> str:
        return (
            f"https://github.com/{self.repository}/blob/{self.commit}/{quote(self.path, safe='/')}"
        )


class PublicEvidence(PublicModel):
    evidence_id: Identifier
    statement: Text
    skills: list[Text] = Field(min_length=1, max_length=30)
    source: SourceRef
    scope: Literal["repository_review", "ci_record", "local_report"]
    limitations: list[Text] = Field(min_length=1, max_length=20)


class ProjectOwnership(PublicModel):
    project_type: Literal["personal"]
    scope: Literal["end_to_end"]
    development_mode: Literal["ai_assisted"]
    basis: Literal["owner_statement"]
    confirmed_on: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")

    @model_validator(mode="after")
    def valid_date(self) -> ProjectOwnership:
        date.fromisoformat(self.confirmed_on)
        return self


class PublicProject(PublicModel):
    project_id: Identifier
    name: Text
    repository: Repo
    status: Literal["in_progress", "analysis_complete", "learning", "archived"]
    summary: Text
    case_study: RelativePath
    contribution_status: Literal["owner_review_required", "owner_confirmed"]
    ownership: ProjectOwnership | None = None
    evidence: list[PublicEvidence] = Field(min_length=1, max_length=100)
    limitations: list[Text] = Field(min_length=1, max_length=20)

    @model_validator(mode="after")
    def references(self) -> PublicProject:
        if (self.contribution_status == "owner_confirmed") != (self.ownership is not None):
            raise ValueError("contribution status and ownership must agree")
        safe_path(self.case_study)
        if not self.case_study.startswith("projects/") or not self.case_study.endswith(".md"):
            raise ValueError("case_study must be a projects/*.md file")
        if any(item.source.repository != self.repository for item in self.evidence):
            raise ValueError("project and evidence repository mismatch")
        return self


class PublicPortfolio(PublicModel):
    schema_version: Literal["career-public/v1", "career-public/v1.1"]
    visibility: Literal["public"]
    as_of: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")
    target_roles: list[Text] = Field(min_length=1, max_length=10)
    projects: list[PublicProject] = Field(min_length=1, max_length=50)

    @model_validator(mode="after")
    def integrity(self) -> PublicPortfolio:
        date.fromisoformat(self.as_of)
        if self.schema_version == "career-public/v1" and any(
            project.ownership is not None for project in self.projects
        ):
            raise ValueError("confirmed ownership requires career-public/v1.1")
        project_ids = [p.project_id for p in self.projects]
        evidence_ids = [e.evidence_id for p in self.projects for e in p.evidence]
        if len(set(project_ids)) != len(project_ids) or len(set(evidence_ids)) != len(evidence_ids):
            raise ValueError("duplicate project or evidence IDs")
        # Defense in depth only; free text still requires a human privacy review.
        if SENSITIVE.search(unicodedata.normalize("NFKC", self.model_dump_json())):
            raise ValueError("public content contains a possible contact detail or secret")
        return self

    @property
    def content_hash(self) -> str:
        payload = self.model_dump()
        # Preserve the exact v1 hash preimage: absent ownership was not a null field.
        for project in payload["projects"]:
            if project["ownership"] is None:
                del project["ownership"]
        raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON keys are not accepted")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError("non-finite JSON numbers are not accepted")


def read_json(path: str | Path) -> object:
    if not Path(path).is_file():
        raise ValueError("input must be a regular JSON file")
    with Path(path).open("rb") as stream:
        if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
            raise ValueError("input must be a regular JSON file")
        raw = stream.read(MAX_INPUT_BYTES + 1)
    if len(raw) > MAX_INPUT_BYTES:
        raise ValueError("input exceeds the size limit")
    try:
        return json.loads(
            raw.decode("utf-8-sig"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
        )
    except RecursionError:
        raise ValueError("JSON nesting exceeds the supported depth") from None


def load_portfolio(path: str | Path) -> PublicPortfolio:
    return PublicPortfolio.model_validate(read_json(path))
