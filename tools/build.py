"""tools/template.html + 데이터 → ../index.html"""
import html, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import kg_data as K
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(H)
rd = lambda p: open(os.path.join(R, p), encoding="utf8").read()
js = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
prompt = rd("code/prompt_cashflow.md")
prompt = prompt.split("```text\n", 1)[1].split("```", 1)[0].rstrip()
t = open(os.path.join(H, "template.html"), encoding="utf8").read()
rep = {
    "__PROMPT__": html.escape(prompt, quote=False),
    "__WRTN_CODE__": html.escape(rd("code/wrtn_cashflow.py"), quote=False),
    "__SG_CODE__": html.escape(rd("code/sg_chemical.py"), quote=False),
    "__SG_OUT__": html.escape(rd("docs/sg_output.txt"), quote=False),
    "__WRTN_OUT__": rd("docs/wrtn_output.txt").replace("</", "<\\/"),
    "__KG_RAW__": js(K.KG), "__KG_LD__": js(K.jsonld(K.KG, K.META)),
    "__REFS__": js(K.REFS), "__META__": js(K.META),
    "__SPRITES__": rd("assets/sprites_page.js"),
}
for k, v in rep.items():
    assert k in t, k
    t = t.replace(k, v)
open(os.path.join(R, "index.html"), "w", encoding="utf8").write(t)
print("index.html", len(t.encode()) // 1024, "KB")
