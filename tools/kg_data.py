"""지식 그래프(kg-raw), JSON-LD, 참고문헌(CSL-JSON), 페이지 서지(page-meta) — build.py가 index.html에 넣는다."""
import json

PAGE = "acct_cashflow_01"

def N(id, type, ko, en, anchor, d="", family="cash-flow", domain=("acct",), conf="high", ev=(), src=(), level=2, extra=None):
    n = {"id": id, "type": type, "label": {"ko": ko, "en": en}, "page": PAGE, "anchor": anchor,
         "level": level, "family": family, "domain": list(domain), "anchorType": "D", "flyStrength": "none",
         "status": "known", "confidence": conf, "evidence": list(ev), "source": [{"cite": s} for s in src],
         "match": [], "tags": []}
    if d: n["definition"] = {"ko": d}
    if extra: n.update(extra)
    return n

STD = {"jurisdiction": "K-IFRS", "asOf": "2026-11-06"}
KRG = {"jurisdiction": "KR-GAAP", "asOf": "2025-12-31"}

nodes = [
    N("lab:concept/cash-flow-statement", "Concept", "현금흐름표", "statement of cash flows", "#lv1",
      "한 기간 동안 현금및현금성자산이 어디서 들어오고 어디로 나갔는지 영업·투자·재무 세 활동으로 나눠 보여 주는 재무제표.", level=1),
    N("lab:concept/accrual-basis", "Concept", "발생주의", "accrual basis", "#why",
      "현금이 오간 날이 아니라 거래가 일어난 날에 수익과 비용을 인식하는 원칙. 이익과 현금이 달라지는 이유.", level=1),
    N("lab:concept/cash-equivalents", "Concept", "현금성자산", "cash equivalents", "#lv6",
      "큰 거래비용 없이 현금으로 바꿀 수 있고 가치 변동이 작으며, 취득 당시 만기가 3개월 이내인 금융상품.", ev=["F12"]),
    N("lab:concept/operating-activities", "Concept", "영업활동", "operating activities", "#lv1",
      "매출·매입·급여처럼 회사의 주된 수익 활동에서 생기는 현금흐름.", level=1),
    N("lab:concept/investing-activities", "Concept", "투자활동", "investing activities", "#lv1",
      "금융자산·유형자산·무형자산·대여금 같은 자산을 사고파는 데서 생기는 현금흐름.", level=1),
    N("lab:concept/financing-activities", "Concept", "재무활동", "financing activities", "#lv1",
      "차입·상환·유상증자·배당처럼 자금을 조달하고 돌려주는 데서 생기는 현금흐름. 외부 투자 유치는 여기에 들어간다.", level=1),
    N("lab:identity/cash-flow-identity", "Identity", "현금흐름표 등식", "cash flow identity", "#lv1",
      "기말 현금 − 기초 현금 = 영업 + 투자 + 재무 순현금흐름.", level=1, ev=["F01"]),
    N("lab:method/direct-method", "Method", "직접법", "direct method", "#lv2",
      "고객에게 받은 현금, 매입처·직원에게 준 현금처럼 항목별 실제 현금 유입·유출을 더해 영업활동 현금흐름을 구하는 방법.", ev=["F02"]),
    N("lab:method/indirect-method", "Method", "간접법", "indirect method", "#lv3",
      "당기순이익에서 출발해 현금이 오가지 않은 손익과 영업 관련 자산·부채 변동을 되돌려 영업활동 현금흐름을 구하는 방법.", ev=["F03"]),
    N("lab:concept/non-cash-expense", "Concept", "비현금비용", "non-cash expense", "#lv3",
      "감가상각비·퇴직급여 설정처럼 비용으로 잡혔지만 그 기간에 현금이 나가지 않은 항목. 간접법에서 다시 더한다."),
    N("lab:concept/working-capital-change", "Concept", "운전자본 변동", "change in working capital", "#lv3",
      "매출채권·재고·선급비용·미지급금·선수수익 같은 영업 관련 자산·부채의 증감. 자산 증가는 −, 부채 증가는 +."),
    N("lab:account/accounts-receivable", "Account", "매출채권", "accounts receivable", "#map",
      "외상으로 판매하고 아직 받지 못한 돈. 늘면 이익보다 현금이 덜 들어온 것.", family="statements"),
    N("lab:account/other-receivables", "Account", "미수금", "other receivables", "#map",
      "주된 영업 외의 거래나 정산 대기 등으로 받을 돈.", family="statements"),
    N("lab:account/accrued-payables", "Account", "미지급금", "other payables", "#map",
      "비용·구매 대금 중 아직 주지 않은 돈. 늘면 비용보다 현금이 덜 나간 것.", family="statements"),
    N("lab:account/deferred-revenue", "Account", "선수수익", "deferred revenue", "#map",
      "대가는 먼저 받았지만 아직 서비스를 제공하지 않아 부채로 남긴 금액.", family="statements"),
    N("lab:account/provision", "Account", "충당부채", "provision", "#map",
      "지출 시기·금액이 확정되지 않았지만 의무가 있어 추정해 인식한 부채. 현금을 따로 모아 둔 것이 아니다.", family="provisions"),
    N("lab:concept/equity-issuance", "Concept", "유상증자", "equity issuance", "#lv4",
      "투자자에게 새 주식을 발행하고 현금을 받는 것. 현금흐름표에서는 재무활동 유입.", family="equity"),
    N("lab:concept/fair-value-loss", "Concept", "공정가치 평가손실", "fair value loss", "#lv5",
      "전환사채·파생상품 등을 공정가치로 다시 재면서 생긴 손실. 순손실을 키우지만 현금은 나가지 않는다.",
      family="financial-instruments", conf="mid"),
    N("lab:metric/cfo-to-ni", "Metric", "영업현금흐름 ÷ 당기순이익", "CFO to net income", "#lv5",
      "이익의 질을 보는 비율. 손실 회사에서는 '순손실 중 실제 현금 손실의 비율'로 읽는다.", family="analysis"),
    N("lab:metric/cash-runway", "Metric", "현금 런웨이", "cash runway", "#lv4",
      "가진 현금성 자금이 지금의 영업현금 유출 속도로 몇 달 버티는지 보는 단순 지표.", family="analysis", conf="mid"),
    N("lab:metric/current-ratio", "Metric", "유동비율", "current ratio", "#lv4", "유동자산 ÷ 유동부채.", family="analysis"),
    N("lab:concept/lifecycle-pattern", "Concept", "현금흐름 생애주기 패턴", "cash flow life-cycle pattern", "#lv4",
      "영업·투자·재무 세 활동의 부호 조합으로 기업의 성장 단계를 짐작하는 틀(Dickinson 2011).", family="analysis",
      src=["Dickinson 2011"], domain=("acct", "biz")),
    N("lab:standard/kifrs-1007", "Standard", "K-IFRS 제1007호 현금흐름표", "K-IFRS 1007 Statement of Cash Flows", "#lv6",
      "한국채택국제회계기준의 현금흐름표 기준서.", family="disclosure", extra=STD),
    N("lab:standard/kr-gaap", "Standard", "일반기업회계기준", "Korean GAAP for non-public entities", "#lv6",
      "K-IFRS를 적용하지 않는 외부감사 대상 회사가 쓰는 기준. 사례 회사가 적용.", family="disclosure", extra=KRG, ev=["F11"]),
    N("lab:method/cashflow-prompt", "Method", "현금흐름표 작성 프롬프트", "cash flow prompt", "#lv7",
      "작성 원칙·검산 요구·출력 형식을 담아 생성AI에게 코드를 쓰게 하는 지시문.", family="systems", domain=("acct", "ai")),
    N("lab:method/assert-reconciliation", "Method", "assert 검산", "assertion-based reconciliation", "#lv9",
      "조건이 틀리면 코드가 멈추게 해 AI가 쓴 계산을 공시 숫자·항등식과 대조하는 방법.", family="systems", domain=("acct", "ai")),
    N("lab:limitation/direct-needs-detail", "Limitation", "직접법은 항목별 자료가 필요하다", "direct method needs detailed data", "#lv2",
      "공시에는 대부분 간접법만 있어 항목별 현금을 직접 알기 어렵다."),
    N("lab:limitation/indirect-hides-gross", "Limitation", "간접법은 총액 흐름을 숨긴다", "indirect method hides gross flows", "#lv3",
      "고객에게 얼마 받고 얼마 냈는지는 보이지 않고 차이만 보인다."),
    N("lab:limitation/bs-delta-mismatch", "Limitation", "재무상태표 증감 ≠ 공시 조정액", "balance deltas differ from disclosed adjustments", "#lv9",
      "계정 재분류·비현금 거래·투자 관련 미지급금 때문에 재무상태표 증감만으로는 공시 숫자가 나오지 않을 수 있다.", ev=["F09"]),
    N("lab:limitation/ai-plausible-errors", "Limitation", "AI 코드는 그럴듯하게 틀린다", "AI code can be plausibly wrong", "#lv8",
      "실행은 되지만 부호·분류·현금 범위가 틀린 코드가 나올 수 있다.", domain=("acct", "ai"), conf="mid"),
    N("lab:analogy/water-tank", "Analogy", "물탱크 (수위와 들어오는 물)", "water tank", "#why",
      "이익은 장부의 수위, 현금흐름은 관으로 실제 드나드는 물. 둘은 다르게 움직인다."),
    N("lab:claim/sg-cfo-270", "Claim", "SG화학 영업현금 270 (직접법 = 간접법)", "SG Chemical CFO 270", "#lv3",
      ev=["F01", "F02", "F03"], src=["10주차 교안"]),
    N("lab:claim/wrtn-2025", "Claim", "뤼튼 2025: 순손실 581억, 영업현금 −512억, 재무 +786억", "Wrtn 2025 cash flows", "#lv4",
      ev=["F04", "F05", "F06"], src=["뤼튼 감사보고서 2026-04-14"], extra=KRG),
    N("lab:claim/wrtn-revenue-growth", "Claim", "뤼튼 영업수익 30.7억 → 471.2억", "Wrtn revenue growth", "#lv4",
      ev=["F07"], src=["뤼튼 감사보고서 2026-04-14"]),
    N("lab:claim/anthropic-2025", "Claim", "Anthropic 2025: 순손실 약 420억 달러, 영업현금 약 −26억 달러", "Anthropic FY2025", "#lv5",
      conf="mid", ev=["F13"], src=["S-1 인용 제3자 분석"], domain=("acct", "ai")),
    N("lab:claim/openai-2025", "Claim", "OpenAI 2025: 매출 130.7억 달러, 영업손실 209.2억 달러", "OpenAI 2025", "#lv5",
      conf="mid", ev=["F14"], src=["보도(유출 재무제표, FT 검증)"], domain=("acct", "ai")),
    N("lab:question/payables-gap", "Question", "미지급금 조정액과 재무상태표 증감의 차이(약 0.8억)는 어디서 왔나?", "payables gap", "#lv9"),
    N("lab:question/fv-vs-cash", "Question", "순손실이 커도 현금 손실은 작을 수 있나?", "fair value vs cash loss", "#lv5"),
    N("lab:question/core", "Question", "손실이 581억인데 현금은 왜 186억 늘었나?", "core question", "#hero"),
    N("lab:sim/direct-sliders", "Simulation", "직접법 잔액 조절기", "direct method sliders", "#lv2"),
    N("lab:sim/indirect-stairs", "Simulation", "간접법 다섯 계단", "indirect stairs", "#lv3"),
    N("lab:sim/check-lab", "Simulation", "검산 실험실", "reconciliation lab", "#lv9", domain=("acct", "ai")),
]

