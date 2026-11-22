# PICO e critérios gerados pelo VICKY para E1 (sem edição)

Projeto #56 na conta de cortesia. Configuração: texto de T1; objetivo de T1 com o acréscimo "Incluir somente ensaios clínicos randomizados."; só PubMed; últimos 5 anos (2022 a 2026); Top 30; sem filtro de texto gratuito. O formulário não tem campo de tipo de estudo; a restrição foi no objetivo. Texto copiado da tela do projeto e de `/projetos/56/search-strings.json`, em 2026-11-18 (BRT), antes de iniciar a triagem.

## Strings de busca (campo string_text, sem edição)

### pubmed

1. `(colchicine AND cardiovascular events AND secondary prevention AND (randomized controlled trial)) AND ("2022"[Date - Publication] : "2026"[Date - Publication])`
2. `(colchicine AND (myocardial infarction OR stroke OR cardiovascular death) AND (randomized controlled trial)) AND ("2022"[Date - Publication] : "2026"[Date - Publication])`
3. `("colchicine"[MeSH] OR colchicina) AND ("cardiovascular diseases"[MeSH] OR doença aterosclerótica) AND ("2022"[Date - Publication] : "2026"[Date - Publication])`
4. `(colchicine OR colchicina) AND (cardiovascular events OR eventos cardiovasculares) AND (secondary prevention OR prevenção secundária) AND (2022:2026)`
5. `(colchicine AND cardiovascular outcomes AND (RCT OR randomized controlled trial)) AND ("2022"[Date - Publication] : "2026"[Date - Publication])`
6. `(colchicine AND (placebo OR usual care) AND (cardiovascular events OR eventos cardiovasculares)) AND ("2022"[Date - Publication] : "2026"[Date - Publication])`

### scholar

1. `colchicine cardiovascular events secondary prevention randomized controlled trial`
2. `colchicine myocardial infarction stroke cardiovascular death randomized controlled trial`
3. `colchicine cardiovascular diseases`
4. `colchicine cardiovascular outcomes RCT`
5. `colchicine placebo usual care cardiovascular events`
6. `colchicine secondary prevention cardiovascular events`

### scielo

1. `(colchicina AND eventos cardiovasculares AND prevenção secundária AND ensaio clínico randomizado)`
2. `(colchicina AND (infarto ou AVC ou morte cardiovascular) AND ensaio clínico randomizado)`
3. `(colchicina ou colchicine) AND (doenças cardiovasculares) AND (2022:2026)`
4. `(colchicina AND eventos cardiovasculares AND prevenção secundária)`
5. `(colchicina AND desfechos cardiovasculares AND ensaio clínico randomizado)`
6. `(colchicina AND (placebo ou cuidado usual) AND eventos cardiovasculares)`

## Critérios (texto integral gerado)

# Protocolo de Triagem (Revisão Sistemática Padrão) — Colchicina na prevenção secundária de eventos cardiovasculares em adultos com doença aterosclerótica

## Maturidade do tema
moderate — A literatura sobre o uso da colchicina na prevenção secundária de eventos cardiovasculares é ativa, mas apresenta uma mistura de estudos, incluindo ensaios clínicos randomizados e coortes observacionais, com validação externa não sendo a regra.

## Janela temporal recomendada
2022–2026 (5 anos, proporcional à maturidade)

## 1. Elegibilidade de Escopo (obrigatória — exclui se falha) ✅

### 1.1 Tema central
- O artigo aborda diretamente o efeito da colchicina na prevenção secundária de eventos cardiovasculares em adultos com doença aterosclerótica.

### 1.2 Tipo de publicação
- Estudo primário com dados (ensaios clínicos randomizados). Exclui editoriais puros, cartas ao editor, comentários sem dados, abstracts de congresso isolados.

### 1.3 Idioma
- Inglês, português ou espanhol.

### 1.4 Disponibilidade
- Texto completo OU abstract estruturado disponível.

### 1.5 Janela temporal
- Publicação entre 2022 e 2026. Estudos clássicos/fundacionais anteriores podem entrar se forem altamente citados ou conceitualmente indispensáveis.

## 2. Piso Metodológico Mínimo (obrigatório, mas amplo) ✅

### 2.1 Metodologia descrita
- O método é descrito (qualquer desenho aceito). NÃO exige validação externa ou multi-centro.

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
| Validação externa (se disponível) | 10 |
| Comparação com placebo ou cuidado usual | 15 |
| Desfechos primários de eventos cardiovasculares (infarto, AVC, morte cardiovascular) | 15 |
| Tipo de estudo: ensaio clínico randomizado | 10 |
| Tamanho da amostra e justificativa do N | 10 |

### Interpretação do score
- **80–100**: prioridade máxima de leitura.
- **60–79**: alta prioridade.
- **40–59**: incluído mas leitura secundária.
- **0–39**: incluído (passou Stage 1+2) mas baixa prioridade — só lido se tiver tempo.

## 4. Ranking Top N
- Os artigos incluídos são ordenados por quality_score DESC.
- Top N (definido pela meta do usuário) recebem prioridade.
- Os demais incluídos continuam acessíveis na lista completa — em revisão sistemática REAL todos os elegíveis devem ser considerados.
