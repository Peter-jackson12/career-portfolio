# 유지보수와 검증

Python 3.11 이상을 사용합니다. 저장소 루트에서 실행합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
ruff check .
ruff format --check .
python scripts/check_portfolio.py --write
python scripts/check_portfolio.py --tracked
python -m pytest -q
```

Linux/macOS는 활성화만 `source .venv/bin/activate`로 바꿉니다.
`--write`는 공개 JSON으로 `generated/PROJECT_INDEX.md`만 갱신합니다.
CI는 lint·format도 확인하며 네트워크로 다른 비공개 저장소를 읽지 않고 데이터·계약 해시·Schema·사례 구조·상대 링크·추적 파일을 검증합니다.
현재 검사기는 외부 URL 존재, Markdown 절 anchor, 모바일 실제 기기 렌더링과 문장 의미를 자동 인증하지 않습니다.

## 변경 순서
원본 revision과 근거를 먼저 검토합니다. 공개 JSON의 as_of/status/근거를 바꾸고 사례의 숨은 표시와 설명을 맞춥니다.
생성 인덱스를 갱신하고 위 검증을 실행한 뒤 브랜치·PR로 검토합니다.
이 저장소의 데이터는 공개 후보이므로 실제 private 공고나 이력서를 테스트 입력으로 쓰지 않습니다.

## 계약 변경
Career Agent의 canonical Python 모델을 먼저 수정하고 가상 회귀를 통과시킵니다.
`src/career_agent/public_contract.py`를 이 저장소 `scripts/public_contract.py`로 그대로 복사합니다.
`contracts.lock.json`의 SHA-256과 생성 Schema를 의도적인 변경으로 함께 검토합니다.

```powershell
python -c "import hashlib; from pathlib import Path; print(hashlib.sha256(Path('scripts/public_contract.py').read_bytes()).hexdigest())"
python -c "import sys,json; sys.path.insert(0,'scripts'); from public_contract import PublicPortfolio; from pathlib import Path; Path('schemas/career-public-v1.schema.json').write_text(json.dumps(PublicPortfolio.model_json_schema(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')"
python scripts/check_portfolio.py --agent-root ../career-agent
```

해시 갱신은 자동 동기화가 아니며 변경 내용을 검토한 뒤 수행합니다. 양쪽 의미를 바꾸는 변경은 계약 버전과 migration을 함께 설계합니다.
[사례 템플릿](PROJECT_CASE_STUDY_TEMPLATE.md) · [Roadmap](ROADMAP.md)

## Ownership 변경 검증
canonical 계약 → 복제본/lock/Schema → 공개 JSON → My Role 일치 검사 → 생성 인덱스 순서로 갱신합니다.
`python scripts/check_portfolio.py --agent-root ../career-agent --write --tracked`와 전체 pytest/Ruff를 실행합니다.
My Role 표기 불일치는 파일 생성 전에 거부하며 README와 사례의 사람 편집 본문은 생성하지 않습니다.
