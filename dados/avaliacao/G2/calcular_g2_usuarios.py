#!/usr/bin/env python3
"""Cálculo de M2.7.2 e M2.5.1 (G2 com usuários) a partir dos CSVs das pastas.

Método: docs/fase-3/metodo-g2-usuarios.md (seção 6, com a exceção da D14 para M2.5.1, seção 2.10).
Fórmulas e níveis: docs/fase-2/especificacao-das-metricas.md e docs/fase-2/niveis-e-julgamento.md.

Só usa a biblioteca padrão do Python (3.9 ou superior). Não escreve nada: imprime as tabelas que vão para
`M2.7.2/consolidado.md` e `M2.5.1/consolidado.md`, para conferência.

Uso, a partir da raiz do repositório:

    python3 dados/avaliacao/G2/calcular_g2_usuarios.py

M2.7.2: o elemento é entendido pelo participante quando `uso = sem_ajuda` (observacao-uso.csv) e
`classificacao_final = correta` (respostas-compreensao.csv); entra em A quando entendido pela maioria dos
participantes válidos (2 de 3, ou 3 de 5). Quality Score (E10) fora da maioria leva a Insatisfatório.

M2.5.1: a tela é agradável para o respondente com nota 4 ou 5; entra em A quando agradável para a maioria dos
respondentes válidos (3 de 5 pela Fase 2; 2 de 3 pela D14, com só três respostas).
"""

from __future__ import annotations

import csv
import os
from statistics import median

PASTA = os.path.dirname(os.path.abspath(__file__))
NIVEIS_M272 = [(0.90, "Excelente"), (0.75, "Bom"), (0.60, "Aceitável"), (0.0, "Insatisfatório")]
NIVEIS_M251 = [(0.80, "Excelente"), (0.60, "Bom"), (0.40, "Aceitável"), (0.0, "Insatisfatório")]


def ler(caminho):
    with open(os.path.join(PASTA, caminho), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def nivel(x, faixas):
    return next(n for limite, n in faixas if x >= limite)


def maioria(n):
    return n // 2 + 1


def m272():
    validos = [s["participante"] for s in ler("M2.7.2/sessoes.csv") if s["situacao"] == "valida"]
    if len(validos) == 4:
        validos = validos[:3]  # seção 6: com quatro, usam-se as três primeiras
    if len(validos) < 3:
        print("M2.7.2: menos de três sessões válidas; não calcular (seção 7.4)")
        return
    uso = {(u["participante"], u["elemento"]): u["uso"] for u in ler("M2.7.2/observacao-uso.csv")}
    comp = {(r["participante"], r["elemento"]): r["classificacao_final"]
            for r in ler("M2.7.2/respostas-compreensao.csv")}
    elementos = [f"E{i:02d}" for i in range(1, 13)]
    corte = maioria(len(validos))
    print(f"M2.7.2: participantes válidos {', '.join(validos)}; maioria = {corte} de {len(validos)}")
    print("| elemento | " + " | ".join(validos) + " | entendido_por | na_maioria |")
    a = 0
    qs_ok = False
    for e in elementos:
        linha = []
        for p in validos:
            ok = uso.get((p, e)) == "sem_ajuda" and comp.get((p, e)) == "correta"
            linha.append(1 if ok else 0)
        soma = sum(linha)
        dentro = soma >= corte
        a += dentro
        if e == "E10":
            qs_ok = dentro
        print(f"| {e} | " + " | ".join(map(str, linha)) + f" | {soma} | {'sim' if dentro else 'não'} |")
    b = len(elementos)
    x = a / b
    n = "Insatisfatório" if not qs_ok else nivel(x, NIVEIS_M272)
    print(f"A = {a}, B = {b}, X = {x:.1%}, Quality Score na maioria: {'sim' if qs_ok else 'não'}, nível = {n}")


def m251():
    linhas = ler("M2.5.1/respostas.csv")
    resp = sorted({r["participante"] for r in linhas})
    telas = ["inicial", "novo_projeto", "detalhe_projeto", "lista_artigos", "ficha_artigo"]
    nota = {(r["participante"], r["tela"]): int(r["nota"]) for r in linhas}
    corte = maioria(len(resp))
    print(f"\nM2.5.1: respondentes {', '.join(resp)}; maioria = {corte} de {len(resp)}")
    print("| tela | " + " | ".join(resp) + " | agradavel_para | na_maioria |")
    a = 0
    for t in telas:
        ns = [nota.get((r, t), 0) for r in resp]  # nota faltando conta como não agradável (seção 7.2)
        soma = sum(1 for n in ns if n >= 4)
        a += soma >= corte
        print(f"| {t} | " + " | ".join(map(str, ns)) + f" | {soma} | {'sim' if soma >= corte else 'não'} |")
    x = a / len(telas)
    print(f"A = {a}, B = {len(telas)}, X = {x:.1%}, nível = {nivel(x, NIVEIS_M251)}")
    unanime = sum(1 for t in telas if all(nota.get((r, t), 0) >= 4 for r in resp))
    print(f"Sensibilidade: exigindo todos os {len(resp)} respondentes, A = {unanime}, X = {unanime / len(telas):.1%}")
    por_resp = {r: sum(1 for t in telas if nota.get((r, t), 0) >= 4) for r in resp}
    print("Telas agradáveis por respondente (H2.5):", por_resp)

    quali = ler("M2.5.1/qualitativo.csv")
    print("\n| afirmacao | notas | mediana | concordam (4 ou 5) |")
    for i in range(1, 11):
        q = f"Q{i:02d}"
        ns = [int(r["nota"]) for r in quali if r["afirmacao"] == q]
        print(f"| {q} | {', '.join(map(str, ns))} | {median(ns):g} | {sum(n >= 4 for n in ns)} de {len(ns)} |")


if __name__ == "__main__":
    m272()
    m251()
