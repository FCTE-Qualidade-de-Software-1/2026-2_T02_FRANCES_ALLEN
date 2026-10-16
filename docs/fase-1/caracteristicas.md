# Seleção e priorização das características

As características são escolhidas no [modelo de qualidade](modelo-de-qualidade.md) da ISO/IEC 25010:2023, considerando o [propósito da avaliação](proposito.md) e as [partes interessadas](partes-interessadas.md).

## 1. Análise das características candidatas

| Característica (ISO/IEC 25010) | Relevância para o VICKY | Viabilidade de medição externa | Prioridade |
|-------------------------------|-------------------------|--------------------------------|:----------:|
| Adequação funcional | _a busca retorna artigos pertinentes e completos?_ | _-_ | _-_ |
| Eficiência de desempenho | _tempo de carregamento e de resposta da busca_ | _-_ | _-_ |
| Compatibilidade | _funcionamento em diferentes navegadores_ | _-_ | _-_ |
| Usabilidade / capacidade de interação | _facilidade de busca e navegação para o estudante_ | _-_ | _-_ |
| Confiabilidade | _disponibilidade do site_ | _-_ | _-_ |
| Segurança | _proteção dos dados de conta, se houver_ | _-_ | _-_ |
| Manutenibilidade | _viável pela análise do código-fonte liberado pela equipe do VICKY_ | _-_ | _-_ |
| Portabilidade / flexibilidade | _adaptação a mobile e desktop_ | _-_ | _-_ |

_Critério de priorização sugerido: impacto para o usuário-alvo x viabilidade de coleta com os recursos da equipe._

## 2. Características selecionadas

A equipe selecionou **três** características de qualidade do produto:

| # | Característica | Subcaracterísticas candidatas (ISO/IEC 25010:2023) | Justificativa (produto + objetivo da avaliação) |
|---|----------------|----------------------------------------------------|-------------------------------------------------|
| C1 | **Adequação funcional** | Completude funcional, correção funcional, aptidão funcional | _a definir_ |
| C2 | **Capacidade de interação** | Reconhecibilidade de adequação, capacidade de aprendizado, operabilidade, proteção contra erro do usuário, engajamento do usuário, inclusividade, assistência ao usuário, autodescritividade | _a definir_ |
| C3 | **Manutenibilidade** | Modularidade, reusabilidade, analisabilidade, modificabilidade, testabilidade | _a definir_ |

_Definir quais subcaracterísticas serão o foco de cada objetivo GQM e justificar a escolha._

!!! info "Acesso ao código-fonte"
    A equipe que desenvolveu o VICKY, e que continua ativa no projeto, liberou o acesso ao produto. Com isso, o grupo tem **todo o código-fonte** disponível para análise. Esse acesso torna viável avaliar a **manutenibilidade** por análise estática e inspeção do código, além das características observáveis no uso do produto.

Cada característica selecionada dá origem a um objetivo GQM na [Fase 2](../fase-2/objetivos-questoes-hipoteses.md#rastreabilidade-com-a-fase-1).

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 05/10/2026 | Registro das características selecionadas | Gabriel Fae | - |
| 0.3 | 05/10/2026 | Registro do acesso ao código-fonte | Gabriel Fae | - |
| 0.4 | 16/10/2026 | Propósito, escopo, norma e rastreabilidade movidos para páginas próprias | Gabriel Fae | - |
