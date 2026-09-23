# AGENTS.md

## 시작: 이 파일은 짧은 작업 입구다
한국어로 작업한다. 사람을 위한 공개 후보 Portfolio이며 private 취업 workflow는 Career Agent가 담당한다.
먼저 두 저장소의 최신 main, 열린 PR, 각 HEAD/base/CI를 GitHub에서 직접 확인한다.
작업할 ref를 명시한 뒤 이 파일 → [현재 상태](docs/STATUS.md) → [문서 지도](docs/INDEX.md)를 읽는다.
이후 해당 설계·계약·원본 근거만 읽는다. 모든 문서와 긴 과거 대화를 매번 읽지 않는다.
인계문/STATUS의 SHA·테스트 수·PR 상태는 확인 시점의 기록이지 현재 원격 상태를 대체하지 않는다.

## 바꾸지 않을 경계
- 수치·성과·상태 수정 전에 원본 README·코드·테스트·실행 근거와 고정 revision을 확인한다.
- 성능 향상·배포·실데이터 검증·수익성·개인 단독 기여를 추측하지 않는다. 실패와 한계를 보존한다.
- 연락처·실명·정확한 주소·이력서 원문·지원 이력·key/token 및 Agent private 입력은 Git에 넣지 않는다.
  비공개 저장소여도 동일하다. 실제 개인 사실·관심 회사·공고별 review를 운영 문서로 복사하지 않는다.
- 접근 공개 범위를 바꾸지 않는다. 원본 프로젝트의 최신 상태를 확인 없이 공개 snapshot에 덮어쓰지 않는다.
- 사용자의 명시적 승인 범위 밖에서 PR merge, force push, 사용자 로컬 checkout 변경을 하지 않는다.

## 데이터 소유권과 생성
[data/public/portfolio.json](data/public/portfolio.json)은 공개 메타데이터 원본이다.
실행 계약은 Agent의 canonical을 복제한다. 계약 변경 시 양쪽 회귀·lock·Schema를 함께 검증한다.
자동 생성 대상은 generated/PROJECT_INDEX.md뿐이다. README와 사례의 사람 편집 본문은 덮어쓰지 않는다.
사례는 [템플릿](docs/PROJECT_CASE_STUDY_TEMPLATE.md)의 My Role·설계 결정·결과·한계를 포함한다.
명시적으로 확인된 Stock/Airplane의 개인·end-to-end·AI-assisted ownership(확인일 2026-09-22)을 보존한다.
이를 다른 프로젝트의 ownership, 기술 숙련도, 채용 자격, 개별 작성/실행, evidence human verification으로 확대하지 않는다.
확인 상태 변경으로 기술 태그·성과·verified_by/verified_at을 생성하지 않는다. v1 호환과 해시를 보존한다.

## 검증과 종료
[DEVELOPMENT](docs/DEVELOPMENT.md)의 Ruff·tracked guard·pytest를 실행하고 CI의 정확한 HEAD를 확인한다.
계약을 바꾼 경우 --agent-root로 바이트 일치까지 확인한다. --write는 생성 인덱스 갱신에만 사용한다.
실행하지 않은 검사나 skip/deselected를 통과로 보고하지 않는다. 공개 전 개인정보·이력 검토는 별도다.
변경한 구조는 ARCHITECTURE, 계약은 DATA_MODEL, 우선순위는 STATUS/ROADMAP에 반영한다.
다음 인계는 저장소/ref·이번 목표·승인 범위·남은 blocker만 적고 설계와 개인정보를 재복사하지 않는다.
