# PICO e critérios gerados pelo VICKY para T4 (sem edição)

Projeto #57 na conta de cortesia. Texto copiado da tela do projeto (seção Critérios) e do endpoint `/projetos/57/search-strings.json`, em 2026-11-19 (BRT), antes de iniciar a triagem. A tela não mostra P, I, C e O rotulados.

## Strings de busca (campo string_text, sem edição)

### pubmed

1. `("Friedreich's Ataxia"[Mesh] OR "Friedreich ataxia" OR "ataxia de Friedreich") AND ("omaveloxolone" OR "idebenone") AND ("placebo" OR "randomized controlled trial") AND ("ataxia scales" OR "neurological progression") AND ("2007"[Date - Publication] : "2026"[Date - Publication])`
2. `("Friedreich's Ataxia"[Mesh] OR "Friedreich ataxia") AND ("omaveloxolone" OR "idebenone") AND ("ataxia scales") AND ("2007"[Date - Publication] : "2026"[Date - Publication])`
3. `("Friedreich's Ataxia"[Mesh] OR "Friedreich ataxia") AND ("treatment" OR "therapy") AND ("randomized controlled trial") AND ("2007"[Date - Publication] : "2026"[Date - Publication])`
4. `("Friedreich's Ataxia"[Mesh] OR "Friedreich ataxia") AND ("clinical trial" OR "RCT") AND ("neurological outcome") AND ("2007"[Date - Publication] : "2026"[Date - Publication])`
5. `("Friedreich's Ataxia"[Mesh] OR "Friedreich ataxia") AND ("drug therapy" OR "pharmacological treatment") AND ("ataxia scales") AND ("2007"[Date - Publication] : "2026"[Date - Publication])`
6. `("Friedreich's Ataxia"[Mesh] OR "Friedreich ataxia") AND ("omaveloxolone" OR "idebenone") AND ("clinical outcomes") AND ("2007"[Date - Publication] : "2026"[Date - Publication])`

### scholar

1. `"Friedreich's Ataxia" AND "omaveloxolone" AND "placebo"`
2. `"Friedreich ataxia" AND "idebenone" AND "ataxia scales"`
3. `"Friedreich's Ataxia treatment" AND "randomized controlled trial"`
4. `"Friedreich ataxia" AND "clinical trial" AND "neurological progression"`
5. `"Friedreich ataxia" AND "drug therapy" AND "ataxia scales"`
6. `"Friedreich's Ataxia" AND "clinical outcomes" AND "2007..2026"`

### scielo

1. `("ataxia de Friedreich" OR "Friedreich ataxia") AND ("omaveloxolone" OR "idebenona") AND ("placebo" OR "ensaio clínico randomizado")`
2. `("ataxia de Friedreich") AND ("escala de ataxia") AND ("tratamento farmacológico")`
3. `("ataxia de Friedreich") AND ("idebenona" OR "omaveloxolone") AND ("resultado clínico")`
4. `("ataxia de Friedreich") AND ("ensaio clínico") AND ("tratamento")`
5. `("ataxia de Friedreich") AND ("fármacos") AND ("escala de ataxia")`
6. `("ataxia de Friedreich") AND ("tratamento farmacológico") AND ("2007".."2026")`

## Critérios (texto integral gerado)

# Protocolo de Triagem (Revisão Sistemática Padrão) — Tratamento farmacológico da ataxia de Friedreich

## Maturidade do tema
emerging — A literatura sobre o tratamento farmacológico da ataxia de Friedreich é ainda em desenvolvimento, com predominância de estudos preliminares e poucos ensaios clínicos randomizados robustos.

## Janela temporal recomendada
2007–2026 (20 anos, proporcional à maturidade)

## 1. Elegibilidade de Escopo (obrigatória — exclui se falha) ✅

### 1.1 Tema central
- O artigo aborda diretamente o tratamento farmacológico da ataxia de Friedreich ou subtemas claramente relacionados, como o uso de omaveloxolona e idebenona.

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

### 3.2 Específico do tema (50 pts — pesos adaptados à maturidade emerging)
| Atributo específico | Peso |
|---|---|
| Metodologia clara e bem descrita | 15 |
| Comparação com placebo | 10 |
| Uso de escalas de ataxia como desfecho | 10 |
| Número de participantes (N) e justificação do tamanho da amostra | 10 |
| Validação externa (quando aplicável) | 5 |
| Relevância prática dos resultados | 5 |

### Interpretação do score
- **80–100**: prioridade máxima de leitura.
- **60–79**: alta prioridade.
- **40–59**: incluído mas leitura secundária.
- **0–39**: incluído (passou Stage 1+2) mas baixa prioridade — só lido se tiver tempo.

## 4. Ranking Top N
- Os artigos incluídos são ordenados por quality_score DESC.
- Top N (definido pela meta do usuário) recebem prioridade.
- Os demais incluídos continuam acessíveis na lista completa — em revisão sistemática REAL todos os elegíveis devem ser considerados.
