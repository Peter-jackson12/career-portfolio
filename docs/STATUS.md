# 현재 작업 상태

기록일: 2026-11-02. 이 문서는 작업 재개의 지도이며 실시간 원격 상태의 대체물이 아니다.
새 작업에서는 두 저장소 main과 열린 PR의 실제 HEAD/base/CI를 직접 읽는다.

## 현재 원격 기준점

- 이 갱신의 시작 Portfolio main: `ede02f0cee5b4ec123fc5aa616af18b45522e3c3`. 병합 뒤 실제 HEAD와 CI는 GitHub에서 확인한다.
- Agent의 최신 결론은 Agent의 docs/STATUS.md가 소유한다.

GitHub Pages 배포는 수행하지 않았다.
원본 Stock/Airplane 프로젝트가 이후 발전해도 이 저장소의 공개 snapshot이 자동 최신화되지는 않는다.

## 2026-11-01 사례 가시성 갱신

- 두 사례 첫머리에 요약 표와 구조도를 두고, 설계·검증·역할 설명에 그림을 연결했다. 그림 기준은 [VISUAL_STYLE](VISUAL_STYLE.md#사례-구조도)을 따른다.
- Stock 수치와 문구는 Stock 총괄 세션이 사용자 확인과 내부 검토를 거쳐 보낸 자료만 썼다. 연구 결과는 전체를 단정하지 않고 실행별 범위를 밝혀 기각 결과를 그대로 적었다.
- 이전 공개본에서 바꾼 표현은 이 저장소의 과거 커밋에 남아 있다. 이력 수정은 별도 계획과 승인이 필요하다.
- AI TOP 100 예선 과제는 문제 내용을 뺀 추상화본만 별도 사례로 넣었다. 대회 컨트롤 세션이 공개 문구를 대조했고, 공개 데이터 계약의 evidence에는 넣지 않았다. 2026-11-04 결과 안내 뒤 결과 표기를 고친다.
- 11/2 이후를 포함한 Stock 합계나 범위를 쓰려면 Stock 총괄 세션에 먼저 확인한다.
- Airplane evidence를 `6a17568`(2026-10-12)로 옮겼다. `616827b` 이후 변경은 문서·테스트뿐이며 사례의 수치는 대조해 일치함을 확인했다.
- `earthquake`(4인 팀 프로젝트)와 `ML_3`(수업 실습)는 README가 없고 개인 담당 범위가 확정되지 않아 추가하지 않았다. `earthquake`는 2026-11-02 사용자 결정으로 이번에도 뺐다.
- 2026-11-02 사용자 지시로 첫 화면의 대표 프로젝트를 Stock 하나로 하고, AI TOP 100을 두 번째, Airplane을 그 다음으로 옮겼다. 세 프로젝트의 대표 구조도를 첫 화면에 넣었다. 새 수치는 없다.

## 현재 역할

이 저장소는 Career System의 **공개 프로젝트/evidence source of truth**다.
개인 경력, 관심 회사, 공고별 human review, private enrichment와 application-prep 결과는 Agent의 로컬 private 영역이 담당한다.
Agent에서 private workflow를 실제로 실행했더라도 그 사실만으로 Portfolio의 기술 태그·성과·숙련도·채용 자격을 새로 만들지 않는다.

현재 공개 서술의 기준일과 한계는 README·프로젝트 사례·`data/public/portfolio.json`에서 확인한다.
공개 evidence를 수정할 때는 원본 프로젝트의 고정 revision과 근거를 다시 검증한다.

## 다음 우선순위

현재 디자인은 README와 프로젝트 문서에 반영됐다. 별도 웹사이트 개발·배포 완료로 해석하지 않는다.

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
