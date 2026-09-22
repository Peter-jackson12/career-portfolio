# 데이터 모델과 두 저장소의 연결

## 소유권
원본 구현과 실험 결과는 Stock/Airplane이 소유합니다. 이 저장소의 `projects/`는 사람이 편집하는 설명,
`data/public/portfolio.json`은 공개 가능한 프로젝트 메타데이터와 검토한 근거 목록입니다.
같은 수치를 여러 페이지에 복제하지 않고 고정 revision의 원본으로 연결합니다.

Career Agent는 공개 JSON을 읽어 로컬 공고와 비교합니다. Agent의 지원 DB·연락처·원문 자료는
이 저장소로 역전송하지 않습니다. GitHub 공개 설정과 JSON의 `visibility: public`은 별개입니다.
후자는 공개 허용 데이터 계약이라는 뜻이며 인터넷에 게시했다는 뜻이 아닙니다.

## career-public/v1
`schema_version`, `visibility`, `as_of`, `target_roles`, `projects`만 최상위에서 허용합니다.
프로젝트는 고정 ID, 이름, repository, 상태, 설명, 사례 경로, 기여 검토 상태, evidence, limitations를 가집니다.
근거는 ID, statement, skills, repository/full commit/path, scope, limitations를 가집니다.
임의 metadata·이메일·전화·주소·실제 경력 원문은 허용하지 않습니다.

`scope`는 repository_review / ci_record / local_report를 구분합니다. 현재 실제 네 근거는
repository_review입니다. CI 성공을 직접 읽은 실행 근거처럼, 로컬 보고를 재실행처럼 바꾸지 않습니다.
`contribution_status: owner_review_required`는 아직 프로젝트 책임에 대한 명시적 확인이 없는 상태입니다. Stock/Airplane은 작성자 확인에 따라 owner_confirmed입니다.
목표 직무는 지원 방향이며 기존 재직 이력이 아닙니다. 취업용 문구로 확정하기 전 본인이 검토합니다.

## JSON을 고른 이유
표준 라이브러리로 읽을 수 있고 타입·허용 필드·버전·해시를 검증하기 쉽습니다.
서술은 Markdown으로 유지해 JSON 안에 긴 자기소개나 이력서 전체를 넣지 않습니다.
실행 모델의 원본은 Career Agent `src/career_agent/public_contract.py`이며,
이 저장소는 같은 파일을 `scripts/public_contract.py`에 그대로 보관합니다.
작은 계약을 위해 별도 배포 패키지나 비공개 저장소 간 CI 인증 토큰을 만들지 않았습니다.

[JSON Schema](../schemas/career-public-v1.schema.json)는 편집·기본 검증용입니다.
중복 ID, 출처 간 일치, 민감 문자열 같은 추가 검사는 Python 모델이 수행합니다.
JSON Schema 통과만으로 전체 검증이 끝나지 않습니다.

## 생성과 사람 편집의 경계
`generated/PROJECT_INDEX.md`만 자동 생성합니다. README와 사례 문장은 생성기가 덮어쓰지 않습니다.
각 사례의 숨은 project/status/as_of 표시는 데이터와 설명의 기준이 어긋나는 것을 탐지합니다.
표시 일치가 문장 의미나 기여를 사실 검증해주는 것은 아닙니다.
계약 복제본은 `contracts.lock.json` 해시로 검사하며, 두 저장소를 로컬에 둔 경우
`python scripts/check_portfolio.py --agent-root ../career-agent`로 바이트 일치를 검증합니다.

[개발 절차](DEVELOPMENT.md) · [개인정보 경계](PRIVACY.md)

## Ownership 계약 v1.1
`career-public/v1.1`은 프로젝트 `contribution_status: owner_confirmed`와 `ownership`을 함께 받습니다.
ownership은 `project_type: personal`, `scope: end_to_end`, `development_mode: ai_assisted`,
`basis: owner_statement`, ISO 날짜 `confirmed_on`으로 구성하며 필드는 모두 필수입니다.
확인 상태와 객체의 불일치·유효하지 않은 날짜는 거부합니다. 프로젝트 이름으로 확인을 추론하지 않습니다.
확인되지 않은 프로젝트는 `owner_review_required`와 ownership 생략/null을 사용합니다.
v1은 기존 미확인 입력을 계속 지원하고 확인 객체는 v1.1에서만 받습니다.
기존 v1 content hash는 빈 ownership 필드를 제외하여 보존합니다. v1.1의 확인 정보는 해시에 포함됩니다.

프로젝트 ownership은 문제 정의·목표·방향·설계 판단·코드 통합·검증 기준·운영·우선순위·문서화·최종 결정의 책임입니다.
개별 코드/테스트를 직접 작성한 사람, 특정 실행자나 AI 코드 비율을 뜻하지 않습니다.
repository evidence, skill proficiency, job qualification, evidence verification은 별개입니다.
확인으로 기술 태그나 verified_by/verified_at을 만들지 않으며 기존 근거와 한계는 보존합니다.
Python 검증은 날짜의 실재성과 버전/상태/객체 관계도 검사합니다. JSON Schema만으로 이 검사를 대신하지 않습니다.

Stock/Airplane은 2026-09-22 owner statement를 반영합니다. 생성 전에 My Role의 ownership marker·날짜·개인 프로젝트/End-to-End/AI-Assisted 표기를 대조합니다. 이는 정해진 표기의 일치 검사이며 자연어 전체의 사실 검증은 아닙니다.
