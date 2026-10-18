# Seleção e priorização das características

As características são escolhidas no [modelo de qualidade](modelo-de-qualidade.md) da ISO/IEC 25010:2023, considerando o [propósito da avaliação](proposito.md) e as [partes interessadas](partes-interessadas.md).

## 1. Análise das características candidatas

A equipe utilizou o método MoSCoW adaptado com pesos para priorizar as características. Os critérios avaliados foram:

- Impacto (Peso 3): Relevância direta para o usuário-alvo (estudantes de medicina) ou para o negócio. Escala de 1 (Baixo) a 3 (Alto).
- Viabilidade (Peso 2): Facilidade de coleta de métricas considerando os recursos da equipe (acesso ao código e ao público-alvo). Escala de 1 (Baixa) a 3 (Alta).

A pontuação final determina a categoria: Must Have (13 a 15 pontos), Should Have (10 a 12 pontos), Could Have (7 a 9 pontos) e Won't Have (< 7 pontos ou cortado por restrição técnica).

| Característica (ISO/IEC 25010) | Impacto (x3) | Viabilidade (x2) | Pontuação Final | Categoria MoSCoW | Justificativa |
|-------------------------------|:---:|:---:|:---:|:---|---|
| Adequação funcional | 3 | 3 | 15 | Must Have | Fundamental para o estudante confiar no Top N. Altamente viável devido ao acesso a estudantes para testes. |
| Capacidade de interação | 3 | 3 | 15 | Must Have | Crítica para a formulação correta dos critérios PICO. Viável através de questionários com usuários reais. |
| Manutenibilidade | 2 | 3 | 12 | Should Have | Impacta a evolução pela equipe de desenvolvimento. Altamente viável pelo acesso total ao código e ferramentas de análise estática. |
| Compatibilidade | 2 | 2 | 10 | Should Have → Won't Have | Rebaixada por restrição de escopo da entrega, priorizando as 3 características principais. |
| Eficiência de desempenho | 2 | 1 | 8 | Could Have → Won't Have | Baixa viabilidade pois depende da latência e instabilidade de APIs externas. |
| Portabilidade / flexibilidade | 2 | 1 | 8 | Could Have → Won't Have | O foco atual do produto é o uso em desktop para pesquisa acadêmica. |
| Segurança | 1 | 1 | 5 | Won't Have | Exigiria testes de intrusão complexos, fora do escopo da disciplina. |
| Confiabilidade | 1 | 1 | 5 | Won't Have | Exigiria simulação de queda de fontes externas (PubMed, Scholar), inviável no momento. |


## 2. Características selecionadas

A equipe selecionou **três** características de qualidade do produto:

| # | Característica | Subcaracterísticas candidatas (ISO/IEC 25010:2023) | Justificativa (produto + objetivo da avaliação) |
|---|----------------|----------------------------------------------------|-------------------------------------------------|
| C1 | **Adequação funcional** | Completude, Correção e Pertinencia. | O VICKY promete poupar o tempo de pesquisa filtrando artigos metodologicamente relevantes. Avaliar a correção e completude garante que o pipeline de LLM e as integrações (PubMed/Scholar) entregam o valor prometido sem falhas nas regras de negócio. |
| C2 | **Capacidade de interação** | Operabilidade, Proteção contra erro do usuário, Autodescritividade, Reconhecimento e + (ver modelo de qualidade) | Estudantes de medicina precisam configurar critérios complexos (PICO) para iniciar uma revisão. A interface deve guiar o usuário na parametrização correta e na interpretação clara do "Quality Score" para evitar erros no uso dos créditos pagos. |
| C3 | **Manutenibilidade** | Modularidade, Analisabilidade e Modificabilidade | O sistema possui um orquestrador assíncrono complexo (`pipeline.py`) e integrações externas instáveis por natureza (LLMs, scrapers). Avaliar a modularidade e analisabilidade do código Python garante que os desenvolvedores consigam atualizar as fontes de busca e os prompts facilmente no futuro.  |

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
| 0.5 | 18/10/2026 | Aplicação do método MoSCoW e inclusão de justificativas com foco no público-alvo | Guilherme Moura | - |
| 0.6 | 18/10/2026 | Revisão das subcaracterísticas selecionadas | Gabriel Fae | Guilherme Moura |