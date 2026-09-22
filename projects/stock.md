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
**개인 프로젝트 · End-to-End Project Ownership · AI-Assisted Development**
<!-- ownership: owner_confirmed; basis: owner_statement; confirmed_on: 2026-09-22 -->

원본 체결·호가를 보존하고 같은 입력으로 연구를 다시 검토할 수 있도록 문제와 목표를 정의했습니다.
수집기·운영 화면·연구 워커의 역할 분리, raw 품질 판정과 qualification·replay를 구분하는 데이터 흐름의 설계 판단을 맡았습니다(`stock-pipeline`).

기능 구현 방향과 코드 통합, 검증 전략 및 테스트·결과 검토 기준을 정하고 프로젝트 운영·우선순위·문서화와 최종 의사결정을 책임졌습니다.
SQLite sidecar와 writer 경합을 다루는 합성 회귀를 검토할 때에도 합성 테스트와 실제 시장 데이터 검증의 범위를 구분했습니다(`stock-sidecar-tests`).

ChatGPT·Claude와 Codex/Claude Code를 코드 작성·리뷰·디버깅·테스트·설계 검토·문서화·리팩터링·조사에 활용했습니다.
AI가 제안한 결과를 검토하고 채택·통합할 책임은 제가 가졌습니다. [작성자가 확인한 책임 범위](../docs/OWNERSHIP.md)는 개별 코드의 직접 타이핑이나 특정 로컬 실행자에 대한 주장과 구별합니다.

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
기준 HANDOFF의 **로컬 보고**는 제한 표본에서 품질 문제를 발견해 연구 실행을 보류했다고 기록합니다. 이 문서 작성자가 raw를 재검사한 결과는 아닙니다.
불안전한 sidecar 전환을 반례와 회귀로 남긴 점이 확인 가능한 엔지니어링 결과입니다.

## Limitations
전체 raw 품질 분포·연구 입력 합격·첫 실데이터 백테스트는 기준 revision에서 미완료입니다.
실주문 연결, 전략 수익성, 공급자 데이터 무누락을 주장하지 않습니다.

## What I Learned
설계에서 읽을 수 있는 교훈은 “백테스트가 실행됨”과 “연구 입력을 신뢰할 수 있음”이 다르다는 것입니다.
원본 보존·품질 판정·재생 검증을 분리한 이유도 여기에 있습니다. 개인적인 일화나 특정 실행 경험은 덧붙이지 않습니다.

## Repository / Evidence
- `stock-pipeline`: [역할과 실행 경계](https://github.com/Peter-jackson12/Stock/blob/6a6d6076649befc767e5d8d59151cbcfb2f27c34/README.md)
- `stock-sidecar-tests`: [실패 경계 회귀](https://github.com/Peter-jackson12/Stock/blob/6a6d6076649befc767e5d8d59151cbcfb2f27c34/tests/test_raw_v2_sidecar_lab_boundaries.py)
- [기준 시점 상태와 미완료 판정](https://github.com/Peter-jackson12/Stock/blob/6a6d6076649befc767e5d8d59151cbcfb2f27c34/HANDOFF.md)

[포트폴리오 첫 화면](../README.md) · [기계 판독 근거](../data/public/portfolio.json)
