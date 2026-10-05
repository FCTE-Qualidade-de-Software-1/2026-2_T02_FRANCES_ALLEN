# Avaliação de Qualidade do VICKY

Este site documenta a **avaliação da qualidade do produto de software VICKY**, conduzida pelo grupo **Frances Allen** (turma T02) na disciplina **FGA0315 - Qualidade de Software 1** (FCTE/UnB, 2026.2), sob orientação da Profa. Cristiane Ramos.

O **VICKY** é um website destinado a **estudantes de medicina**, voltado à busca e consulta de informações sobre artigos científicos e conteúdos acadêmicos da área da saúde. Detalhes em [Objeto de avaliação](projeto/objeto-de-avaliacao.md).

## Como a avaliação está organizada

A avaliação segue o processo de avaliação de produto da família **SQuaRE** (ISO/IEC 25040) e se apoia em três premissas obrigatórias, cada uma documentada em uma seção deste site:

| Premissa | O que define | Fase do processo |
|----------|--------------|------------------|
| [Premissa 1 - Características de qualidade](premissa-1-caracteristicas/index.md) | Adequação funcional, capacidade de interação e manutenibilidade (ISO/IEC 25010:2023) e sua justificativa | Fase 1 - Estabelecer os requisitos da avaliação |
| [Premissa 2 - Métricas (GQM)](premissa-2-metricas/index.md) | Objetivos, questões, hipóteses, métricas e critérios de julgamento | Fase 2 - Especificar a avaliação |
| [Premissa 3 - Gestão do projeto (PSM/CID)](premissa-3-gestao/index.md) | Indicadores de acompanhamento do próprio projeto e decisões de gestão | Transversal a todas as fases |

```mermaid
flowchart LR
    F1["Fase 1<br/>Requisitos da avaliação<br/>(Premissa 1)"] --> F2["Fase 2<br/>Especificação<br/>(Premissa 2)"]
    F2 --> F3["Fase 3<br/>Projeto da avaliação"]
    F3 --> F4["Fase 4<br/>Execução e conclusão"]
    G["Gestão do projeto - PSM/CID<br/>(Premissa 3)"] -.-> F1
    G -.-> F2
    G -.-> F3
    G -.-> F4
```

## Entregas

| Entrega | Data | Conteúdo | Release |
|---------|------|----------|---------|
| Entrega 1 | 26/10/2026 | Fases 1 e 2, 1ª versão do artigo, tabela de contribuição | _a publicar_ |
| Entrega 2 | _conforme cronograma da disciplina_ | Fases 3 e 4, ação de melhoria, 2ª versão do artigo | _a publicar_ |

## Links

- Repositório: [FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN)
- Releases: [página de releases](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/releases)
- Quadro de tarefas: _link do GitHub Projects_
- Equipe: [Integrantes e papéis](projeto/equipe.md)

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
