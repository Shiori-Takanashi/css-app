#!/usr/bin/env python3
from pathlib import Path
from bs4 import BeautifulSoup

# パス設定
TEMPLATE = Path("templates/index.template.html")
OUTPUT   = Path("index.html")

# ルート直下の .html を列挙し、index.html とテンプレートは外す
html_files = sorted(
    [p for p in Path(".").glob("*.html")
     if p.name not in (OUTPUT.name, TEMPLATE.name)]
)

# <h1>を抜いてリンクリストを作成
items = []
for p in html_files:
    soup = BeautifulSoup(p.read_text(encoding="utf-8"), "html.parser")
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else p.stem
    items.append(f'<li class="list-group-item"><a href="{p.name}">{title}</a></li>')

# テンプレートに埋め込んで出力
template = TEMPLATE.read_text(encoding="utf-8")
body     = "\n    ".join(items)
output   = template.replace("{{article_links}}", body)
OUTPUT.write_text(output, encoding="utf-8")
