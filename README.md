# Career Portfolio

> 데이터 기반 문제를 **정의하고, 검증 가능한 파이프라인으로 만들고, 결과의 한계까지 설명하는 과정**을 보여주는 포트폴리오입니다.

이 저장소는 이력서와 GitHub 프로젝트 사이를 연결하는 **포트폴리오 허브**입니다.  
상세 구현과 실행 근거는 각 프로젝트 저장소에 두고, 여기서는 채용 담당자가 빠르게 읽을 수 있도록 **문제 → 접근 → 검증 → 결과 → 한계** 순서로 핵심만 정리합니다.

---

## Featured Projects

| 프로젝트 | 한 줄 설명 | 핵심 역량 | 상세 |
|---|---|---|---|
| **Stock — 틱 수집과 재현 연구** | 원본 체결·호가 이벤트를 수집하고 틱 단위 전략 재현의 정확성을 검증하는 연구·운영 파이프라인 | Python · 데이터 파이프라인 · 이벤트 재생 · 테스트 · Streamlit | [Case Study](projects/stock.md) · [Repo](https://github.com/Peter-jackson12/Stock) |
| **Airplane — 항공편 지연 분류** | 100만 행 항공편 데이터의 결측·시각·식별 문제를 점검하고 누수를 피하는 평가 경로를 설계 | Python · LightGBM · CV/OOF · 데이터 품질 · 실험 설계 | [Case Study](projects/airplane.md) · [Repo](https://github.com/Peter-jackson12/Airplane) |
| **KRX Quant EDA** | 약 70만 행 KRX 시세 데이터의 무결성·결측·이상치를 검증하고 시장/섹터 특성을 분석 | Pandas · EDA · 금융 데이터 · 시각화 · 도메인 검증 | [Repository](https://github.com/Peter-jackson12/finance) |
| **Inferential Statistics & DOE** | 가설검정부터 ANOVA, 회귀, A/B 테스트 표본 설계까지 재현 가능한 노트북으로 정리 | SciPy · 통계적 추론 · A/B Test · 회귀 · 실험계획 | [Repository](https://github.com/Peter-jackson12/inferential_stats_and_doe_2) |

### Learning & Engineering Log

수업에서 배운 개념뿐 아니라 프로젝트에서 실제로 만난 문제, 실험, 해결 과정을 [`TIL`](https://github.com/Peter-jackson12/TIL)에 기록합니다.

---

## What I Focus On

### 1. 데이터가 맞는지 먼저 확인합니다
결측률을 낮추거나 모델 점수를 높이는 것보다 **그 값이 무엇을 의미하는지, 어떤 조건에서 믿을 수 있는지**를 먼저 확인합니다.

### 2. 평가와 선택의 경계를 분리합니다
검증 데이터가 모델 선택에 섞이지 않도록 평가 경계를 명시하고, 결과를 재현할 수 있는 실행 경로를 남깁니다.

### 3. 실패한 실험도 결과로 남깁니다
성능 향상이 없거나 가설이 틀렸더라도 조건과 결과를 기록합니다. 포트폴리오에서는 성공한 숫자보다 **판단 근거와 검증 과정**을 보여주는 것을 우선합니다.

### 4. 코드와 설명이 서로 검증되게 만듭니다
README의 주장, 코드, 테스트, 생성물의 역할을 분리하고 가능하면 서로 교차 확인할 수 있게 구성합니다.

---

## Project Case Study Format

각 주요 프로젝트는 아래 흐름으로 요약합니다.

1. **Problem** — 어떤 문제를 풀려고 했는가
2. **Data & Constraints** — 데이터와 현실적인 제약은 무엇이었는가
3. **Approach** — 어떤 설계와 방법을 선택했는가
4. **Validation** — 무엇을 어떻게 검증했는가
5. **Result** — 확인된 결과는 무엇인가
6. **Limitations** — 아직 주장할 수 없는 것은 무엇인가
7. **Evidence** — 코드, 테스트, 문서, 실행 결과로 어디에서 확인할 수 있는가

새 case study를 작성할 때는 [`docs/PROJECT_CASE_STUDY_TEMPLATE.md`](docs/PROJECT_CASE_STUDY_TEMPLATE.md)를 사용합니다.

---

## Repository Role

```text
career-portfolio/
├── README.md                         # 채용 담당자용 첫 화면
├── AGENTS.md                         # AI/에이전트 작업 원칙
├── projects/
│   ├── stock.md
│   └── airplane.md
└── docs/
    ├── PROJECT_CASE_STUDY_TEMPLATE.md
    └── ROADMAP.md
```

이 저장소에는 다른 프로젝트의 코드를 복제하지 않습니다.  
프로젝트별 구현은 원래 저장소를 **single source of truth**로 유지하고, 여기서는 채용 관점의 요약과 링크만 관리합니다.

---

## Next

현재는 **Markdown 기반 포트폴리오 허브**를 먼저 구축하는 단계입니다.  
콘텐츠가 안정되면 GitHub Pages용 웹 UI를 얹고, 이후 동일한 내용을 기반으로 한 PDF 이력서와 연결할 예정입니다.