E = []
def e(s, p, o, a, c="high"):
    E.append({"s": s, "p": "lab:" + p, "o": o, "anchor": a, "confidence": c})

e("lab:concept/accrual-basis", "prerequisiteOf", "lab:concept/cash-flow-statement", "#why")
for x in ["operating", "investing", "financing"]:
    e(f"lab:concept/{x}-activities", "partOf", "lab:concept/cash-flow-statement", "#lv1")
e("lab:identity/cash-flow-identity", "partOf", "lab:concept/cash-flow-statement", "#lv1")
e("lab:concept/cash-equivalents", "prerequisiteOf", "lab:identity/cash-flow-identity", "#lv6")
e("lab:concept/cash-flow-statement", "prerequisiteOf", "lab:method/direct-method", "#lv2")
e("lab:method/direct-method", "prerequisiteOf", "lab:method/indirect-method", "#lv3")
e("lab:method/direct-method", "hasLimitation", "lab:limitation/direct-needs-detail", "#lv2")
e("lab:limitation/direct-needs-detail", "addressedBy", "lab:method/indirect-method", "#lv3")
e("lab:method/indirect-method", "hasLimitation", "lab:limitation/indirect-hides-gross", "#lv3")
e("lab:limitation/indirect-hides-gross", "addressedBy", "lab:method/direct-method", "#lv8")
e("lab:method/direct-method", "contrastsWith", "lab:method/indirect-method", "#lv3")
e("lab:method/direct-method", "partOf", "lab:concept/operating-activities", "#lv2")
e("lab:method/indirect-method", "partOf", "lab:concept/operating-activities", "#lv3")
e("lab:concept/non-cash-expense", "partOf", "lab:method/indirect-method", "#lv3")
e("lab:concept/working-capital-change", "partOf", "lab:method/indirect-method", "#lv3")
for a in ["accounts-receivable", "other-receivables", "accrued-payables", "deferred-revenue"]:
    e(f"lab:account/{a}", "partOf", "lab:concept/working-capital-change", "#map")
