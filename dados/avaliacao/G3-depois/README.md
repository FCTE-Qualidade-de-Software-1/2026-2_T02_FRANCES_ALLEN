# G3 depois da ação de melhoria

Coleta do G3 repetida no commit da melhoria (`7e9ccd8`, branch `melhoria/g3-pipeline-logging` do fork `LucasAvelar2711/Vicky`, PR #1), com os mesmos scripts e lockfiles de `dados/avaliacao/G3/`. A linha de base (`c2ae570`) continua intacta em `dados/avaliacao/G3/`.

Comando: `COMMIT=7e9ccd81a49693d4f811ae074200de4884f4afe8 dados/avaliacao/G3-depois/coletar.sh <clone do fork>` (23/11/2026).

| Métrica | Antes (`c2ae570`) | Depois (`7e9ccd8`) |
|---|---|---|
| M3.1.1 Acoplamento | 2,05 (Excelente) | 2,05 (Excelente) |
| M3.1.2 Complexidade adequada | 76,6% (36/47, Aceitável) | 85,5% (59/69, Bom) |
| M3.2.1 PEP 8 | 5,3% (Insatisfatório) | 5,3% (Insatisfatório) |
| M3.2.2 Duplicação | 0,15% (Excelente) | 0,15% (Excelente) |
| M3.2.3 Logs | 0,0% (0/33, Insatisfatório) | 100,0% (43/43, Excelente) |
| M3.3.1 Cobertura | 63,17% (Aceitável) | 65,22% (Aceitável) |

A ficha de inspeção de M3.2.3 (`M3.2.3/inspecao.md`) foi gerada para as 43 funções críticas do commit novo e ainda não tem a ratificação de A1 e A2.
