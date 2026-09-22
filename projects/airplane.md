# Airplane — 항공편 지연 분류와 데이터 품질

<!-- project: airplane; status: in_progress; as_of: 2026-09-22 -->

**기준일 2026-09-22 · 상태: 확장 실험 진행 중 · source revision `0e1495c5f17deb958e6dce623eea78cb96cb54c4`**

## Problem
불완전한 항공편 데이터를 단순히 채워 넣으면 모호한 항공사 대응과 시각 의미를 숨길 수 있습니다.
전처리의 타당성과 모델 성능을 서로 다른 질문으로 검증하는 것이 목표입니다.

## Context
원본은 100만 행이며 직접 모델 평가한 라벨 집단은 255,001행입니다.
원본·날씨 cache는 Git 제외 데이터입니다. 날짜 귀속 집단과 모델 평가 집단은 같은 분모가 아닙니다.
현지 HHMM 차이를 시간대가 보정된 비행시간이라고 부르지 않습니다.

## My Role
프로젝트의 전처리·평가·외부 데이터 확장 과정을 정리한 사례입니다.
아래 설명은 저장소 수준의 구현과 결과이지 개인의 단독 구현 인증이 아닙니다.
**본인 확인 필요:** 직접 담당한 전처리·실험·설계 검토, 팀 작업과 AI 도구의 지원 범위.
코드에 존재하는 모든 기능을 개인 경력으로 자동 변환하지 않습니다.

## Approach
항공사 코드가 유일하게 대응하는 경우만 결측을 채우고, 미상 시각은 결측 플래그와 함께 보존합니다.
모델 선택과 채점의 경계를 나눠 동일한 평가 조건으로 전처리 변경을 비교합니다.
외부 BTS 자료로 뒷받침되는 행만 날짜를 채택하고 날씨 확장으로 연결합니다.

## Architecture / Pipeline
```text
원본 품질 점검 → 의미 보존 전처리 → inner 선택 / outer 평가 → OOF 비교
별도 확장: 날짜 귀속 → station·시각 계약 → 날씨 수집 → point-in-time 결합 → 날씨 유무 비교
```
날씨 수집 완료를 전체 결합이나 모델 성능 검증 완료로 해석하지 않습니다.

## Key Technical Decisions
모호한 대응을 첫 관측값으로 채우지 않고, 추정값과 원래 관측값의 이력을 보존합니다.
`CVConfig`로 평가 설정을 공유하고 early stopping과 임계값 선택이 채점 데이터에 기대지 않도록 구분합니다.
과거 호환 함수의 교차 fold 의존성 한계도 숨기지 않습니다(`airplane-cv`).

## Validation
기준 README는 10조건 × 3시드 × 5-fold의 전처리 비교를 보고합니다.
이 사례에서는 README와 평가 코드를 검토했으며 모델을 재학습하지 않았습니다.
검증 대상은 정적 라벨 집단이며 미래 운영 성능이나 모든 과거 실행 경로를 인증하지 않습니다.

## Results
전처리 의미와 검증 구조는 개선했지만 **Macro F1 향상은 확인하지 못했습니다**(`airplane-findings`).
날씨 transport는 완료됐고 point-in-time 결합 코드가 추가됐지만,
전체 706,759행 결합 실행과 weather-on 모델 비교는 기준 커밋에서 미실행입니다.
수치표를 복제하기보다 [기준 결과 설명](https://github.com/Peter-jackson12/Airplane/blob/0e1495c5f17deb958e6dce623eea78cb96cb54c4/README.md)에 연결합니다.

## Limitations
확률 보정 개선과 분류 성능 개선은 다릅니다. 날씨 추가의 성능 향상도 아직 주장하지 않습니다.
날짜 귀속 채택은 원본 전체의 완전 복원이 아니며 보류된 행을 감추지 않습니다.
실서비스 시점의 정보 가용성·서빙·운영 효과는 별도 검증이 필요합니다.

## What I Learned
**설계에 대한 해석이며 개인 회고는 미확인입니다.** 이 프로젝트는 결측률 감소나 높은 점수보다 값의 의미와 평가 경계가 먼저임을 보여줍니다.
실패한 성능 개선 실험도 다음 정보원 선택의 근거가 됩니다. 개인 회고 문장은 본인 경험 확인 후 제출합니다.

## Repository / Evidence
- `airplane-cv`: [공통 평가 설정과 검증 경계](https://github.com/Peter-jackson12/Airplane/blob/0e1495c5f17deb958e6dce623eea78cb96cb54c4/src/cv.py)
- `airplane-findings`: [데이터 분모·결과·미완료 범위](https://github.com/Peter-jackson12/Airplane/blob/0e1495c5f17deb958e6dce623eea78cb96cb54c4/README.md)
- [결합 코드 추가 시점의 실행 범위](https://github.com/Peter-jackson12/Airplane/commit/0e1495c5f17deb958e6dce623eea78cb96cb54c4)

[포트폴리오 첫 화면](../README.md) · [기계 판독 근거](../data/public/portfolio.json)