e("lab:account/provision", "partOf", "lab:concept/non-cash-expense", "#lv4")
e("lab:concept/equity-issuance", "partOf", "lab:concept/financing-activities", "#lv4")
e("lab:concept/fair-value-loss", "partOf", "lab:concept/non-cash-expense", "#lv5", "mid")
e("lab:analogy/water-tank", "analogyOf", "lab:concept/accrual-basis", "#why")
e("lab:claim/sg-cfo-270", "supports", "lab:identity/cash-flow-identity", "#lv3")
e("lab:claim/sg-cfo-270", "supports", "lab:method/indirect-method", "#lv3")
e("lab:claim/wrtn-2025", "supports", "lab:concept/lifecycle-pattern", "#lv4")
e("lab:claim/wrtn-2025", "supports", "lab:concept/equity-issuance", "#lv4")
e("lab:claim/wrtn-revenue-growth", "supports", "lab:metric/cash-runway", "#lv4", "mid")
e("lab:claim/anthropic-2025", "supports", "lab:concept/fair-value-loss", "#lv5", "mid")
e("lab:claim/openai-2025", "supports", "lab:concept/fair-value-loss", "#lv5", "mid")
e("lab:metric/cfo-to-ni", "measuredBy", "lab:concept/operating-activities", "#lv5")
e("lab:concept/lifecycle-pattern", "evaluatedBy", "lab:metric/cfo-to-ni", "#lv5", "mid")
e("lab:metric/current-ratio", "relatedTo", "lab:metric/cash-runway", "#lv4")
e("lab:concept/cash-flow-statement", "governedBy", "lab:standard/kifrs-1007", "#lv6")
e("lab:concept/cash-flow-statement", "governedBy", "lab:standard/kr-gaap", "#lv6")
e("lab:standard/kifrs-1007", "contrastsWith", "lab:standard/kr-gaap", "#lv6")
e("lab:standard/kifrs-1007", "prerequisiteOf", "lab:method/cashflow-prompt", "#lv7")
e("lab:method/cashflow-prompt", "prerequisiteOf", "lab:method/assert-reconciliation", "#lv9")
e("lab:method/cashflow-prompt", "hasLimitation", "lab:limitation/ai-plausible-errors", "#lv8")
e("lab:limitation/ai-plausible-errors", "addressedBy", "lab:method/assert-reconciliation", "#lv9")
e("lab:method/assert-reconciliation", "hasLimitation", "lab:limitation/bs-delta-mismatch", "#lv9")
e("lab:limitation/bs-delta-mismatch", "raises", "lab:question/payables-gap", "#lv9")
e("lab:concept/fair-value-loss", "raises", "lab:question/fv-vs-cash", "#lv5")
e("lab:question/core", "relatedTo", "lab:claim/wrtn-2025", "#hero")
e("lab:method/direct-method", "demonstratedBy", "lab:sim/direct-sliders", "#lv2")
e("lab:method/indirect-method", "demonstratedBy", "lab:sim/indirect-stairs", "#lv3")
e("lab:method/assert-reconciliation", "demonstratedBy", "lab:sim/check-lab", "#lv9")
e("lab:concept/cash-equivalents", "relatedTo", "lab:concept/investing-activities", "#lv6")

