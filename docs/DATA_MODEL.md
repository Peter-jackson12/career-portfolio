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
`contribution_status: owner_review_required`는 저장소 검토가 개인의 기여 인증이 아님을 뜻합니다.
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
