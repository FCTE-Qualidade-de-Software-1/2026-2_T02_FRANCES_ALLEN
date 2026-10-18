# Objeto de avaliação: VICKY

## 1. Identificação

| Item | Descrição |
|------|-----------|
| Nome | VICKY |
| Tipo | Aplicação web (SaaS) de triagem de literatura científica assistida por IA, acessada pelo navegador |
| URL | <https://vicky.synaptha.com/> |
| Organização responsável | Synaptha Inc Ltda (CNPJ 63.642.396/0001-90), Brasília-DF |
| Versão avaliada / data de acesso | Versão em produção acessada em 17/10/2026 (Termos de Uso e Política de Privacidade na versão 2026-09-29) |
| Público-alvo | Estudantes de medicina (foco declarado) em iniciação científica, TCC, monografia e artigo de resumo; uso restrito a maiores de 18 anos |
| Plataformas | Navegador web, desktop e mobile |
| Exige cadastro ou login | Sim, com nome, e-mail e senha. |
| Modelo de acesso | Cadastro, criação de projeto e prévia do PICO gratuitos; triagem completa paga por crédito avulso (1 crédito = 1 triagem, R$ 24,90), sem assinatura nem mensalidade |
| Acesso ao código-fonte | Sim, código-fonte completo, liberado pela equipe de desenvolvimento (ativa no projeto) |
| Repositório do código | _link ou forma de acesso - a definir_ |

## 2. Descrição

### 2.1 Visão geral

O VICKY é uma plataforma web que automatiza as etapas operacionais da revisão de literatura científica para *estudantes de medicina*. O usuário informa o tema da pesquisa que está realizando e o sistema segue o seguinte passo-a-passo:

1. gera um **protocolo PICO** (população, intervenção, comparador e desfecho);
2. busca artigos nas bases **PubMed**, **SciELO** e **Google Acadêmico**;
3. aplica a **triagem com modelos de linguagem** em duas passadas independentes (*double-check* das exclusões);
4. entrega uma **lista ranqueada** (normalmente um top 30) por **Quality Score** de 0 a 100, com os links para as fontes e um log auditável dos critérios.

A proposta do site (e onde mostra seu valor) é trocar dias de triagem manual por uma lista com critérios metodológicos explícitos, que o estudante possa defender perante o orientador.

**Alternativas usadas pelo público:** é comum que estudantes façam busca manual no próprio PubMed, SciELO ou Google Acadêmico. Também existem ferramentas de IA que podem indicar artigos relacionados ao tema pesquisado, como o próprio ChatGPT.

### 2.2 Módulos

Visão funcional dos módulos, inferida das páginas públicas, dos Termos de Uso, da Política de Privacidade e do acesso ao código-fonte em nosso fork do projeto original. 

| ID | Módulo | Responsabilidade | Fonte da evidência |
|----|--------|------------------|--------------------|
| M01 | Página institucional (*landing*) | Apresentação do produto, funcionamento, entregas, preço, FAQ, Termos e Privacidade | Site |
| M02 | Autenticação e conta | Cadastro, login, recuperação de senha, sessão por cookie, registro do aceite dos Termos e exclusão de conta | Site, Privacidade |
| M03 | Projetos | Criação do projeto: tema, observações, recortes (população, período, tipo de estudo, objetivo), modo de revisão (sistemática/narrativa), bases e quantidade (Top N) | Site, FAQ |
| M04 | Geração de PICO | Geração e revisão do protocolo PICO e dos critérios de inclusão e exclusão por LLM (prévia gratuita) | Site, Termos, Código-Fonte |
| M05 | Busca em bases científicas | Consulta ao PubMed, SciELO e Google Acadêmico usando os termos derivados do PICO | Termos, Privacidade, Código-Fonte |
| M06 | Triagem e ranqueamento | Triagem por LLM em duas passadas, *double-check* das exclusões e cálculo do Quality Score | Termos, Código-Fonte |
| M07 | Resultados e exportação | Lista ranqueada, links para as fontes, favoritos, log auditável e exportação em PDF, XLSX, CSV e JSON | Site, Termos, Código-Fonte  |
| M08 | Créditos e pagamento | Compra de créditos (Pix/cartão via Asaas; Stripe nas compras até 09/2026), consumo, estorno e devolução por falha | Termos, Privacidade |
| M09 | Configurações | Cadastro e remoção de credenciais opcionais de serviços de terceiros | Privacidade, Código-Fonte  |
| M10 | Controle de uso e retenção | Limite diário de prévias por conta/IP, prevenção de abuso e expurgo diário de registros com mais de 180 dias | Site, Privacidade, Código-Fonte  |

### 2.3 Interfaces

_Ainda falta anexar imagens das interfaces do Vicky nas interfaces web e suas rotas_

| Interface | Tipo | Descrição |
|-----------|------|-----------|
| Interface web | Usuário (navegador) | Páginas HTML renderizadas no servidor, com interatividade em Alpine.js; rotas públicas `/`, `/login`, `/signup`, `/esqueci-senha`, `/termos` e `/privacidade` |
| Bases científicas | Sistema externo (saída) | Consultas ao PubMed, SciELO e Google Acadêmico com termos de busca, sem dados pessoais |
| Provedores de LLM | Sistema externo (saída) | OpenRouter, que intermedeia modelos como OpenAI e Anthropic; recebe o tema, os critérios e os títulos e resumos dos artigos |
| Gateway de pagamento | Sistema externo (saída) | Asaas (Pix e cartão); Stripe Checkout no legado |
| Arquivos exportados | Saída de dados | PDF, XLSX, CSV e JSON com os resultados do projeto |

