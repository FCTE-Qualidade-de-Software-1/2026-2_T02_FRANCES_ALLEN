# PICO e critérios gerados pelo VICKY para T1 (sem edição)

Projeto #53 na conta de cortesia. Texto copiado da tela do projeto (seção Critérios) e do endpoint `/projetos/53/search-strings.json`, em 17/11/2026, antes de iniciar a triagem.

Observação: a tela não mostra os quatro componentes P, I, C e O rotulados; o VICKY gera um protocolo de triagem (escopo, piso metodológico, Quality Score) e strings de busca. É isso que está registrado abaixo.

## Strings de busca

### pubmed (6 strings)

1. `(colchicine AND cardiovascular events AND secondary prevention AND (randomized controlled trial OR RCT)) AND (2007[Date - Publication] : 2026[Date - Publication])`
2. `(colchicine AND cardiovascular disease AND (placebo OR usual care) AND (randomized controlled trial OR RCT)) AND (2007[Date - Publication] : 2026[Date - Publication])`
3. `("colchicine"[MeSH] OR colchicina) AND ("cardiovascular events"[MeSH] OR eventos cardiovasculares) AND ("secondary prevention"[MeSH] OR prevenção secundária) AND (2007[Date - Publication] : 2026[Date - Publication])`
4. `(colchicine OR colchicina) AND ("cardiovascular" OR "heart disease") AND ("secondary prevention" OR "prevenção secundária") AND (2007[Date - Publication] : 2026[Date - Publication])`
5. `(colchicine AND cardiovascular events AND secondary prevention AND adult) AND (2007[Date - Publication] : 2026[Date - Publication])`
6. `(colchicine AND (RCT OR randomized controlled trial OR clinical trial)) AND (2007[Date - Publication] : 2026[Date - Publication])`

### scielo (6 strings)

1. `(colchicina AND eventos cardiovasculares AND prevenção secundária)`
2. `(colchicina AND doença cardiovascular AND (placebo OR cuidado usual))`
3. `(colchicina OR colchicine) AND (eventos cardiovasculares OR cardiovascular events)`
4. `(colchicina AND prevenção secundária AND adultos)`
5. `(colchicina AND ensaio clínico randomizado)`
6. `(colchicina AND (RCT OR ensaio clínico controlado randomizado))`

### scholar (6 strings)

1. `colchicine cardiovascular events secondary prevention`
2. `colchicine placebo usual care cardiovascular disease`
3. `colchicine AND cardiovascular AND secondary prevention`
4. `colchicine AND cardiovascular events AND RCT`
5. `colchicine AND heart disease AND secondary prevention`
6. `colchicine AND clinical trials cardiovascular`

## Critérios (texto integral gerado)

# Protocolo de Triagem (Revisão Sistemática Padrão) — Colchicina na prevenção secundária de eventos cardiovasculares em adultos com doença aterosclerótica

## Maturidade do tema
moderate — A literatura sobre o uso da colchicina na prevenção secundária de eventos cardiovasculares está em desenvolvimento, com alguns ensaios clínicos randomizados, mas a heterogeneidade e a necessidade de mais validação externa indicam uma maturidade moderada.

## Janela temporal recomendada
2007–2026 (20 anos, proporcional à maturidade)

## 1. Elegibilidade de Escopo (obrigatória — exclui se falha) ✅

### 1.1 Tema central
- O artigo aborda diretamente o uso da colchicina na prevenção secundária de eventos cardiovasculares em adultos com doença aterosclerótica.

### 1.2 Tipo de publicação
- Estudo primário ou secundário com dados (RCT, coorte, caso-controle, transversal, qualitativo, revisão sistemática, meta-análise, guideline, consenso). Exclui editoriais puros, cartas ao editor, comentários sem dados, abstracts de congresso isolados.

### 1.3 Idioma
- Inglês, português ou espanhol.

### 1.4 Disponibilidade
- Texto completo OU abstract estruturado disponível.

### 1.5 Janela temporal
- Publicação entre 2007 e 2026. Estudos clássicos/fundacionais anteriores podem entrar se forem altamente citados ou conceitualmente indispensáveis.

## 2. Piso Metodológico Mínimo (obrigatório, mas amplo) ✅

### 2.1 Metodologia descrita
- O método é descrito (qualquer desenho aceito). NÃO exige RCT, validação externa ou multi-centro.

### 2.2 Amostra coerente com desenho
- O N é coerente com o tipo de estudo (sem cap fixo). Estudos pequenos com desenho justificado entram.

### 2.3 Métrica/desfecho relevante
- Pelo menos UM desfecho ou métrica relacionada ao tema é reportado.

### 2.4 Coerência interna
- Há coerência entre objetivo, método, resultados e conclusão.

## 3. Quality Score (0–100, NÃO exclui)

### 3.1 Universal (50 pts — aplicável a qualquer tema)
| Atributo | Peso |
|---|---|
| Clareza da pergunta científica / definição da população | 10 |
| Adequação do desenho ao objetivo | 15 |
| Controle de viés, confundidores, análise estatística adequada | 15 |
| Atualidade e relevância prática | 10 |

### 3.2 Específico do tema (50 pts — pesos adaptados à maturidade moderate)
| Atributo específico | Peso |
|---|---|
| Comparação com placebo ou cuidado usual (RCT) | 15 |
| Validação externa (se disponível) | 12 |
| Desfechos cardiovasculares primários reportados | 10 |
| Tamanho da amostra e justificação do N | 8 |
| Tempo de seguimento dos participantes | 5 |
| Tipo de estudo prospectivo (se aplicável) | 5 |

### Interpretação do score
- **80–100**: prioridade máxima de leitura.
- **60–79**: alta prioridade.
- **40–59**: incluído mas leitura secundária.
- **0–39**: incluído (passou Stage 1+2) mas baixa prioridade — só lido se tiver tempo.

## 4. Ranking Top N
- Os artigos incluídos são ordenados por quality_score DESC.
- Top N (definido pela meta do usuário) recebem prioridade.
- Os demais incluídos continuam acessíveis na lista completa — em revisão sistemática REAL todos os elegíveis devem ser considerados.
