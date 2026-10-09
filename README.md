# Career Portfolio

**데이터 분석·데이터 사이언스 직무를 위한 프로젝트 포트폴리오입니다.**
Stock과 Airplane은 **개인 프로젝트**입니다. 문제 정의부터 설계·코드 통합·검증 기준·운영과 최종 의사결정까지 책임졌습니다.
아래 결과는 **고정 revision 기준**이며(Airplane 2026-10-08, Stock 2026-09-29 revision, 2026-10-09 검토) 실시간 진행률이 아닙니다.

**바로가기:** [Stock](https://github.com/Peter-jackson12/Stock) · [Airplane](https://github.com/Peter-jackson12/Airplane) · [학습 기록(TIL)](https://github.com/Peter-jackson12/TIL) · [분석·학습 묶음](projects/learning.md)

## 대표 프로젝트

### Stock — 틱 수집과 이벤트 기반 백테스트 연구
주식 체결·호가 원본을 수집·보존하고 이벤트 단위로 재생해 전략을 검증하는 연구 파이프라인입니다.
제한 범위의 실제 데이터로 이벤트 재생·가상체결·결과 대조와 재현성을 확인했습니다.
정밀 재생 결과와의 일치를 검증한 빠른 백테스트(screening 전용)와, 1,286개 셀 다조건 실행·중단 후 재개가 가능한 실행 구조를 구현했습니다.
**진행 중:** 전체 원본 데이터의 품질 검증, 실거래 적용, 수익성 검증은 별도 과제입니다.

[문제·선택·검증·내 역할](projects/stock.md) · [원본 저장소](https://github.com/Peter-jackson12/Stock)

### Airplane — 지연 예측과 날씨 정보 확장
전처리의 의미와 새 정보(날씨)의 예측력을 나눠 검증하도록 연구 방향·평가 경계·구현 통합을 맡았습니다.
**전처리 수정:** 의미는 개선됐지만 Macro F1 향상은 확인하지 못했습니다.
**날씨 추가:** 동일 180,332행·동일 폴드 비교에서 Macro F1 0.574 → 0.599 등 세 지표가 세 시드 모두 개선됐습니다(정적 교차검증, 인과 효과 아님).
분류기 3종 비교·확률 보정까지 진행했고, 결과를 Tableau Public 대시보드 3종으로 게시했습니다.

[분석·결과·한계·내 역할](projects/airplane.md) · [원본 저장소](https://github.com/Peter-jackson12/Airplane) · [Tableau 대시보드](https://public.tableau.com/app/profile/.82847805/viz/airplane_portfolio/1)

## 개발 방식과 근거

ChatGPT·Claude·Codex/Claude Code를 구현·리뷰·디버깅·테스트·문서화 등의 개발 보조로 활용했습니다.
프로젝트 방향, 아키텍처, 검증 기준과 최종 결과의 채택·통합은 제가 통제했습니다.
[ownership 확인 범위](docs/OWNERSHIP.md)와 [코드·테스트 근거 인덱스](generated/PROJECT_INDEX.md)는 서로 다른 사실을 설명합니다.
기술 태그는 숙련도·채용 요건 충족 인증이 아닙니다. 목표 직무는 지원 방향이지 재직 직함이 아닙니다.

## 다른 분석과 학습

[KRX EDA · 추론통계 · 제품 분석](projects/learning.md)을 별도 묶음으로 제공합니다.
[TIL](https://github.com/Peter-jackson12/TIL)은 2026년 8월부터 이어 온 데이터 사이언스·AI 교육 과정의 학습·실습 일지입니다.
Stock·Airplane의 개인 프로젝트 확인을 다른 저장소의 개인 기여 확인으로 확대하지 않습니다.

## 운영 안내

Portfolio는 사람이 읽는 공개 후보 자료, Career Agent는 로컬 지원 준비 시스템입니다.
현재 공개 저장소이며 연락처·이력서 원본·지원 기록을 추가하지 않습니다.
[작업 입구](AGENTS.md) · [현재 상태](docs/STATUS.md) · [문서 지도](docs/INDEX.md) · [구조와 파이프라인](docs/ARCHITECTURE.md)

[데이터·연결 계약](docs/DATA_MODEL.md) · [개인정보 점검](docs/PRIVACY.md) ·
[개발·검증](docs/DEVELOPMENT.md) · [Roadmap](docs/ROADMAP.md) · [감사 기록](docs/AUDIT_20260922.md)