KG = {"version": "1.0", "page": PAGE, "nodes": nodes, "edges": E}

def jsonld(kg, meta):
    ctx = {"skos": "http://www.w3.org/2004/02/skos/core#", "schema": "https://schema.org/",
           "dct": "http://purl.org/dc/terms/", "prov": "http://www.w3.org/ns/prov#", "lab": "urn:lab:"}
    g = [{"@id": "urn:lab:page/" + PAGE, "@type": "schema:LearningResource", "schema:name": meta["title"],
          "schema:inLanguage": "ko", "schema:dateCreated": meta["date"]}]
    for n in kg["nodes"]:
        t = {"Claim": "schema:Claim", "Standard": "schema:Legislation", "Question": "schema:Question"}.get(n["type"], "skos:Concept")
        o = {"@id": n["id"], "@type": [t, "lab:" + n["type"]],
             "skos:prefLabel": [{"@value": n["label"]["ko"], "@language": "ko"}, {"@value": n["label"]["en"], "@language": "en"}]}
        if "definition" in n:
            o["skos:definition"] = {"@value": n["definition"]["ko"], "@language": "ko"}
        g.append(o)
    for x in kg["edges"]:
        g.append({"@id": x["s"], x["p"]: {"@id": x["o"]}})
    return {"@context": ctx, "@graph": g}

