# 현금흐름표 연구실 — 직접법·간접법에서 생성AI 검산까지

**회계·재무분석 연구실 10-1** · 글 · 안상선 ((주)M-Robo 대표) · 2026-11-06

▶ 페이지 보기: https://adminmrobo.github.io/cashflow-lab/

박사·조수 하루·초파리 연구원·주판봇이 진행하는 한 페이지 해설입니다. 계정과목을 한글 그대로 쓰면서 현금흐름표를 **직접법과 간접법** 두 길로 계산하고, 실제 공시 사례로 "손실 회사의 현금"을 읽은 뒤, 작성 원칙을 **프롬프트**로 바꿔 생성AI가 쓴 **파이썬 코드**를 공시 숫자로 **검산**합니다.

> 핵심 질문: 손실이 581억 원인데, 현금은 왜 186억 원 늘었을까?

## 무엇을 다루나

| 부 | 칸 | 내용 | 자료 |
|---|---|---|---|
| 1부 | ① 등식 | 기말 − 기초 = 영업 + 투자 + 재무 | (주)SG화학 2014 (10주차 예제) |
| | ② 직접법 | 항목별 실제 현금 — 잔액을 움직여 보는 조절기 | SG화학 |
| | ③ 간접법 | 당기순이익 170 → 영업현금 270, 다섯 계단 | 서울(주) 2014 |
| | ④ 사례 | 순손실 581.2억, 영업현금 −511.6억, 재무 +786.2억 | (주)뤼튼테크놀로지스 2025 감사보고서 (DART, 2026-04-14) |
| | ⑤ 비교 | 순손실 중 현금 손실의 비율 — 공정가치 평가손실의 효과 | 오픈AI·Anthropic (보도·제3자 분석) |
| 2부 | ⑥ 원칙 | 현금흐름표 작성 원칙 여덟 가지 | K-IFRS 제1007호, 일반기업회계기준 |
| | ⑦ 프롬프트 | 원칙 + 검산 A~E + 출력 형식 | `code/prompt_cashflow.md` |
| | ⑧ AI 코드 | 생성AI가 쓴 pandas 코드를 사람 말로 읽기 | `code/wrtn_cashflow.py` |
| | ⑨ 검산 | 흔한 실수 네 가지를 켜고 검산이 잡는지 보기 | 공시 숫자 |
| | 대결 | 재무상태표만 본 AI 초안(−507.5억) vs 공시 대조 검산(−511.6억) | |

맨 끝에 **지식 색인**(검색·관계 지도)과 **온톨로지·서지 꾸러미**(JSON-LD·Turtle·CSV·CSL-JSON·BibTeX·RIS, ZIP)가 있습니다.

## 저장소 구조

```
index.html                  ← 해설 페이지 (단일 파일, 캐릭터 그림 포함)
.nojekyll · .gitignore      ← GitHub Pages 설정, 올리지 않을 파일
README.md
code/
  prompt_cashflow.md        ← 생성AI에 붙여 넣는 프롬프트 (원칙 + 검산 A~E)
  wrtn_cashflow.py          ← 뤼튼 2025 간접법·직접법 재구성·검산 (Colab에 그대로)
  sg_chemical.py            ← 10주차 예제 직접법·간접법
data/
  wrtn_2025_balance.csv           ← 재무상태표 영업 관련 계정 (기초·기말, 원)
  wrtn_2025_cashflow_disclosed.csv← 공시 현금흐름표 조정 항목 (원)
docs/
  wrtn_output.txt, sg_output.txt  ← 코드 실제 실행 결과
  IMG_10-1_cashflow.md            ← 이미지 제작 명세서
  COVER_00_index.md               ← 글 표지 생성 지시문 (Genspark 등)
tools/
  template.html, kg_data.py, build.py  ← index.html 다시 만들기
assets/
  sprites_page.js           ← 이 페이지에 쓴 캐릭터 표정 21종 (base64)
```

## GitHub에 올리기

