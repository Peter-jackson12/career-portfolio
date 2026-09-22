# Career Portfolio

**데이터 분석·데이터 사이언스 직무를 위한 프로젝트 포트폴리오입니다.**
데이터 입력의 의미, 기술적 선택, 검증 결과와 남은 한계를 코드·문서로 연결합니다.
아래 상태는 **2026-09-22에 검토한 고정 revision 기준**이며 실시간 진행률이 아닙니다.

## 대표 프로젝트

### Stock — 틱 수집과 재현 연구
초봉으로 잃기 쉬운 체결·호가 이벤트를 보존하고 수집·입력 검증·재생의 책임을 나눴습니다.
SQLite sidecar 정리와 writer 경합의 실패 조건을 합성 회귀로 다룹니다.
**구현·합성 검증 진행 중:** 전체 실데이터 품질 판정과 첫 백테스트는 기준 revision에서 미완료입니다.

[문제·선택·검증·역할](projects/stock.md) · [원본 저장소](https://github.com/Peter-jackson12/Stock)

### Airplane — 지연 분류와 데이터 품질
모호한 결측 대치를 줄이고 모델 선택과 최종 평가 데이터를 분리해 전처리 변경을 비교했습니다.
**전처리 비교 완료:** 의미는 개선됐지만 Macro F1 향상은 확인하지 못했습니다.
날씨 수집 이후 전체 결합·모델 비교는 별도 검증 단계입니다.

[분석·결과·한계·역할](projects/airplane.md) · [원본 저장소](https://github.com/Peter-jackson12/Airplane)

## 근거와 개인 기여

Python·SQLite·pytest는 Stock의 코드와 실패 경계에서, scikit-learn·LightGBM은 Airplane의 평가와 결과에서 확인합니다.
[근거 인덱스](generated/PROJECT_INDEX.md)는 evidence ID와 고정 원본 파일로 연결됩니다.
기술 태그는 숙련도 평가가 아닙니다. **My Role은 본인 확인 전 상태**이며 직접 담당한 결정·구현·검증과 팀/AI 도구 지원을 구분해 확정해야 합니다.
목표 직무도 현재 프로젝트 기반 지원 방향이지 재직 직함이나 경력 인증이 아닙니다.

## 다른 분석과 학습

[KRX EDA · 추론통계 · 제품 분석](projects/learning.md)을 별도 묶음으로 제공합니다.
탐색·교육 결과를 실거래 수익성이나 실제 사업 성과로 표현하지 않습니다.

## 운영 안내

Portfolio는 사람이 읽는 공개용 후보 자료, Career Agent는 로컬 지원 준비 시스템입니다.
현재 접근 설정은 **비공개**이며 연락처·이력서 원본·지원 기록을 추가하지 않습니다.
[데이터·연결 계약](docs/DATA_MODEL.md) · [개인정보 점검](docs/PRIVACY.md) ·
[개발·검증](docs/DEVELOPMENT.md) · [Roadmap](docs/ROADMAP.md) · [감사 기록](docs/AUDIT_20260922.md)
