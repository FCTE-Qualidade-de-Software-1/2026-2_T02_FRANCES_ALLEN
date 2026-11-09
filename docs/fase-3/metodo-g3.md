# Método do G3 (manutenibilidade)

!!! note "Rascunho em aberto: Guilherme Moura (#23)"
    Só está registrado aqui o que a [Fase 2](../fase-2/especificacao-das-metricas.md) já define. Os itens abertos ficam para o responsável decidir e escrever.

## 1. Métricas cobertas

| Métrica | Medida | Ferramenta ou comando citado na Fase 2 | Pasta em `dados/avaliacao/G3/` |
|---------|--------|----------------------------------------|--------------------------------|
| [M3.1.1](../fase-2/especificacao-das-metricas.md#m311) | MMo-1-G | Análise de imports | `M3.1.1/` |
| [M3.1.2](../fase-2/especificacao-das-metricas.md#m312) | MMo-2-S | `radon cc src/vicky/pipeline.py -s -a` | `M3.1.2/` |
| [M3.2.1](../fase-2/especificacao-das-metricas.md#m321) | MRe-2-S | `flake8 src/vicky/ --count --statistics` | `M3.2.1/` |
| [M3.2.2](../fase-2/especificacao-das-metricas.md#m322) | MRe-1-G | `pylint --disable=all --enable=duplicate-code src/vicky/` e `radon raw` | `M3.2.2/` |
| [M3.2.3](../fase-2/especificacao-das-metricas.md#m323) | MAn-1-G | Inspeção de código | `M3.2.3/` |
| [M3.3.1](../fase-2/especificacao-das-metricas.md#m331) | MTe-1-G | `pytest --cov=src/vicky/ tests/` | `M3.3.1/` |

## 2. Preparação

- [ ] Qual repositório e qual commit serão avaliados? (as hipóteses do G2 citam o fork no commit `c2ae570`)
- [ ] Quais versões de radon, flake8, pylint e pytest-cov serão usadas?
- [ ] O que é preciso para instalar o projeto e rodar a suíte de testes?
- [ ] Rever as medidas de analisabilidade (hoje MRe-2-S e MRe-1-G), como pede a #23
- [ ] Trocar os seis links de busca do Google nas fichas do G3
- [ ] Fechar as faixas de nível com buraco

## 3. Passo a passo

- [ ] Como contar os imports internos de M3.1.1 de forma que todos cheguem ao mesmo número?
- [ ] Em M3.1.2, quais blocos da saída do `radon` entram na contagem?
- [ ] Em M3.2.1, como obter o número de arquivos com violação?
- [ ] Em M3.2.2, como somar as linhas duplicadas e qual total de linhas usar?
- [ ] Em M3.2.3, quais são as funções críticas de `pipeline.py`?

## 4. Registro

- [ ] Criar a pasta `dados/avaliacao/G3/`, com um README como os do G1 e do G2
- [ ] O que cada pasta recebe além da saída bruta da ferramenta?

## 5. Cálculo

As fórmulas estão nas [fichas da Fase 2](../fase-2/especificacao-das-metricas.md), e os níveis em [níveis de pontuação](../fase-2/niveis-e-julgamento.md).

## 6. Discordância e repetição

- [ ] Quem repete os comandos para confirmar o mesmo número?
- [ ] Como tratar testes que falham ou são pulados em M3.3.1?
- [ ] Como resolver divergências na inspeção de M3.2.3?

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 04/11/2026 | Criação da página | Lucas Avelar | - |
| 0.2 | 09/11/2026 | Esqueleto com o que a Fase 2 define e os pontos em aberto para o responsável | Gabriel Fae | - |