def r(id, typ, title, year, auth, cont="", url="", role="primary", supports=(), locs=(), ver=None, note="", acc=(2026, 11, 6), pub=""):
    d = {"id": id, "type": typ, "title": title, "issued": {"date-parts": [[year]]}}
    if auth: d["author"] = auth
    if cont: d["container-title"] = cont
    if pub: d["publisher"] = pub
    if url: d["URL"] = url; d["accessed"] = {"date-parts": [list(acc)]}
    d["lab"] = {"work": "lab:work/" + id, "role": role, "supports": list(supports), "locs": list(locs),
                "verified": ver or {"title": True, "authors": True, "year": True, "doi": False}, "note": note}
    return d

REFS = [
    r("wrtn2026audit", "report", "주식회사 뤼튼테크놀로지스 재무제표에 대한 감사보고서 (제5기, 2025.1.1~2025.12.31)", 2026,
      [{"literal": "대주회계법인"}], "전자공시시스템 DART", "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260414000008",
      role="data", supports=["lab:claim/wrtn-2025", "lab:claim/wrtn-revenue-growth"],
      locs=[{"claim": "lab:claim/wrtn-2025", "loc": "재무상태표·손익계산서·현금흐름표 5~10쪽, 주석 17"}],
      note="공시일 2026-04-14, 일반기업회계기준. 전기(2024) 재무제표는 감사받지 않음"),
    r("w10lecture", "report", "현금흐름표와 재무분석 (10주차 강의 교안)", 2026, [], "회계·재무분석 강의",
      role="primary", supports=["lab:claim/sg-cfo-270"], locs=[{"claim": "lab:claim/sg-cfo-270", "loc": "3.3~3.9절 예제"}],
      ver={"title": True, "authors": False, "year": True, "doi": False}, note="(주)SG화학·서울(주) 예제"),
    r("kifrs1007", "legislation", "기업회계기준서 제1007호 '현금흐름표'", 2026, [{"literal": "한국회계기준원"}],
      "한국채택국제회계기준", role="background", supports=["lab:standard/kifrs-1007"],
      ver={"title": True, "authors": True, "year": False, "doi": False}, note="문단 번호는 쓰지 않음. 현행 조문은 회계기준원에서 확인"),
    r("krgaap", "legislation", "일반기업회계기준 (재무제표의 작성과 표시)", 2026, [{"literal": "한국회계기준원"}],
      role="background", supports=["lab:standard/kr-gaap"], ver={"title": True, "authors": True, "year": False, "doi": False},
      note="사례 회사 적용 기준. 장·문단 번호 미기재"),
    r("dickinson2011", "article-journal", "Cash flow patterns as a proxy for firm life cycle", 2011,
      [{"family": "Dickinson", "given": "Victoria"}], "The Accounting Review", role="background",
      supports=["lab:concept/lifecycle-pattern"], ver={"title": True, "authors": True, "year": True, "doi": False}),
    r("secapi2026anthropic", "webpage", "Anthropic (ANT) S-1 IPO SEC Filing Analysis", 2026, [{"literal": "sec-api.io"}],
      "", "https://sec-api.io/insights/anthropic-ant-s-1-ipo-sec-filing-analysis", role="data",
      supports=["lab:claim/anthropic-2025"], note="2026-10-26 제출로 보도된 S-1의 수치를 인용한 제3자 분석. SEC 원문 미확인"),
    r("cestrian2026anthropic", "webpage", "Anthropic (ANT) S-1: $81bn Loss vs $3.9bn Cash Flow", 2026,
      [{"literal": "Cestrian Capital Research"}], "", "https://www.cestriancapitalresearch.com/anthropic-ant-s1-81bn-loss-3-9bn-operating-cash-flow/",
      role="data", supports=["lab:claim/anthropic-2025"], note="교차 확인용 제3자 분석"),
    r("anthropic2026seriesg", "webpage", "Anthropic raises $30 billion in Series G funding at $380 billion post-money valuation", 2026,
      [{"literal": "Anthropic"}], "", "https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation",
      role="data", supports=["lab:claim/anthropic-2025"], note="2026-02-12 회사 발표"),
    r("cleantechnica2026openai", "webpage", "OpenAI Went From $5.09 Billion Net Loss in 2024 to $38.53 Billion Net Loss in 2025", 2026,
      [{"family": "Shahan", "given": "Zachary"}], "CleanTechnica",
      "https://cleantechnica.com/2026/06/30/openai-went-from-5-09-billion-net-loss-in-2024-to-38-53-billion-net-loss-in-2025/",
      role="data", supports=["lab:claim/openai-2025"], note="유출된 감사 재무제표를 FT가 검증했다고 보도. 회사 공식 공시 아님"),
    r("yahoo2026openai", "webpage", "OpenAI's $34 Billion Burn: Losses Grew 8x Ahead of IPO", 2026, [{"family": "Landes", "given": "Al"}],
      "Yahoo Finance", "https://finance.yahoo.com/markets/stocks/articles/openai-34-billion-burn-losses-162759402.html",
      role="data", supports=["lab:claim/openai-2025"], note="비현금 공정가치 조정 415.5억 달러 언급"),
    r("bloomberg2025openai", "webpage", "OpenAI Finalizes $40 Billion Funding at $300 Billion Value", 2025, [{"literal": "Bloomberg"}],
      "Bloomberg", "https://www.bloomberg.com/news/articles/2025-03-31/openai-finalizes-40-billion-funding-at-300-billion-valuation",
      role="data", supports=["lab:claim/openai-2025"], note="2025-03-31 보도"),
]

