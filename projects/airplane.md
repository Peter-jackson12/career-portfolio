# Airplane

**항공편 지연 예측과 날씨 정보 확장**

<!-- project: airplane; status: in_progress; as_of: 2026-10-09 -->

[포트폴리오](../README.md) / 대표 프로젝트 02

**후속 실험 후보 남음** · 기준일 2026-10-09  
Source revision: `56f91bbe966c86ea7eec7b94103a10ae039b979b` (2026-10-08)

[문제](#problem) · [내 역할](#my-role) · [설계](#architecture--pipeline) · [검증](#validation) · [결과](#results) · [한계](#limitations) · [원본 근거](#repository--evidence)  
[Tableau Public 대시보드 →](https://public.tableau.com/app/profile/.82847805/viz/airplane_portfolio/1)

---

> 전처리의 타당성과 새 정보의 예측력을 별도로 검증했습니다. 전처리 비교 255,001행과 날씨 비교 180,332행은 서로 다른 평가 집단입니다.

## Problem
불완전한 항공편 데이터를 단순히 채워 넣으면 모호한 항공사 대응과 시각 의미를 숨길 수 있습니다.
전처리의 타당성과 모델 성능을 서로 다른 질문으로 검증하는 것이 목표입니다.

## Context
원본은 100만 행이며 직접 모델 평가한 라벨 집단은 255,001행입니다.
미국 BTS 운항 자료로 706,759행의 날짜를 귀속하고, 그중 라벨이 있는 180,332행에서 날씨 유무를 비교했습니다.
원본·날씨 cache는 Git 제외 데이터입니다. 전처리 비교(255,001행)와 날씨 비교(180,332행)는 서로 다른 평가 집단입니다.
현지 HHMM 차이를 시간대가 보정된 비행시간이라고 부르지 않습니다.

## My Role
**개인 프로젝트 · End-to-End Project Ownership · AI-Assisted Development**
<!-- ownership: owner_confirmed; basis: owner_statement; confirmed_on: 2026-09-22 -->

불완전한 항공편 데이터에서 전처리의 타당성과 예측 성능을 별도로 확인하도록 문제와 연구 목표를 정의했습니다.
전처리·평가·BTS 날짜 귀속·날씨 확장의 데이터 흐름과 기술적 판단을 맡고, 공통 평가 설정과 모델 선택·채점 경계를 구분하는 방향을 관리했습니다(`airplane-cv`).

기능 구현 방향과 코드 통합, 검증 전략 및 테스트·결과 검토 기준을 정했습니다.
전처리 의미 개선과 Macro F1 향상 미확인을 구별하고, 날씨 수집 이후의 결합·모델 비교를 별도 단계로 관리했습니다(`airplane-findings`).
작업 우선순위·프로젝트 운영·문서화와 최종 의사결정도 제가 책임졌습니다.

ChatGPT·Claude와 Codex/Claude Code를 구현·리뷰·디버깅·테스트·설계 검토·문서화·리팩터링·조사에 활용했습니다.
개발 도구의 지원을 받되 방향·검증 기준·결과 채택과 통합은 제가 통제했습니다. [작성자가 확인한 책임 범위](../docs/OWNERSHIP.md)는 모든 실험을 직접 실행하거나 모든 코드를 손으로 작성했다는 의미가 아닙니다.

## Approach
항공사 코드가 유일하게 대응하는 경우만 결측을 채우고, 미상 시각은 결측 플래그와 함께 보존합니다.
모델 선택과 채점의 경계를 나눠 동일한 평가 조건으로 전처리 변경을 비교합니다.
외부 BTS 자료로 뒷받침되는 행만 날짜를 채택하고 날씨 확장으로 연결합니다.

## Architecture / Pipeline
```text
원본 품질 점검 → 의미 보존 전처리 → inner 선택 / outer 평가 → OOF 비교
별도 확장: 날짜 귀속 → station·시각 계약 → 날씨 수집 → point-in-time 결합 → 날씨 유무 비교 → 분류기 비교·확률 보정
공개: 기존 실행 근거 → 집계 CSV 15개 → Tableau Public 대시보드 3종
```
예측 시점 이후 관측은 결합하지 않으며, 날씨 공개 지연 10분은 실측이 아닌 사전 가정입니다.

## Key Technical Decisions
모호한 대응을 첫 관측값으로 채우지 않고, 추정값과 원래 관측값의 이력을 보존합니다.
`CVConfig`로 평가 설정을 공유하고 early stopping과 임계값 선택이 채점 데이터에 기대지 않도록 구분합니다.
과거 호환 함수의 교차 fold 의존성 한계도 숨기지 않습니다(`airplane-cv`).

## Validation
전처리 비교는 10조건 × 3시드 × 5-fold, 날씨 비교는 동일 180,332행·동일 시드(42/1/7)·동일 외부 5-fold의 쌍비교입니다.
Logistic Regression·Random Forest·LightGBM은 같은 폴드에서 모델별 사전 선언 후보와 내부 선택 경계로 비교했습니다.
이 사례에서는 README와 평가 코드를 검토했으며 모델을 재학습하지 않았습니다.
검증 대상은 정적 라벨 집단이며 미래 운영 성능이나 모든 과거 실행 경로를 인증하지 않습니다.

## Results
전처리 의미와 검증 구조는 개선했지만 **전처리 수정만으로는 Macro F1 향상을 확인하지 못했습니다**(`airplane-findings`).
날씨 14개 피처를 추가하자 Macro F1 0.573910 → 0.598945, LogLoss 0.448116 → 0.436689, ROC-AUC 0.640618 → 0.672936으로
세 시드 모두 세 지표가 같은 방향으로 개선됐습니다. 주된 구성은 지연 오경보 감소이며 지연 recall 증가는 작았습니다.
같은 조건의 분류기 비교에서는 시험한 탐색 예산 모두에서 Random Forest가 LightGBM·Logistic Regression보다 앞섰고,
확률 보정은 ECE를 줄였지만 LogLoss·Macro F1과 분류기 순서는 거의 바꾸지 않았습니다.
결과는 Tableau Public 대시보드 3종(지연 패턴·날씨와 지연·모델 오류)으로 게시했습니다(`airplane-dashboards`).
수치표 전체는 [기준 결과 설명](https://github.com/Peter-jackson12/Airplane/blob/56f91bbe966c86ea7eec7b94103a10ae039b979b/README.md)과 [대시보드](https://public.tableau.com/app/profile/.82847805/viz/airplane_portfolio/1)에 연결합니다.

## Limitations
정적 교차검증의 예측력 차이이며 날씨의 인과 효과나 미래 운항 성능을 뜻하지 않습니다. 배포 모델로 확정하지 않았습니다.
분류기 비교는 사전 선언한 유한 탐색 예산 안의 결과이며 Random Forest가 일반적으로 더 낫다는 근거가 아닙니다.
날짜 귀속 채택은 원본 전체의 완전 복원이 아니며, 원본 시각이 모두 결측인 3,031행은 날씨 평가 집단에 포함되지 않습니다.
시간 순서 검증·실서비스 시점의 정보 가용성·서빙은 별도 검증이 필요합니다.

## What I Learned
결과를 해석할 때 전처리의 타당성과 분류 성능을 같은 개선으로 취급해서는 안 됩니다.
성능이 오르지 않은 비교도 다음 정보원을 검토할 근거로 남길 수 있습니다. 이는 기록된 설계와 결과에 대한 해석이며 개인적인 발견 일화는 추가하지 않습니다.

## Repository / Evidence
- `airplane-cv`: [공통 평가 설정과 검증 경계](https://github.com/Peter-jackson12/Airplane/blob/56f91bbe966c86ea7eec7b94103a10ae039b979b/src/cv.py)
- `airplane-findings`: [데이터 분모·결과·한계](https://github.com/Peter-jackson12/Airplane/blob/56f91bbe966c86ea7eec7b94103a10ae039b979b/README.md)
- `airplane-dashboards`: [Tableau 집계 CSV 생성 스크립트](https://github.com/Peter-jackson12/Airplane/blob/56f91bbe966c86ea7eec7b94103a10ae039b979b/scripts/build_tableau_extracts.py) · [Tableau Public](https://public.tableau.com/app/profile/.82847805/viz/airplane_portfolio/1)

[포트폴리오 첫 화면](../README.md) · [기계 판독 근거](../data/public/portfolio.json)
