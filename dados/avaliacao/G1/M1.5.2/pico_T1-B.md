# PICO e critérios gerados pelo VICKY para T1-B (sem edição)

Projeto #81 na conta de cortesia. Mesma entrada de T1 (tema, objetivo, revisão sistemática, 20 anos, PubMed, SciELO e Google Acadêmico, Top 30, sem filtro de acesso aberto). Texto copiado da tela do projeto (seção Critérios) e do endpoint `/projetos/81/search-strings.json`, em 2026-11-19, antes de iniciar a triagem.

## Strings de busca

### pubmed (6 strings)

1. `(colchicine AND cardiovascular events AND secondary prevention AND atherosclerotic disease) AND (2007[Date - Publication] : 2026[Date - Publication])`
2. `(colchicine AND (placebo OR usual care) AND (myocardial infarction OR stroke OR cardiovascular death)) AND (2007[Date - Publication] : 2026[Date - Publication])`
3. `("colchicine"[MeSH] OR "colchicina" OR "colchicine therapy") AND ("cardiovascular events" OR "cardiovascular diseases") AND (2007[Date - Publication] : 2026[Date - Publication])`
4. `("colchicine" OR "colchicina") AND ("secondary prevention" OR "preventive treatment") AND (2007[Date - Publication] : 2026[Date - Publication])`
5. `(colchicine AND atherosclerosis AND (adult OR elderly)) AND (2007[Date - Publication] : 2026[Date - Publication])`
6. `("colchicine" AND "randomized controlled trial") AND (2007[Date - Publication] : 2026[Date - Publication])`

### scholar (6 strings)

1. `colchicine cardiovascular events secondary prevention atherosclerotic disease`
2. `colchicine placebo usual care myocardial infarction stroke cardiovascular death`
3. `colchicine therapy cardiovascular events`
4. `colchicine secondary prevention`
5. `colchicine atherosclerosis adult elderly`
6. `colchicine randomized controlled trial`

### scielo (6 strings)

1. `(colchicina AND eventos cardiovasculares AND prevenção secundária AND doença aterosclerótica)`
2. `(colchicina AND (placebo OR cuidado usual) AND (infarto OR AVC OR morte cardiovascular))`
3. `(colchicina OR "colchicine") AND ("eventos cardiovasculares" OR "doenças cardiovasculares")`
4. `(colchicina AND "prevenção secundária")`
5. `(colchicina AND aterosclerose AND (adulto OR idoso))`
6. `(colchicina AND "ensaio clínico randomizado")`

## Critérios (texto integral gerado)

# Protocolo de Triagem (Revisão Sistemática Padrão) — Colchicina na prevenção secundária de eventos cardiovasculares em adultos com doença aterosclerótica

## Maturidade do tema
moderate — A literatura sobre colchicina na prevenção secundária de eventos cardiovasculares é ativa, mas apresenta uma mistura de ensaios clínicos randomizados (RCTs) e estudos observacionais, com validação externa não sendo a regra.

## Janela temporal recomendada
2007–2026 (20 anos, proporcional à maturidade)

## 1. Elegibilidade de Escopo (obrigatória — exclui se falha) ✅

### 1.1 Tema central
- O artigo aborda diretamente o efeito da colchicina na prevenção secundária de eventos cardiovasculares em adultos com doença aterosclerótica.

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
| Validação externa (comparação com outros estudos) | 12 |
| Comparação com baseline/padrão (cuidado usual) | 12 |
| Métricas primárias de desfecho (infarto, AVC, morte cardiovascular) | 12 |
| Tipo de estudo prospectivo/RCT | 12 |
| Amostra adequada e justificada | 10 |
| Relevância prática e impacto clínico | 10 |

### Interpretação do score
- **80–100**: prioridade máxima de leitura.
- **60–79**: alta prioridade.
- **40–59**: incluído mas leitura secundária.
- **0–39**: incluído (passou Stage 1+2) mas baixa prioridade — só lido se tiver tempo.

## 4. Ranking Top N
- Os artigos incluídos são ordenados por quality_score DESC.
- Top N (definido pela meta do usuário) recebem prioridade.
- Os demais incluídos continuam acessíveis na lista completa — em revisão sistemática REAL todos os elegíveis devem ser considerados.
