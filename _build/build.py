"""Builds index.html from index.template.html and menu.py.  Run: python3 _build/build.py"""
import html
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from menu import MENU  # noqa: E402

DIET_LABEL = {"vg": "Vegan", "v": "Veggie", "vgo": "Vegan option"}


def esc(s):
    return html.escape(s, quote=True)


def price(p):
    return " / ".join("£" + part.strip() for part in p.split("/"))


tabs, sections = [], []
for i, sec in enumerate(MENU):
    tabs.append(f'          <a href="#m-{sec["id"]}"{" aria-current=\"true\"" if i == 0 else ""}>{esc(sec["en"])}</a>')
    rows = []
    for item in sec["items"]:
        en, zh, p, diet = item[:4]
        desc = item[4] if len(item) > 4 else ""
        badge = f' <span class="diet diet-{diet}">{DIET_LABEL[diet]}</span>' if diet else ""
        rows.append(
            f'              <li class="dish" data-diet="{diet}">\n'
            f'                <div class="dish-name"><span class="en">{esc(en)}</span>{badge}'
            f'<span class="zh" lang="zh-Hant">{esc(zh)}</span></div>\n'
            f'                <span class="dish-price">{price(p)}</span>\n'
            + (f'                <p class="dish-desc">{esc(desc)}</p>\n' if desc else "")
            + "              </li>"
        )
    note = f'\n            <p class="menu-sec-note">{esc(sec["note"])}</p>' if sec["note"] else ""
    sections.append(
        f'          <section class="menu-sec" id="m-{sec["id"]}" aria-labelledby="m-{sec["id"]}-h">\n'
        f'            <h3 id="m-{sec["id"]}-h">{esc(sec["en"])} <span class="zh" lang="zh-Hant">{esc(sec["zh"])}</span></h3>{note}\n'
        f'            <ul class="dishes">\n' + "\n".join(rows) + "\n            </ul>\n          </section>"
    )

tpl = (HERE / "index.template.html").read_text(encoding="utf-8")
out = tpl.replace("{{MENU_TABS}}", "\n".join(tabs)).replace("{{MENU_SECTIONS}}", "\n".join(sections))
(HERE.parent / "index.html").write_text(out, encoding="utf-8")
print("index.html written")
