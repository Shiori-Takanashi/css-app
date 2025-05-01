from pathlib import Path
from bs4 import BeautifulSoup

template_path = Path("templates/index.template.html")
output_path = Path("index.html")
articles = sorted(Path(".").glob("article*.html"))

def extract_h1(file_path):
    soup = BeautifulSoup(file_path.read_text(encoding="utf-8"), "html.parser")
    h1 = soup.find("h1")
    return h1.text.strip() if h1 else file_path.name

items = []
for html in articles:
    title = extract_h1(html)
    items.append(f'<li class="list-group-item"><a href="{html.name}">{title}</a></li>')

template = template_path.read_text(encoding="utf-8")
output = template.replace("{{article_links}}", "\n    ".join(items))
output_path.write_text(output, encoding="utf-8")