META = {
    "title": "현금흐름표 연구실 — 직접법·간접법에서 생성AI 검산까지",
    "series": "회계·재무분석 연구실", "number": "10-1",
    "creator": [{"name": "안상선 ((주)M-Robo 대표)", "role": "author"}],
    "contributor": [{"name": "AI 보조 제작", "role": "assistant"}],
    "date": "2026-11-06", "version": "1.0", "language": ["ko"], "license": "", "url": "https://adminmrobo.github.io/cashflow-lab/",
    "domain": ["acct", "ai"],
    "about": ["lab:method/direct-method", "lab:method/indirect-method", "lab:claim/wrtn-2025",
              "lab:method/cashflow-prompt", "lab:method/assert-reconciliation"],
    "educationalLevel": "입문~중급", "learningResourceType": "interactive explainer",
    "basedOn": ["w10lecture", "wrtn2026audit"],
    "suggestedCitation": "안상선 (2026). 현금흐름표 연구실 — 직접법·간접법에서 생성AI 검산까지. 회계·재무분석 연구실 10-1, v1.0. https://adminmrobo.github.io/cashflow-lab/",
}

if __name__ == "__main__":
    ids = {n["id"] for n in nodes}
    bad = [x for x in E if x["s"] not in ids or x["o"] not in ids]
    deg = {i: 0 for i in ids}
    for x in E: deg[x["s"]] += 1; deg[x["o"]] += 1
    print(len(nodes), "nodes", len(E), "edges", "broken", bad, "isolated", [k for k, v in deg.items() if v == 0])
    print("relatedTo share", sum(x["p"] == "lab:relatedTo" for x in E) / len(E))
