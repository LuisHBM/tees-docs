import sys
from datetime import timedelta
from pathlib import Path

import matplotlib.pyplot as plt
import yaml


def gerar_burndown(yaml_path: Path):
    with open(yaml_path) as f:
        dados = yaml.safe_load(f)

    inicio = dados["inicio"]
    fim = dados["fim"]
    tarefas = dados["tarefas"]

    total_dias = (fim - inicio).days
    total_pontos = sum(t["pontos"] for t in tarefas)

    dias = [inicio + timedelta(days=i) for i in range(total_dias + 1)]

    concluido_por_dia = {d: 0 for d in dias}
    for t in tarefas:
        concluido_em = t["concluido_em"]
        if concluido_em in concluido_por_dia:
            concluido_por_dia[concluido_em] += t["pontos"]

    real = []
    restante = total_pontos
    for d in dias:
        restante -= concluido_por_dia[d]
        real.append(restante)

    ideal = [
        round(total_pontos - total_pontos * i / total_dias, 1)
        for i in range(total_dias + 1)
    ]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dias, ideal, linestyle="--", color="gray", label="Ideal")
    ax.plot(dias, real, marker="o", color="#185FA5", label="Real")
    ax.set_title(f"Burndown — Sprint {dados['sprint']}: {dados['titulo']}")
    ax.set_xlabel("Data")
    ax.set_ylabel("Pontos restantes")
    ax.set_ylim(0, total_pontos + 2)
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    fig.autofmt_xdate()

    saida = yaml_path.parent / "burndown.png"
    fig.savefig(saida, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Gerado: {saida}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arquivos = [Path(a) for a in sys.argv[1:]]
    else:
        raiz = Path(__file__).parent
        arquivos = sorted(raiz.glob("*/burndown.yaml"))

    for arq in arquivos:
        gerar_burndown(arq)
