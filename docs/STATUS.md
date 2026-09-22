# 현재 작업 상태

기록일: 2026-09-22. 이 문서는 작업 재개의 지도이며 실시간 원격 상태의 대체물이 아니다.
새 작업에서는 두 저장소 main과 열린 PR의 실제 HEAD/base/CI를 직접 읽는다.

## 검토한 기준점
- Portfolio main: `d19b2eb3787144aaa6abe746bc61f5199650ac45` — PR #1 병합 상태.
- 이 문서 변경은 운영 입구·구조·문서 책임 분리다. 공개 JSON·근거 revision·성과·ownership·계약은 수정하지 않는다.
- 원본 프로젝트가 이후 발전했더라도 이 저장소의 snapshot이 자동 최신화되지는 않는다.
  현재 공개 서술의 기준일과 한계는 README·프로젝트 사례·공개 JSON에서 확인한다.

## 다음 우선순위
1. 현재 운영 문서 PR의 diff·CI를 확인한다. 병합은 명시적 사용자 승인 후에만 한다.
2. Agent의 회사 facts/선호 정책과 private 검토 workflow를 안정화한다. 이 작업은 Portfolio 공개 계약 개정이 아니다.
3. 공개 성과 snapshot 갱신을 요청받으면 Stock/Airplane 원본 근거를 새로 확인해 별도 변경으로 처리한다.

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