**웹에서 올릴 때:** 새 저장소를 만들고 *Add file → Upload files*로 이 폴더 안의 모든 파일·폴더를 끌어다 놓습니다. `index.html`과 `README.md`가 저장소 맨 위에 있어야 합니다. 숨김 파일 `.nojekyll`도 함께 올립니다.

**명령줄로 올릴 때:**

```bash
cd cashflow-lab
git init -b main
git config user.name  "adminmrobo"
git config user.email "sangsun.ahn@gmail.com"
git add .
git commit -m "현금흐름표 연구실 10-1 첫 공개"
git remote add origin https://github.com/adminmrobo/cashflow-lab.git
git push -u origin main
```

## GitHub Pages로 열기

1. Settings → Pages → Source: *Deploy from a branch*, Branch: `main` / `(root)` → Save.
2. 1~2분 뒤 **https://adminmrobo.github.io/cashflow-lab/** 에서 열립니다.
3. 라이선스를 정하면 `tools/kg_data.py`의 `META`에 `license`를 채우고 `python tools/build.py`로 다시 만듭니다(꾸러미의 인용 정보에 들어갑니다).

페이지는 외부 스크립트 없이 동작합니다. 외부 요청은 글꼴(IBM Plex Sans KR) 하나이고, 브라우저 저장소·쿠키를 쓰지 않습니다.

## 코드 실행

Colab 새 셀에 `code/wrtn_cashflow.py` 전체를 붙여 넣고 실행합니다. 자료가 코드 안에 들어 있어 파일이 필요 없습니다.

```
python code/wrtn_cashflow.py
```

```
영업활동 현금흐름: -511.6 억원 (공시 -511.6 )
현금 증가: 186.4 | 기초 90.1 → 기말 276.5
검산 A·B·C·E 통과
[검산 D: 공시 조정액 vs 재무상태표 증감, 차이가 있는 계정]  선급비용 · 미지급금 · 미지급비용
```

다른 회사로 해 보려면 `code/prompt_cashflow.md`의 프롬프트에 그 회사 감사보고서의 재무상태표·손익계산서·현금흐름표를 붙여 넣으세요. AI가 만든 코드는 **반드시 검산 A~E를 통과한 뒤** 씁니다.

## 페이지 다시 만들기

```
python tools/build.py      # template.html + code/ + docs/ + kg_data.py → index.html
```

## 출처와 확인 상태

| 자료 | 상태 |
|---|---|
| (주)뤼튼테크놀로지스 제5기 감사보고서, 대주회계법인, DART 2026-04-14 | 원문 PDF에서 직접 옮김. 일반기업회계기준, 감사의견 적정. 전기(2024) 재무제표는 감사받지 않음 |
| 10주차 강의 교안 「현금흐름표와 재무분석」 | 원문에서 직접 옮김 |
| Anthropic 2025 숫자 | 2026-10-26 제출로 보도된 S-1을 인용한 제3자 분석(sec-api.io, Cestrian). SEC 원문 미확인 |
| OpenAI 2025 숫자 | 유출된 감사 재무제표를 FT가 검증했다는 보도(CleanTechnica, Yahoo Finance). 회사 공식 공시 아님. 영업현금흐름 미보도 |
| K-IFRS 제1007호, 일반기업회계기준, IFRS 18 | 문단 번호는 쓰지 않음. 현행 조문과 국내 적용 시점은 한국회계기준원에서 확인 |

## 알림

- 이 페이지는 교육용이며 세무·회계·투자 자문이 아닙니다.
- ② 슬라이더 값, ⑨ 실수 시뮬레이션, 대결의 초안 값, 현금 런웨이(7.7개월)는 설명용 계산입니다. ⑧ 직접법은 공시에 없는 강의용 재구성입니다(미수금을 고객 현금에 넣는 가정).
- 캐릭터(박사·조수 하루·초파리 연구원·주판봇)의 이름·설정·그림은 저작권자 안상선에게 있으며 허락 없이 쓸 수 없습니다. 주판봇은 연구실 캐릭터이며 극 중 대사는 비유일 뿐입니다.

© 2026 안상선 (Ahn Sangsun) · [소개](https://adminmrobo.github.io/who_am_i/who_am_i.html)
