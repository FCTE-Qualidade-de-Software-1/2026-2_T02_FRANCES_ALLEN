# PICO e critérios gerados pelo VICKY para T2 (sem edição)

Projeto #54 na conta de cortesia. Texto copiado da tela do projeto (seção Critérios) e do endpoint `/projetos/54/search-strings.json`, em 2026-11-17 (BRT), antes de iniciar a triagem. A tela não mostra P, I, C e O rotulados.

Observação: em PubMed, as posições 0 a 2 do endpoint trazem a string `(yoga AND cancer AND fatigue) AND (2007` quebrada em fragmentos (`(yoga AND cancer AND fatigue) AND (`, `[Date - Publication] :`, `[Date - Publication])`); as demais strings PubMed terminam em `AND (` sem o intervalo de datas. Registrado como veio.

## Strings de busca (campo string_text, sem edição)

### pubmed

1. `(yoga AND cancer AND fatigue) AND (`
2. `[Date - Publication] :`
3. `[Date - Publication])`
4. `(yoga AND fatigue AND cancer patients) AND (`
5. `(yoga[MeSH Terms] OR yoga) AND (fatigue[MeSH Terms] OR fatigue) AND (cancer[MeSH Terms] OR neoplasms) AND (`
6. `(cancer AND fatigue AND yoga) OR (cancer AND fatigue AND exercise) AND (`
7. `(yoga OR yoga therapy) AND (cancer OR neoplasms) AND (fatigue OR tiredness) AND (`
8. `(randomized controlled trial AND yoga AND cancer AND fatigue) AND (`

### scholar

1. `yoga cancer fatigue`
2. `yoga and fatigue in cancer patients`
3. `yoga therapy cancer fatigue`
4. `randomized controlled trial yoga cancer fatigue`
5. `cancer fatigue exercise yoga`
6. `yoga interventions for fatigue in cancer patients`

### scielo

1. `(yoga OR ioga) AND (câncer OR neoplasias) AND (fadiga OR cansaço)`
2. `(yoga AND fadiga AND pacientes com câncer)`
3. `(ioga AND fadiga AND câncer)`
4. `(yoga AND câncer AND fadiga) OR (yoga AND câncer AND exercício)`
5. `(yoga OR terapia de yoga) AND (câncer OR neoplasias) AND (fadiga OR cansaço)`
6. `(ensaio clínico randomizado AND yoga AND câncer AND fadiga)`

## Critérios (texto integral gerado)

# Protocolo de Triagem (Revisão Sistemática Padrão) — Ioga para fadiga em pessoas com câncer

## Maturidade do tema
moderate — A literatura sobre ioga para fadiga em pessoas com câncer é ativa, mas apresenta uma mistura de ensaios clínicos randomizados (RCTs) pequenos e estudos observacionais. A validação externa não é a regra, mas há um número crescente de estudos relevantes nos últimos anos.

## Janela temporal recomendada
2007–2026 (20 anos, proporcional à maturidade)

## 1. Elegibilidade de Escopo (obrigatória — exclui se falha) ✅

### 1.1 Tema central
- O artigo aborda diretamente o efeito da ioga sobre a fadiga relacionada ao câncer em adultos durante ou após o tratamento.

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
| Validação externa (se disponível) | 10 |
| Comparação com grupo controle (nenhuma intervenção, lista de espera, cuidado usual) | 15 |
| Desfechos primários relacionados à fadiga | 15 |
| Tipo de estudo prospectivo/RCT | 10 |
| Amplitude da amostra e justificativa do N | 10 |

### Interpretação do score
- **80–100**: prioridade máxima de leitura.
- **60–79**: alta prioridade.
- **40–59**: incluído mas leitura secundária.
- **0–39**: incluído (passou Stage 1+2) mas baixa prioridade — só lido se tiver tempo.

## 4. Ranking Top N
- Os artigos incluídos são ordenados por quality_score DESC.
- Top N (definido pela meta do usuário) recebem prioridade.
- Os demais incluídos continuam acessíveis na lista completa — em revisão sistemática REAL todos os elegíveis devem ser considerados.
