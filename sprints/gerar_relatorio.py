import re
import subprocess
import sys
import tempfile
from pathlib import Path

raiz = Path(__file__).parent.parent


def resolver_includes(conteudo: str) -> str:
    def substituir(match):
        nome = match.group(1)
        arquivo = raiz / f"{nome}.md"
        if not arquivo.exists():
            print(f"Aviso: arquivo não encontrado para include '{nome}'")
            return ""
        return arquivo.read_text().strip()

    return re.sub(r"<!-- include:(\S+) -->", substituir, conteudo)


def gerar(numero: int):
    pasta = raiz / "sprints" / str(numero)
    sprint_md = pasta / f"sprint_0{numero}.md"

    if not sprint_md.exists():
        print(f"Arquivo não encontrado: {sprint_md}")
        sys.exit(1)

    conteudo = resolver_includes(sprint_md.read_text())

    with tempfile.NamedTemporaryFile(suffix=".md", mode="w", delete=False, dir=pasta) as tmp:
        tmp.write(conteudo)
        tmp_path = Path(tmp.name)

    saida_html = pasta / f"relatorio_sprint_{numero}.html"
    saida_pdf = pasta / f"relatorio_sprint_{numero}.pdf"
    css = Path(__file__).parent / "relatorio.css"

    try:
        subprocess.run([
            "pandoc",
            str(tmp_path),
            "--resource-path", f"{raiz}:{pasta}",
            "-o", str(saida_html),
            "--self-contained",
            f"--css={css}",
            "--metadata", f"title=LicitAI — Relatório Sprint {numero}",
        ], check=True)

        print(f"HTML gerado: {saida_html}")

        subprocess.run([
            "google-chrome",
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={saida_pdf}",
            str(saida_html),
        ], check=True)

        print(f"PDF gerado: {saida_pdf}")
    finally:
        tmp_path.unlink(missing_ok=True)


if __name__ == "__main__":
    numero = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    gerar(numero)
