# 현재 작업 상태

기록일: 2026-09-23. 이 문서는 작업 재개의 지도이며 실시간 원격 상태의 대체물이 아니다.
새 작업에서는 두 저장소 main과 열린 PR의 실제 HEAD/base/CI를 직접 읽는다.

## 현재 원격 기준점

- Portfolio main: `9903971f268bd3484fc0b2c03872a06b7b8110f5` — 문서 기반 인계 PR #2 병합 상태.
- merge 후 main CI: Portfolio checks `35834250332` / push / success.
- Agent main: `252413d0e66c9697bb6ccca2369f55b9f355aa1e` — 회사 facts v2·문서 인계 PR #6 병합 상태.
- 기록 시점에 두 저장소의 열린 PR은 없다. 새 작업 시작 시 다시 확인한다.

PR #2는 운영 입구·구조·문서 책임 분리를 정리한 작업이다.
공개 JSON·근거 revision·성과·ownership·계약을 변경하지 않았다.
원본 Stock/Airplane 프로젝트가 이후 발전해도 이 저장소의 공개 snapshot이 자동 최신화되지는 않는다.

## 현재 역할

이 저장소는 Career System의 **공개 프로젝트/evidence source of truth**다.
개인 경력, 관심 회사, 공고별 human review, private enrichment와 application-prep 결과는 Agent의 로컬 private 영역이 담당한다.
Agent에서 private workflow를 실제로 실행했더라도 그 사실만으로 Portfolio의 기술 태그·성과·숙련도·채용 자격을 새로 만들지 않는다.

현재 공개 서술의 기준일과 한계는 README·프로젝트 사례·`data/public/portfolio.json`에서 확인한다.
공개 evidence를 수정할 때는 원본 프로젝트의 고정 revision과 근거를 다시 검증한다.

## 다음 우선순위

1. 공개 성과 snapshot 또는 기술 태그 갱신 요청이 있을 때 Stock/Airplane 원본 근거를 새로 확인해 별도 PR로 처리한다.
2. Agent의 private 지원 준비가 요구하는 태그를 맞추기 위해 Portfolio evidence를 억지로 추가하지 않는다.
3. 공개 계약 변경이 필요할 때만 Agent canonical contract와 Portfolio 복제본·lock·Schema·양쪽 회귀를 함께 갱신한다.
4. 문서 상태가 실제 main/CI와 다시 어긋나면 STATUS만 짧게 갱신하고 개발일지처럼 누적하지 않는다.

## 새 대화 시작 문장

```text
Career System 작업을 이어간다. 한국어로 작업하라.
Peter-jackson12/career-agent와 career-portfolio의 최신 main/열린 PR/CI를 직접 확인하라.
작업 대상 ref의 AGENTS.md → docs/STATUS.md → docs/INDEX.md를 읽고 해당 업무 문서만 추가로 읽어라.
이번 목표: <목표 한 문장>. 병합 승인 범위: <없음 또는 승인한 PR 번호>.
GitHub 가능한 작업은 직접 수행하고, private/실제 DB/Windows 전용 실행만 로컬로 넘겨라.
```

## 유지 규칙

완료/미완료/사용자 승인/로컬 미확인을 구분한다. CI 결과를 쓸 때는 정확한 HEAD와 run을 함께 기록한다.
개인 학력·경력·연락처·선호 회사·공고별 review는 이 문서에 넣지 않는다.
설계 상세를 계속 덧붙이지 말고 INDEX의 해당 문서를 수정한다.
