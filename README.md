# Career Portfolio

**데이터 분석·데이터 사이언스 직무를 위한 프로젝트 포트폴리오입니다.**
Stock과 Airplane은 **개인 프로젝트**입니다. 문제 정의부터 설계·코드 통합·검증 기준·운영과 최종 의사결정까지 책임졌습니다.
아래 결과는 **2026-09-22에 검토한 고정 revision 기준**이며 실시간 진행률이 아닙니다.

## 대표 프로젝트

### Stock — 틱 수집과 재현 연구
체결·호가의 원본 보존, 수집·입력 품질 판정·재생을 나누는 구조와 검증 방향을 관리했습니다.
SQLite sidecar와 writer 경합의 실패 조건을 합성 회귀로 다룹니다.
**진행 중:** 전체 실데이터 품질 판정과 첫 백테스트는 기준 revision에서 미완료입니다. 수익성을 주장하지 않습니다.

[문제·선택·검증·내 역할](projects/stock.md) · [원본 저장소](https://github.com/Peter-jackson12/Stock)

### Airplane — 지연 분류와 데이터 품질
전처리의 의미와 예측 성능을 분리해 검토하도록 연구 방향·평가 경계·구현 통합을 맡았습니다.
**전처리 비교 완료:** 의미는 개선됐지만 Macro F1 향상은 확인하지 못했습니다.
날씨 수집 이후 전체 결합·모델 비교는 별도 검증 단계입니다.

[분석·결과·한계·내 역할](projects/airplane.md) · [원본 저장소](https://github.com/Peter-jackson12/Airplane)

## 개발 방식과 근거

ChatGPT·Claude·Codex/Claude Code를 구현·리뷰·디버깅·테스트·문서화 등의 개발 보조로 활용했습니다.
프로젝트 방향, 아키텍처, 검증 기준과 최종 결과의 채택·통합은 제가 통제했습니다.
[ownership 확인 범위](docs/OWNERSHIP.md)와 [코드·테스트 근거 인덱스](generated/PROJECT_INDEX.md)는 서로 다른 사실을 설명합니다.
기술 태그는 숙련도·채용 요건 충족 인증이 아닙니다. 목표 직무는 지원 방향이지 재직 직함이 아닙니다.

## 다른 분석과 학습

[KRX EDA · 추론통계 · 제품 분석](projects/learning.md)을 별도 묶음으로 제공합니다.
Stock·Airplane의 개인 프로젝트 확인을 다른 저장소의 개인 기여 확인으로 확대하지 않습니다.

## 운영 안내

Portfolio는 사람이 읽는 공개 후보 자료, Career Agent는 로컬 지원 준비 시스템입니다.
현재 접근 설정은 **비공개**이며 연락처·이력서 원본·지원 기록을 추가하지 않습니다.
[데이터·연결 계약](docs/DATA_MODEL.md) · [개인정보 점검](docs/PRIVACY.md) ·
[개발·검증](docs/DEVELOPMENT.md) · [Roadmap](docs/ROADMAP.md) · [감사 기록](docs/AUDIT_20260922.md)
