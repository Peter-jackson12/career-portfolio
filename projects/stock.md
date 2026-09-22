# Stock — 틱 수집과 재현 연구

<!-- project: stock; status: in_progress; as_of: 2026-09-22 -->

**기준일 2026-09-22 · 상태: 진행 중 · source revision `6a6d6076649befc767e5d8d59151cbcfb2f27c34`**

## Problem
체결·호가를 초봉으로만 변환하면 구간 안의 이벤트 순서와 원래 관측값을 잃을 수 있습니다.
전략 점수보다 먼저 어떤 입력을 보존했고 어떤 검증을 통과했는지 설명할 수 있어야 합니다.

## Context
로컬 Windows·OCX와 Git 제외 시장 데이터에 의존합니다. 기존 LOB/초봉 경로를 유지하면서
raw-v2 수집과 틱 연구 경로를 분리합니다. CI 합성 데이터와 실제 시장 데이터를 같은 근거로 취급하지 않습니다.

## My Role
개인 저장소에서 수집·연구 시스템을 발전시키는 프로젝트입니다.
이 사례는 코드와 문서에서 확인한 설계·검증 범위를 설명하며, 모든 코드를 혼자 작성했다는 주장이 아닙니다.
**본인 확인 필요:** 직접 작성한 구현, 직접 내린 설계 결정, AI 도구의 구현 지원 범위를 구분한 기여 문장.
커밋 작성자만으로 개인의 숙련도나 팀 기여율을 추정하지 않습니다.

## Approach
원문과 정규화 기록을 구분하고, 수집 종료의 일관성 확인과 연구 입력 합격을 분리합니다.
운영 화면·수집기·작업 워커를 별도 프로세스로 두어 실패와 제어의 책임을 나눕니다.

## Architecture / Pipeline
```text
raw-v2 수집 → 종료 근거 대조 → 제한 표본 → 전체 품질/무결성 판정
                                                ↓ 합격 후
                           이벤트 재생 → 연구 결과와 재현성 확인
```
단계별 운영 절차이며 한 번에 실행되는 자동 명령이라는 뜻은 아닙니다.

## Key Technical Decisions
원본 보존을 우선해 품질 문제가 있는 입력을 백테스트 후보로 승격하지 않습니다.
SQLite read-only 연결이 sidecar를 전혀 만들지 않는다고 가정하지 않으며,
잠금을 풀고 쓰기 연결을 여는 in-place 정리는 경쟁 writer가 들어올 수 있어 채택하지 않았습니다.
레거시 변환 자산은 삭제하지 않고 결과 계약을 분리해 유지합니다.

## Validation
`stock-sidecar-tests`는 Windows 핸들·부분 정리·writer 경합·경로 교체의 합성 회귀 코드를 가리킵니다.
이 사례 작성에서는 원격 코드를 읽었으며 실제 raw 전체 검사나 Windows 로컬 실행을 재수행하지 않았습니다.
CI 통과와 운영 데이터 인증을 구별합니다.

## Results
수집·제어·입력 검증·연구 실행을 구분한 구현과 문서가 존재합니다(`stock-pipeline`).
제한 표본에서 품질 문제를 확인한 상태를 숨기지 않고 전체 검증 전 연구 실행을 보류합니다.
불안전한 sidecar 전환을 반례와 회귀로 남긴 점이 확인 가능한 엔지니어링 결과입니다.

## Limitations
전체 raw 품질 분포·연구 입력 합격·첫 실데이터 백테스트는 기준 revision에서 미완료입니다.
실주문 연결, 전략 수익성, 공급자 데이터 무누락을 주장하지 않습니다.

## What I Learned
이 프로젝트가 보여주는 판단은 “백테스트가 실행됨”보다 “입력을 믿을 수 있는 조건”이 먼저라는 것입니다.
개인 회고로 제출할 때는 본인이 겪은 사건과 결정으로 확인한 뒤 작성합니다.

## Repository / Evidence
- `stock-pipeline`: [역할과 실행 경계](https://github.com/Peter-jackson12/Stock/blob/6a6d6076649befc767e5d8d59151cbcfb2f27c34/README.md)
- `stock-sidecar-tests`: [실패 경계 회귀](https://github.com/Peter-jackson12/Stock/blob/6a6d6076649befc767e5d8d59151cbcfb2f27c34/tests/test_raw_v2_sidecar_lab_boundaries.py)
- [기준 시점 상태와 미완료 판정](https://github.com/Peter-jackson12/Stock/blob/6a6d6076649befc767e5d8d59151cbcfb2f27c34/HANDOFF.md)

[포트폴리오 첫 화면](../README.md) · [기계 판독 근거](../data/public/portfolio.json)