### 2.4 Dependências

| Dependência | Tipo | Observação |
|-------------|------|------------|
| PubMed, SciELO, Google Acadêmico | Fontes de dados externas | Indisponibilidade ou resultados parciais afetam a triagem (Termos, §9) |
| OpenRouter e provedores de LLM | Serviço externo (EUA) | Núcleo da geração do PICO e da triagem |
| Asaas / Stripe | Pagamento | Necessários para comprar créditos e, portanto, para a triagem completa. Hoje as compras passam pelo Asaas (Pix e cartão); o Stripe atendeu as compras até 09/2026 |
| Cloudflare | Proxy, CDN e segurança | Todo o tráfego passa por ele |
| Hostinger | Hospedagem do servidor e do banco de dados (Brasil) | -- |
| Alpine.js 3.14.1, Tailwind CSS, Google Fonts | Frontend | Identificados no Frontend do repositório |
| Python 3.11 ou superior, FastAPI, Uvicorn, Jinja2 e PostgreSQL (driver psycopg) | Backend | Identificados no `pyproject.toml` do repositório |

### 2.5 Restrições

| Restrição | Tipo | Impacto para a avaliação |
|-----------|------|--------------------------|
| A triagem completa custa 1 crédito (R$ 24,90) | Financeira | Limita o número de execuções completas que a equipe consegue observar; a avaliação usa créditos de cortesia, sem compra pela equipe |
| Limite diário de prévias gratuitas por conta | Uso | Limita repetições de teste da geração do PICO, limita diferentes testes no mesmo dia com usuários |
| Os Termos proíbem engenharia reversa, *scraping* abusivo e sobrecarga intencional | Legal/contratual | Testes de carga ou automação contra a produção dependem de autorização da equipe do VICKY |
| A triagem depende de LLM | Técnica | Resultados podem variar entre execuções do mesmo tema |
| LGPD; uso apenas por maiores de 18 anos | Legal | Testes com usuários exigem participantes adultos, dados anonimizados e termos de compromisso |

## 3. Principais funcionalidades

Levantadas a partir das páginas públicas, dos Termos de Uso e da Política de Privacidade (acesso em 17/10/2026). As telas internas ainda precisam ser verificadas com uma conta.

| ID | Funcionalidade | Descrição | No escopo da avaliação? |
|----|----------------|-----------|:-----------------------:|
| F01 | Cadastro e login | Criação de conta (nome, e-mail, senha, aceite dos Termos), login e recuperação de senha | sim |
| F02 | Criação de projeto | Informar o tema e as observações; ajustar população, período, tipo de estudo e objetivo; escolher o modo de revisão (sistemática/narrativa) | sim |
| F03 | Geração do protocolo PICO | Geração automática do PICO e dos critérios de inclusão e exclusão a partir do tema, com revisão pelo usuário; gratuita, com limite diário | sim |
| F04 | Seleção de bases e quantidade | Escolha entre PubMed, SciELO e Google Acadêmico, e do tamanho do resultado (Top 10, 20 ou 30) | sim |
| F05 | Triagem completa | Busca nas bases, triagem por LLM em duas passadas e *double-check* das exclusões; consome 1 crédito | sim |
| F06 | Lista ranqueada por Quality Score | Exibição dos artigos ordenados por Quality Score (0-100), com link para abrir a fonte | sim |
| F07 | Favoritos | Marcar e desmarcar artigos como favoritos na lista | sim |
| F08 | Log auditável | Registro das buscas e dos critérios de inclusão e exclusão aplicados, para anexar ao trabalho | sim |
| F09 | Exportação de resultados | Exportação em PDF, XLSX, CSV e JSON | sim |
| F10 | Compra de créditos | Compra avulsa por Pix ou cartão, com direito de arrependimento em 7 dias e devolução do crédito em caso de falha | não |
| F11 | Configurações da conta | Gerenciamento de credenciais opcionais de serviços de terceiros | não  |

## 4. Contexto de uso

| Aspecto | Descrição |
|---------|-----------|
| Usuários | Estudantes de medicina (_semestre e perfil a levantar_) |
| Tarefas típicas | _ex.: localizar artigo para seminário; revisar tema para prova_ |
| Ambiente | _ex.: celular entre aulas; notebook em casa ou biblioteca_ |

## 5. Implicações para a avaliação

Hoje, possuímos acesso ao código fonte, ao site e a praticamente todos os testes do VICKY.

Contudo, ainda somos limitados pelo uso restritivo de LLMs, pesquisas em sites externos, valor monetário e pelas funcionalidades realizadas/dependentes de terceiros.

As partes interessadas estão em [Requisitante e partes interessadas](partes-interessadas.md), e o recorte do que será avaliado está em [Escopo e profundidade](escopo.md).

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 05/10/2026 | Criação da estrutura do documento | Gabriel Fae | - |
| 0.2 | 16/10/2026 | Página movida para a Fase 1; partes interessadas movidas para página própria | Gabriel Fae | - |
| 0.3 | 17/10/2026 | Identificação, descrição estruturada (módulos, interfaces, dependências, restrições) e funcionalidades levantadas a partir do site público | Gabriel Fae | Lucas Avelar |
| 0.4 | 18/10/2026 | Revisão: modelo de acesso por crédito avulso, papel do Asaas e do Stripe, stack do backend e correções de redação | Lucas Avelar | - |
| 0.5 | 18/10/2026 | Triagem completa (F05) marcada como dentro do escopo, em linha com a página de escopo; restrição financeira atualizada com os créditos de cortesia | Larissa Gomes Silva | - |
