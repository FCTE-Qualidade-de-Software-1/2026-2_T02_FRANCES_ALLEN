# Escopo, profundidade e objetos de avaliação

## 1. Dentro e fora do escopo

| Item | Definição |
|------|-----------|
| Escopo | Funcionalidades de núcleo: Cadastro e login (F01), Criação de projeto e geração PICO (F02, F03, F04); triagem completa (F05), executada com créditos de cortesia, sem compra pela equipe; visualização da lista ranqueada, favoritos, log auditável e exportação (F06, F07, F08, F09); código-fonte do backend em Python focado na orquestração da triagem (diretórios `src/vicky/` e `tests/`). |
| Fora do escopo | Funcionalidades de suporte: Configurações da conta (F11), pois não diferenciam a qualidade do produto; compra de créditos (F10) devido à restrição do projeto acadêmico; módulos e instabilidade de gateways de pagamento (Asaas/Stripe) e infraestrutura de deploy (Docker/VPS). |

## 2. Objetos de avaliação

| Objeto | Característica relacionada | Profundidade | Justificativa |
|--------|----------------------------|--------------|---------------|
| Funcionalidades de acesso, parametrização, triagem e resultados (F01 a F09) | C1, C2 | Testes de cenário (caixa-preta) e questionários de usabilidade com a amostra de estudantes de medicina. | O acesso à plataforma (F01), a interação com os critérios PICO e a precisão dos logs e exportações formam a jornada completa do VICKY para a fundamentação teórica de estudantes. |
| Código-fonte principal do backend em Python (diretórios `src/vicky/` e `tests/`) | C3 (Manutenibilidade) | Análise estática automatizada com foco na extração de métricas de complexidade estrutural, duplicação de código, adesão a padrões de formatação (PEP8), registros de log e completude de testes automatizados. | O orquestrador de busca é complexo e assíncrono. Medir complexidade ciclomática, adesão ao PEP8, duplicação e cobertura de testes é essencial para a sustentabilidade e a evolução segura do projeto. |

As funcionalidades candidatas estão listadas em [Objeto de avaliação](objeto-de-avaliacao.md#3-principais-funcionalidades).

## 3. Limites de validade dos resultados

* **Plataforma:** Os testes de usabilidade e funcionalidade refletem o comportamento da aplicação em navegadores web desktop, não atestando a experiência em dispositivos móveis.
* **Amostragem:** A avaliação da capacidade de interação (C2) e adequação funcional (C1) estará limitada às percepções e aos cenários executados pela amostra específica de estudantes de medicina participantes dos testes.
* **Fatores Externos:** A avaliação não julga a precisão médica dos modelos de linguagem subjacentes (OpenRouter) ou a disponibilidade das bases (PubMed, SciELO). O foco recai sobre como a plataforma reage e orquestra essas dependências.
* **Código Limitado:** A métrica de manutenibilidade (C3) reflete apenas o código da aplicação (Python), excluindo a qualidade de dependências de interface (Tailwind CSS, Alpine.js) ou configurações de CDN/Proxy (Cloudflare)

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 16/10/2026 | Página criada a partir da seção "Propósito da avaliação" de Seleção e justificativa | Gabriel Fae | - |
| 0.2 | 18/10/2026 | Definição do escopo, objetos de avaliação e limites de validade | Guilherme Moura | - |
| 0.3 | 18/10/2026 | Triagem completa (F05) incluída no escopo por decisão do grupo, porque a lista ranqueada, os favoritos, o log e a exportação só existem depois de uma triagem | Larissa Gomes Silva | - |
| 0.4 | 18/10/2026 | Inclusão do diretório tests/ e da completude de testes nos objetos de avaliação de C3 | Guilherme Moura | - |