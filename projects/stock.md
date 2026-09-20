# Stock — Tick Collection & Replay Research

> **핵심 질문:** 원본 체결·호가 이벤트를 어떤 형태로 보존하고 재생해야 틱 단위 전략의 결과를 신뢰할 수 있는가?

- **Repository:** https://github.com/Peter-jackson12/Stock
- **Focus:** 데이터 수집 · 이벤트 재생 · 가상 체결 · 운영/분석 UI · 회귀 테스트
- **Stack:** Python · Streamlit · pytest · SQLite/시장 데이터 · GitHub Actions

## 1. Problem
주식 전략을 초·분봉으로만 재현하면 같은 시간 구간 안에서 실제 체결과 호가가 어떤 순서로 발생했는지 잃을 수 있습니다. 이 프로젝트는 원본 체결·호가 이벤트를 보존하고, 이후 연구 단계에서 같은 입력을 다시 재생할 수 있는 구조를 만드는 데 초점을 둡니다.

단순히 백테스트 수익률을 출력하는 것이 아니라 **입력 데이터가 무엇인지, 어떤 변환을 거쳤는지, 어느 단계까지 검증되었는지**를 구분하는 것이 핵심 요구사항입니다.

## 2. Data & Constraints
- 실제 시장 데이터와 키움 OCX 등 일부 실행 환경은 로컬에만 존재합니다.
- GitHub CI의 합성 테스트 성공은 실제 시장 데이터 검증 완료를 뜻하지 않습니다.
- 기존 LOB/초봉 변환 경로와 새 틱 연구 경로가 공존하므로 결과 계약을 혼동하지 않아야 합니다.
- 실제 주문 연결과 전략 수익성 입증은 별도 단계입니다.

## 3. Approach
1. 신규 수집 데이터를 `raw-v2` 계약으로 보존하고 원문과 정규화 기록을 구분합니다.
2. 이벤트 재생·가상 체결·전략 로직을 수집기와 분리합니다.
3. 운영 화면, 수집기, 작업 워커를 별도 프로세스로 두어 역할과 실패 경계를 나눕니다.
4. `HANDOFF`, `BACKTEST_TODO`, `PIPELINE_MAP` 등 문서별 책임을 분리해 현재 상태와 과거 기록을 구분합니다.
5. 레거시 경로를 제거하기보다 현재 연구 경로와 계약을 명시적으로 분리합니다.

## 4. Validation
- push/PR마다 Windows + Python 3.14 환경에서 Git-only pytest를 실행합니다.
- 파일 잠금, 프로세스, 소켓 등 운영 경계에 대한 합성 회귀 테스트를 포함합니다.
- Git-only 검증과 로컬 실데이터 검증을 문서상 별도 단계로 관리합니다.
- 실제 연구 전에는 제한 표본과 입력 계약을 먼저 확인하는 절차를 둡니다.

## 5. Result
현재 저장소는 **틱 수집 → 입력 검증 → 이벤트 재생 → 연구 실행**을 분리해 다룰 수 있는 연구·운영 구조를 갖추고 있습니다. 또한 기존 LOB/초봉 기반 자산을 유지하면서 새 틱 연구 경로를 독립적으로 발전시킬 수 있게 정리했습니다.

이 결과를 전략 수익성이나 실거래 성과로 해석하지 않습니다.

## 6. What I Changed / Learned
초기에는 백테스트 엔진과 파생 데이터 중심으로 문제를 보았지만, 프로젝트가 커지면서 **재현 가능한 연구의 선행 조건은 전략 코드보다 입력 데이터의 계약과 실행 경계를 명확히 하는 것**이라는 점이 더 중요해졌습니다.

그래서 데이터 수집, 변환, 검증, 재생, 결과 저장과 운영 화면의 책임을 나누고, 문서도 “현재 상태”와 “과거 설계 기록”을 분리하는 방향으로 바꿨습니다.

## 7. Limitations
- 실제 주문 연결은 검증 범위 밖입니다.
- 실데이터 백테스트와 수익성 검증은 로컬 데이터가 필요한 별도 단계입니다.
- 합성/CI 통과만으로 수집 데이터의 실제 품질을 보증할 수 없습니다.

## 8. Evidence
- [Main README](https://github.com/Peter-jackson12/Stock)
- [Pipeline Map](https://github.com/Peter-jackson12/Stock/blob/master/docs/PIPELINE_MAP.md)
- [Testing Guide](https://github.com/Peter-jackson12/Stock/blob/master/docs/TESTING.md)
- [Tick Research Runbook](https://github.com/Peter-jackson12/Stock/blob/master/TICK_RESEARCH_RUNBOOK.md)

## 30-second Summary
원본 체결·호가 이벤트를 보존하고 다시 재생할 수 있도록 주식 연구 파이프라인을 재구성한 프로젝트입니다. 수집기·운영 UI·이벤트 재생·가상 체결을 분리하고, 합성 CI와 실제 시장 데이터 검증의 경계도 명시했습니다. 목표는 화려한 백테스트 숫자보다 **같은 입력으로 같은 연구를 다시 수행하고 그 결과를 검증할 수 있는 구조**를 만드는 것입니다.