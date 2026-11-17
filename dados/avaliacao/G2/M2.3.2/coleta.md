# Registro da coleta: M2.3.2

Preenchido por A1 antes da primeira captura e atualizado se algo mudar. Método: [G2 por inspeção](../../../../docs/fase-3/metodo-g2-inspecao.md).

| Item | Valor |
|------|-------|
| Avaliadores | A1 e A2 (A3 se houver divergência sem consenso) |
| Início (data e hora) | |
| Fim (data e hora) | |
| Navegador | Google Chrome, versão: |
| Área visível | 1366 x 768 pixels, zoom de 100% (modo responsivo do DevTools) |
| Produto | VICKY em produção, <https://vicky.synaptha.com/> |
| Versão em produção | Data e hora de acesso; versão dos Termos exibida no site: ; versão exibida no menu lateral: |
| Código de referência (só A1) | Fork `LucasAvelar2711/Vicky`, commit `c2ae570` (29/09/2026) |

## Arquivos

- `modelo.csv`: cabeçalho e itens da métrica. Cada avaliador copia para `A1.csv` ou `A2.csv` e preenche sozinho.
- `inventario.csv`: mensagens levantadas no código por A1 (etapa 1), só com o texto. Na coluna `texto`, `//` separa linhas da mesma caixa, `{...}` marca parte variável e `[...]` descreve botão ou trecho omitido.
- `evidencias/`: capturas no formato `AAAAMMDD_A1_<item>.png` ou `AAAAMMDD_A2_<item>.png`.

## Decisões antes da coleta (17/11/2026)

- **Mensagem que não aparece em produção:** fica de lado por enquanto. Na planilha, `origem = nao_exibida` e as colunas de classificação ficam vazias. Se ela entra ou não no denominador será decidido antes da consolidação (etapa 7), com a mesma regra para todos os itens.

## Valores da coluna `origem`

| Valor | Quando usar |
|-------|-------------|
| `producao` | A mensagem foi vista na tela, mostrada pelo VICKY |
| `navegador` | Quem respondeu foi a validação do próprio Chrome |
| `inventario` | Não dá para disparar sem gastar crédito; classificada pelo texto do inventário |
| `nao_exibida` | O gatilho foi provocado, mas nenhuma mensagem apareceu |
| `nao_coletado` | Não foi possível observar por causa externa (site fora do ar, triagem indisponível) |

## Ocorrências

Mudanças em produção, itens `nao_coletado`, diferenças entre produção e código e interpretações de critério adotadas na consolidação.

-

## Concordância bruta (etapa 7)

- Itens com o mesmo resultado em A1 e A2: de
