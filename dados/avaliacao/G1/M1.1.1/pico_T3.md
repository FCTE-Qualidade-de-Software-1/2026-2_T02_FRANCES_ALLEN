# PICO e critérios gerados pelo VICKY para T3 (sem edição)

Projeto #55 na conta de cortesia. Texto copiado da tela do projeto (seção Critérios) e do endpoint `/projetos/55/search-strings.json`, em 2026-11-18 (BRT), antes de iniciar a triagem. A tela não mostra P, I, C e O rotulados.

## Strings de busca (campo string_text, sem edição)

### pubmed

1. `("Gestational Diabetes Mellitus"[Mesh] OR "diabetes mellitus gestacional" OR "diabetes gestacional") AND ("Brazil" OR "Brasil") AND ("2007"[Date - Publication] : "2026"[Date - Publication])`
2. `("Gestational Diabetes" OR "diabetes gestacional") AND ("prevalence" OR "prevalência") AND ("Brazil" OR "Brasil") AND ("2007"[Date - Publication] : "2026"[Date - Publication])`
3. `("Gestational Diabetes Mellitus"[Mesh] OR "diabetes mellitus gestacional") AND ("observational study" OR "estudo observacional") AND ("Brazil" OR "Brasil") AND ("2007"[Date - Publication] : "2026"[Date - Publication])`
4. `("Gestational Diabetes" OR "diabetes gestacional") AND ("epidemiology" OR "epidemiologia") AND ("Brazil" OR "Brasil") AND ("2007"[Date - Publication] : "2026"[Date - Publication])`
5. `("Gestational Diabetes Mellitus"[Mesh] OR "diabetes mellitus gestacional") AND ("risk factors" OR "fatores de risco") AND ("Brazil" OR "Brasil") AND ("2007"[Date - Publication] : "2026"[Date - Publication])`
6. `("diabetes gestacional" AND "Brazil") AND ("cohort study" OR "estudo de coorte") AND ("2007"[Date - Publication] : "2026"[Date - Publication])`

### scholar

1. `"gestational diabetes mellitus prevalence Brazil"`
2. `"diabetes gestacional Brasil"`
3. `"prevalência diabetes gestacional Brasil"`
4. `"gestational diabetes observational study Brazil"`
5. `"diabetes gestacional fatores de risco Brasil"`
6. `"diabetes gestacional estudo de coorte Brasil"`

### scielo

1. `("diabetes mellitus gestacional" OR "gestational diabetes") AND ("Brasil" OR "Brazil") AND (2007 TO 2026)`
2. `("prevalência" OR "prevalence") AND ("diabetes gestacional") AND ("Brasil" OR "Brazil") AND (2007 TO 2026)`
3. `("estudo observacional" OR "observational study") AND ("diabetes gestacional") AND ("Brasil" OR "Brazil") AND (2007 TO 2026)`
4. `("epidemiologia" OR "epidemiology") AND ("diabetes gestacional") AND ("Brasil" OR "Brazil") AND (2007 TO 2026)`
5. `("fatores de risco" OR "risk factors") AND ("diabetes gestacional") AND ("Brasil" OR "Brazil") AND (2007 TO 2026)`
6. `("diabetes gestacional" AND "estudo de coorte") AND ("Brasil" OR "Brazil") AND (2007 TO 2026)`

## Critérios (texto integral gerado)

# Protocolo de Triagem (Revisão Sistemática Padrão) — Prevalência de diabetes mellitus gestacional no Brasil

## Maturidade do tema
moderate — A literatura sobre diabetes mellitus gestacional no Brasil é ativa, mas apresenta uma mistura de estudos observacionais e dados heterogêneos, com validação externa não sendo a regra.

## Janela temporal recomendada
2007–2026 (20 anos, proporcional à maturidade)

## 1. Elegibilidade de Escopo (obrigatória — exclui se falha) ✅

### 1.1 Tema central
- O artigo aborda diretamente a prevalência de diabetes mellitus gestacional em gestantes brasileiras ou subtemas claramente relacionados.

### 1.2 Tipo de publicação
- Estudo primário ou secundário com dados (coorte, caso-controle, transversal, qualitativo, revisão sistemática, meta-análise). Exclui editoriais puros, cartas ao editor, comentários sem dados, abstracts de congresso isolados.

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
| Validação externa (se presente) | 10 |
| Comparação com baseline/padrão | 10 |
| Tamanho da amostra (N adequado) | 10 |
| Desenho do estudo (observacional, coorte, etc.) | 10 |
| Desfechos primários de diabetes mellitus gestacional | 10 |
| Contexto geográfico (estudos focados no Brasil) | 10 |

### Interpretação do score
- **80–100**: prioridade máxima de leitura.
- **60–79**: alta prioridade.
- **40–59**: incluído mas leitura secundária.
- **0–39**: incluído (passou Stage 1+2) mas baixa prioridade — só lido se tiver tempo.

## 4. Ranking Top N
- Os artigos incluídos são ordenados por quality_score DESC.
- Top N (definido pela meta do usuário) recebem prioridade.
- Os demais incluídos continuam acessíveis na lista completa — em revisão sistemática REAL todos os elegíveis devem ser considerados.
