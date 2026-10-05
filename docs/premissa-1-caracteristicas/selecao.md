# Seleção e justificativa das características

## 1. Norma de referência

Modelo de qualidade do produto da **ISO/IEC 25010:2023** (família SQuaRE - ISO/IEC 25000). A terminologia segue a edição de 2023, em que "usabilidade" passou a se chamar **capacidade de interação**.

## 2. Propósito da avaliação

_Descrever por que a avaliação está sendo feita, para quem e qual decisão ela apoia. Exemplo de redação:_

> Avaliar em que medida o VICKY atende às necessidades de estudantes de medicina na busca e consulta de artigos científicos, para fornecer aos mantenedores evidências que orientem a priorização de melhorias.

| Item | Definição |
|------|-----------|
| Requisitante | _a definir_ |
| Perspectiva da avaliação | Externa (produto em uso) e interna (análise do código-fonte), com acesso liberado pela equipe de desenvolvimento do VICKY |
| Escopo | _funcionalidades e plataformas avaliadas_ |
| Fora do escopo | _ex.: infraestrutura de hospedagem, correção do conteúdo médico_ |

## 3. Análise das características candidatas

| Característica (ISO/IEC 25010) | Relevância para o VICKY | Viabilidade de medição externa | Prioridade |
|-------------------------------|-------------------------|--------------------------------|:----------:|
| Adequação funcional | _a busca retorna artigos pertinentes e completos?_ | _-_ | _-_ |
| Eficiência de desempenho | _tempo de carregamento e de resposta da busca_ | _-_ | _-_ |
| Compatibilidade | _funcionamento em diferentes navegadores_ | _-_ | _-_ |
| Usabilidade / capacidade de interação | _facilidade de busca e navegação para o estudante_ | _-_ | _-_ |
| Confiabilidade | _disponibilidade do site_ | _-_ | _-_ |
| Segurança | _proteção dos dados de conta, se houver_ | _-_ | _-_ |
| Manutenibilidade | _exige acesso ao código; provavelmente fora do escopo_ | _-_ | _-_ |
| Portabilidade / flexibilidade | _adaptação a mobile e desktop_ | _-_ | _-_ |

_Critério de priorização sugerido: impacto para o usuário-alvo x viabilidade de coleta com os recursos da equipe._

## 4. Características selecionadas

A equipe selecionou **três** características de qualidade do produto:

| # | Característica | Subcaracterísticas candidatas (ISO/IEC 25010:2023) | Justificativa (produto + objetivo da avaliação) |
|---|----------------|----------------------------------------------------|-------------------------------------------------|
| C1 | **Adequação funcional** | Completude funcional, correção funcional, aptidão funcional | _a definir_ |
| C2 | **Capacidade de interação** | Reconhecibilidade de adequação, capacidade de aprendizado, operabilidade, proteção contra erro do usuário, engajamento do usuário, inclusividade, assistência ao usuário, autodescritividade | _a definir_ |
| C3 | **Manutenibilidade** | Modularidade, reusabilidade, analisabilidade, modificabilidade, testabilidade | _a definir_ |

_Definir quais subcaracterísticas serão o foco de cada objetivo GQM e justificar a escolha._

!!! info "Acesso ao código-fonte"
    A equipe que desenvolveu o VICKY, e que continua ativa no projeto, liberou o acesso ao produto. Com isso, o grupo tem **todo o código-fonte** disponível para análise. Esse acesso torna viável avaliar a **manutenibilidade** por análise estática e inspeção do código, além das características observáveis no uso do produto.

## 5. Rastreabilidade para a Fase 2

| Característica | Parte interessada | Objetivo GQM |
|----------------|-------------------|--------------|
| C1 - Adequação funcional | _-_ | [G1](../premissa-2-metricas/objetivos-questoes-hipoteses.md#g1) |
| C2 - Capacidade de interação | _-_ | [G2](../premissa-2-metricas/objetivos-questoes-hipoteses.md#g2) |
| C3 - Manutenibilidade | _-_ | [G3](../premissa-2-metricas/objetivos-questoes-hipoteses.md#g3) |

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 05/10/2026 | Registro das características selecionadas | Gabriel Fae | - |
| 0.3 | 05/10/2026 | Registro do acesso ao código-fonte | Gabriel Fae | - |
