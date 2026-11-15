# Método do G3 (manutenibilidade)

Este método cobre as seis métricas do G3, todas medidas no código-fonte do VICKY por análise estática e pela execução da suíte de testes. Definição, fórmula e níveis são os da [Fase 2](../fase-2/especificacao-das-metricas.md); esta página diz como executar a coleta de forma que qualquer integrante, na própria máquina, chegue ao mesmo número. A coleta inteira roda com um comando, o script [`coletar.sh`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/tree/main/dados/avaliacao/G3), e o cálculo sai das saídas brutas, sem contagem à mão.

## 1. Métricas cobertas

| Métrica | Medida (ISO/IEC 25023:2016) | Questão | Ferramenta e comando de base | Pasta em `dados/avaliacao/G3/` |
|---------|-----------------------------|:-------:|------------------------------|--------------------------------|
| [M3.1.1](../fase-2/especificacao-das-metricas.md#m311) | Adaptada de MMo-1-G | Q3.1 | Leitura dos imports por AST (`extrair.py imports`) | `M3.1.1/` |
| [M3.1.2](../fase-2/especificacao-das-metricas.md#m312) | MMo-2-S | Q3.1 | `radon cc src/vicky/pipeline.py -s -a` | `M3.1.2/` |
| [M3.2.1](../fase-2/especificacao-das-metricas.md#m321) | Medida adicional | Q3.2 | `flake8 --isolated src/vicky/ --count --statistics` | `M3.2.1/` |
| [M3.2.2](../fase-2/especificacao-das-metricas.md#m322) | Medida adicional | Q3.2 | `pylint --disable=all --enable=duplicate-code src/vicky/` e `radon raw` | `M3.2.2/` |
| [M3.2.3](../fase-2/especificacao-das-metricas.md#m323) | Adaptada de MAn-1-G | Q3.2 | Inventário por AST (`extrair.py funcoes`) e inspeção do código | `M3.2.3/` |
| [M3.3.1](../fase-2/especificacao-das-metricas.md#m331) | Adaptada de MTe-1-G | Q3.3 | `pytest --cov=src/vicky/ tests/` | `M3.3.1/` |

As medidas foram revistas na Fase 2 antes desta coleta (#23): M3.2.1 e M3.2.2 usavam MRe-2-S e MRe-1-G, que na norma pertencem à reusabilidade, e passaram a medidas adicionais de analisabilidade; M3.1.1, M3.2.3 e M3.3.1 passaram a declarar a adaptação. O motivo de cada uma está na [ficha da métrica](../fase-2/especificacao-das-metricas.md) e no [GQM do G3](../fase-2/objetivos-questoes-hipoteses.md#g3).

## 2. Por que este método

**O ponto de vista pede medida interna.** O G3 avalia a manutenibilidade do ponto de vista da equipe de desenvolvimento, e a [Fase 1](../fase-1/escopo.md) delimitou o objeto como o código do backend (`src/vicky/` e `tests/`), com análise estática automatizada. As medidas de manutenibilidade da ISO/IEC 25023:2016 (subcláusula 8.8) são calculadas sobre o próprio produto, e todas as fórmulas das fichas do G3 são contagens sobre o código: imports, ramificações, violações de estilo, linhas repetidas, chamadas de log e linhas executadas. Nenhuma delas depende de usuário, de produção ou de opinião, o que permite um método inteiramente automatizado, com inspeção humana só para conferir a regra de M3.2.3.

**Ferramenta no lugar de contagem manual.** Nesta fase o processo da ISO/IEC 25040:2024 projeta a avaliação, e o critério de pronto da #23 é que qualquer integrante rode os comandos e chegue ao mesmo número. Contar à mão 1.916 violações de estilo ou 7.519 linhas executáveis não é repetível; uma ferramenta com versão fixa, configuração fixa e entrada fixa é. Por isso cada métrica tem uma ferramenta, e cada escolha abaixo existe para fechar uma fonte de variação:

| Fonte de variação | Como o método a fecha |
|-------------------|-----------------------|
| Versão do código | Commit fixo, `c2ae570`, exportado com `git archive`, que leva só os arquivos versionados. Arquivo local do clone (`.env`, banco, cache) não entra na medição |
| Versão das ferramentas | Ambientes novos a cada coleta, instalados de lockfile com hash (`ferramentas.lock`, `testes.lock` e o `requirements.lock` do próprio VICKY). O lockfile fixa a versão resolvida de cada pacote e o hash impede trocar o pacote sem trocar o arquivo ([uv, *Locking and syncing*](https://docs.astral.sh/uv/concepts/projects/sync/), consultado em 14/11/2026) |
| Versão do Python | Python 3.12, a mesma série da imagem de produção do VICKY (`Dockerfile.prod`, base `python:3.12-slim` fixada por digest) e a usada para gerar o `requirements.lock` |
| Configuração das ferramentas | A Fase 2 manda usar a configuração padrão. O flake8 roda com `--isolated` e o pylint com um arquivo de configuração vazio, para que nenhum arquivo de configuração da máquina do avaliador mude as regras |
| Ambiente da suíte de testes | Suíte offline do VICKY, a mesma do `make test`: banco SQLite descartável, rede bloqueada e credenciais falsas. `DATABASE_URL` vazia, sem Postgres local e sem chave da Stripe |
| Regra de contagem | Cada ambiguidade da ficha (o que é uma dependência, que linha da saída conta, que total de linhas usar) foi decidida na seção 4 e está escrita em código em `calcular.py` |

**Por que cada ferramenta.** As ferramentas são as citadas nas fichas da Fase 2:

- **radon** calcula a complexidade ciclomática de McCabe por função e a classifica de A a F; a nota C começa em 11 ([radon, *Command-line Usage*](https://radon.readthedocs.io/en/latest/commandline.html), consultado em 14/11/2026). O limiar da Fase 2 (CC acima de 10, notas C a F) coincide com a fronteira entre B e C. O mesmo radon (`radon raw`) dá o total de linhas para M3.2.2.
- **flake8** reúne o pycodestyle, que verifica o PEP 8, e o pyflakes, que acusa erro lógico como import sem uso. É o verificador que a ficha de M3.2.1 cita. Com `--isolated`, usa os padrões do pycodestyle, inclusive o limite de 79 caracteres por linha do PEP 8.
- **pylint**, com apenas a verificação `duplicate-code` (R0801) ligada, compara os arquivos e aponta trechos de 4 ou mais linhas iguais, ignorando comentários, docstrings, imports e assinaturas, que são os padrões da ferramenta.
- **pytest-cov** liga o coverage.py ao pytest. A cobertura de linhas do coverage.py conta comandos executáveis, não linhas físicas, o que é o "total de linhas do escopo testável" da ficha de M3.3.1.
- **AST da biblioteca padrão** para M3.1.1 e para o inventário de M3.2.3. Não há ferramenta consagrada que conte imports internos com a regra da ficha, e a contagem por expressão regular erraria em imports de várias linhas e em imports relativos. O módulo `ast` lê o código sem executá-lo.

**Por que este commit.** As hipóteses do G3 e o [método do G2 por inspeção](metodo-g2-inspecao.md#22-ambiente) usam o commit `c2ae570` do fork `LucasAvelar2711/Vicky`, de 29/09/2026, e medir a mesma versão mantém os três objetivos comparáveis. O commit foi conferido antes da coleta: existe no fork `LucasAvelar2711/Vicky` (merge do PR #26 na `main`). Ele **não** existe no fork `LucasAvelar2711/vicky-avaliacao`, cuja `main` para em `6c35d25`, de 27/08/2026; por isso a coleta clona o `LucasAvelar2711/Vicky`.

**Coerência com a Fase 2.** Cada métrica usa a fórmula da ficha e as faixas da [tabela de níveis](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica), e a agregação segue as [regras do G3](../fase-2/niveis-e-julgamento.md#4-regras-do-g3-manutenibilidade):

| Métrica | Fórmula da ficha | A no método | B no método | Piso de Bom | Papel na agregação |
|---------|------------------|-------------|-------------|:-----------:|--------------------|
| M3.1.1 | X = A / B | Dependências internas distintas | Arquivos `.py` de `src/vicky/` | abaixo de 10 | Média em Q3.1 |
| M3.1.2 | X = 1 menos A / B | Funções com CC acima de 10 | Funções e métodos de `pipeline.py` | 85% | Média em Q3.1; bloqueadora |
| M3.2.1 | C = A / B | Arquivos sem violação | Arquivos `.py` de `src/vicky/` | 90% | Média em Q3.2 |
| M3.2.2 | D = linhas duplicadas / total, em % | Linhas cobertas por trecho duplicado | LOC do `radon raw` | até 5% | Média em Q3.2 |
| M3.2.3 | X = A / B | Funções críticas com chamada a `logging` | Funções críticas de `pipeline.py` | 75% | Média em Q3.2 |
| M3.3.1 | T = executadas / testáveis, em % | Linhas executáveis executadas | Linhas executáveis de `src/vicky/` | 70% (H3.3) | Única em Q3.3; limita G3 |

**Limites conhecidos.** A cobertura de ramos mostra o lado falso de um `if` que a cobertura de linhas dá como coberto ([coverage.py, *Branch coverage measurement*](https://coverage.readthedocs.io/en/latest/branch.html), consultado em 14/11/2026). A ficha de M3.3.1 pede cobertura de linhas e o método mantém a ficha; a cobertura de ramos fica como sugestão para uma próxima avaliação. Em M3.2.1, o limite de 79 caracteres responde pela maior parte das violações; o método aplica o padrão, como a ficha manda, e a distribuição por código de regra fica registrada em `flake8-statistics.txt` para a análise da Fase 4.

## 3. Preparação

### 3.1 Papéis

| Papel | Responsabilidade |
|-------|------------------|
| A1 | Roda a coleta, faz a inspeção de M3.2.3 e sobe os dados |
| A2 | Repete a coleta na própria máquina, sem olhar o resultado de A1 antes de terminar, e faz a sua inspeção de M3.2.3 |
| A3 | Decide apenas as divergências da inspeção de M3.2.3 que A1 e A2 não resolverem. Não pode ser A1 nem A2 |

### 3.2 Hardware e software

| Item | Requisito | Versão usada na coleta de 14/11/2026 |
|------|-----------|--------------------------------------|
| Computador | macOS ou Linux, 4 GB de RAM livre e 1 GB de disco livre para o clone e os dois ambientes (o de testes ocupa cerca de 260 MB) | Apple M4, 16 GB de RAM |
| Sistema operacional | macOS ou Linux com bash. No Windows, usar o WSL (não testado pela equipe) | macOS 26.6.2 (Darwin 25.6.0, arm64) |
| Rede | Necessária só para clonar e instalar pacotes. A suíte de testes roda sem rede | - |
| git | 2.x, com acesso de leitura ao fork privado `LucasAvelar2711/Vicky` | - |
| uv | 0.12 ou mais recente; instala o Python e os pacotes | 0.12.5 |
| Python | Série 3.12, instalada pelo uv se não houver (`uv python install 3.12`) | 3.12.13 |
| radon | 6.0.1 | 6.0.1 |
| flake8 | 7.5.0, com pycodestyle 2.15.0, pyflakes 4.1.0 e mccabe 0.7.0 | as mesmas |
| pylint | 4.1.4, com astroid 4.3.4 | as mesmas |
| pytest | 9.2.0 | 9.2.0 |
| pytest-cov | 7.1.0, com coverage 7.17.3 | as mesmas |
| Dependências do VICKY | As 58 do `requirements.lock` do commit avaliado, com hash | as mesmas |
| Postgres e Stripe | **Não** pode haver Postgres escutando em `localhost:5433` nem chave `sk_test_` da Stripe no Keychain. Com eles, a suíte roda testes a mais e a cobertura muda | ausentes |

As versões exatas de todas as dependências, com hash, estão em `dados/avaliacao/G3/ferramentas.lock` e `dados/avaliacao/G3/testes.lock`. A versão realmente usada em cada coleta é gravada em `ambiente.txt`, em cada pasta de métrica.

### 3.3 Conhecimento exigido

- Terminal com bash e git básico (clonar, trocar de commit, ver diferença entre arquivos).
- Leitura de Python, para a inspeção de M3.2.3: reconhecer definição de função, bloco `try`/`except`, chamada a `logging` e chamada a `print`.
- Noção de complexidade ciclomática e de cobertura de testes, no nível das fichas da Fase 2. Não é preciso conhecer o domínio do VICKY nem saber programar as ferramentas.

### 3.4 Versão do código

| Item | Valor |
|------|-------|
| Repositório | `https://github.com/LucasAvelar2711/Vicky` (privado; pedir acesso de leitura a Lucas Avelar) |
| Commit | `c2ae5704b9770fbc33156fb3f457c4e8c63e5007`, de 29/09/2026 20:51 (UTC-3) |
| Escopo medido | `src/vicky/` (38 arquivos `.py`, incluindo `sources/` e `web/`) e `tests/` |

O script confere que o commit existe no clone antes de começar e para com erro se não existir. O clone não é alterado: a cópia de trabalho vai para uma pasta temporária.

### 3.5 Instalação

Uma vez por máquina:

```bash
# 1. uv (se ainda não houver); ver https://docs.astral.sh/uv/getting-started/installation/
curl -LsSf https://astral.sh/uv/install.sh | sh
# 2. Python 3.12 gerenciado pelo uv
uv python install 3.12
# 3. Clone do fork avaliado e do repositório do trabalho
git clone https://github.com/LucasAvelar2711/Vicky.git ~/vicky-fork
git clone https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN.git
```

Os ambientes das ferramentas não são instalados à mão: o `coletar.sh` cria dois ambientes novos a cada execução, para que nenhum pacote antigo da máquina entre na medição. Os comandos que ele roda são estes:

```bash
uv venv --python 3.12 "$TRAB/venv-ferramentas"
uv pip install --python "$TRAB/venv-ferramentas/bin/python" --require-hashes -r dados/avaliacao/G3/ferramentas.lock
uv venv --python 3.12 "$TRAB/venv-testes"
uv pip install --python "$TRAB/venv-testes/bin/python" --require-hashes -r "$TRAB/codigo/requirements.lock"
uv pip install --python "$TRAB/venv-testes/bin/python" --require-hashes -r dados/avaliacao/G3/testes.lock
```

### 3.6 Como a suíte de testes roda

A suíte do VICKY (`tests/`, 1.034 testes no commit avaliado) foi escrita para rodar offline. O `tests/conftest.py` cria um banco SQLite novo por teste, aponta a configuração para um `.env` falso com credenciais inventadas e derruba qualquer teste que tente abrir conexão de rede. O comando do método é o mesmo do `make test` do VICKY, com a cobertura ligada:

```bash
DATABASE_URL= python -m pytest --cov=src/vicky/ tests/
```

`DATABASE_URL` vazia é obrigatória: com ela preenchida, os testes de Postgres tentam conectar. Não é preciso instalar o VICKY como pacote, porque o `conftest.py` põe `src/` no caminho de import.

**Resultado esperado no ambiente de referência:** 1.002 testes aprovados, 27 pulados, 5 falhas esperadas (`xfail`) e nenhuma falha, em cerca de 2 minutos e meio. Os 27 pulados precisam de recurso externo que o método exclui de propósito:

| Testes pulados | Motivo informado pelo próprio teste |
|:--------------:|-------------------------------------|
| 20 | Postgres local (`make pg-up` e `make pg-init`) |
| 6 | Chave de teste da Stripe no Keychain |
| 1 | Arquivo de outro repositório, que só existe na máquina do desenvolvedor |

## 4. Passo a passo

### 4.1 Coleta completa

Na raiz do repositório do trabalho, na branch em que os dados serão registrados:

```bash
dados/avaliacao/G3/coletar.sh ~/vicky-fork
```

O script executa, nesta ordem, os passos 4.2 a 4.7, grava as saídas brutas na pasta de cada métrica e chama `calcular.py`. Ao fim, imprime o valor e o nível de cada métrica. Para guardar a pasta temporária e conferir algo depois, defina `TRAB` antes (`TRAB=~/g3-trabalho dados/avaliacao/G3/coletar.sh ~/vicky-fork`). Os comandos abaixo rodam dentro de `$TRAB/codigo`, a cópia do commit; `$F` é `$TRAB/venv-ferramentas/bin`, `$T` é `$TRAB/venv-testes/bin` e `$G3` é a pasta `dados/avaliacao/G3`.

**Lista de arquivos (denominador de M3.1.1 e M3.2.1):**

```bash
find src/vicky -name '*.py' -type f | LC_ALL=C sort > $G3/M3.1.1/arquivos-py.txt
```

Entram todos os `.py` de `src/vicky/` e das subpastas, inclusive os `__init__.py` vazios, porque cada um é um módulo do pacote.

### 4.2 M3.1.1: acoplamento de componentes

```bash
$F/python -I $G3/extrair.py imports src vicky > $G3/M3.1.1/imports.csv
```

O script lê cada arquivo com o módulo `ast` e escreve uma linha por import que aponta para o próprio pacote. **Regra de contagem**, para que todos cheguem ao mesmo A:

1. Conta import absoluto (`import vicky.db`, `from vicky.storage import connect`) e relativo (`from .storage import connect`, `from ..storage import connect`), resolvido para o nome completo do módulo.
2. `from pacote import submodulo` aponta para o submódulo (`from .web import projects` vale `vicky.web.projects`); `from modulo import nome` aponta para o módulo (`from .config import Config` vale `vicky.config`).
3. Conta import dentro de função, porque também cria dependência.
4. A é o número de pares distintos (arquivo de origem, módulo de destino). O mesmo módulo importado duas vezes no mesmo arquivo conta uma vez, porque é uma dependência só. Biblioteca externa e biblioteca padrão não contam.
5. B é o número de linhas de `arquivos-py.txt`.

O número de declarações de import (sem tirar repetição) aparece em `resultado.md` apenas como informação.

### 4.3 M3.1.2: adequação da complexidade ciclomática

```bash
$F/radon cc src/vicky/pipeline.py -s -a > $G3/M3.1.2/radon-cc.txt
$F/radon cc src/vicky/pipeline.py -s -j > $G3/M3.1.2/radon-cc.json
```

O primeiro comando é o da Fase 2 e fica como registro legível; o segundo dá a mesma análise em JSON, que o cálculo lê. **Que blocos entram:** cada linha da saída começa com o tipo do bloco: `F` (função), `M` (método) ou `C` (classe). Entram em B as linhas `F` e `M`. A linha `C` não entra, porque resume a classe e não é uma função; em `c2ae570` a única classe de `pipeline.py` é uma exceção sem métodos. Função definida dentro de outra não aparece como linha própria na saída padrão do radon e não entra em B. A é o número de linhas `F` e `M` com complexidade maior que 10 (notas C, D, E ou F). A média impressa pelo `-a` não entra na fórmula.

### 4.4 M3.2.1: conformidade de estilo PEP 8

```bash
$F/flake8 --isolated src/vicky/ --count --statistics > $G3/M3.2.1/flake8-statistics.txt
$F/flake8 --isolated src/vicky/ > $G3/M3.2.1/flake8-violacoes.txt
```

O primeiro é o comando da Fase 2, que dá o total e a contagem por regra, mas não por arquivo. O segundo lista uma violação por linha, no formato `caminho:linha:coluna: código mensagem`. **Como obter os arquivos com violação:** o cálculo pega o caminho de cada linha do segundo arquivo e conta os caminhos distintos, o equivalente a `cut -d: -f1 flake8-violacoes.txt | sort -u | wc -l`. A = B menos os arquivos com violação; B = linhas de `arquivos-py.txt`. O flake8 sai com código 1 quando encontra violação, e o script trata isso como resultado, não como erro.

### 4.5 M3.2.2: densidade de código duplicado

```bash
: > $TRAB/pylintrc-vazio
$F/pylint --rcfile=$TRAB/pylintrc-vazio --disable=all --enable=duplicate-code src/vicky/ > $G3/M3.2.2/pylint-duplicate-code.txt
$F/radon raw src/vicky -s > $G3/M3.2.2/radon-raw.txt
$F/radon raw src/vicky -j > $G3/M3.2.2/radon-raw.json
```

**Como somar as linhas duplicadas:** cada aviso R0801 lista as ocorrências do mesmo trecho no formato `==modulo:[inicio:fim]`, com `inicio` contado a partir de zero e `fim` exclusivo; a ocorrência ocupa as linhas `inicio + 1` a `fim` do arquivo. O numerador é a união das linhas de todas as ocorrências, a original e as cópias, porque todas precisam ser mantidas juntas; linha que aparece em dois avisos conta uma vez. **Que total usar:** a soma do campo `loc` (linhas físicas) do `radon raw` em todos os arquivos, porque os intervalos do pylint também são linhas físicas, com comentários e linhas em branco entre o início e o fim. O valor com SLOC (linhas de código sem comentário e sem linha em branco) no denominador aparece em `resultado.md` só como informação.

### 4.6 M3.2.3: completude de logs do sistema

```bash
$F/python -I $G3/extrair.py funcoes src/vicky/pipeline.py > $G3/M3.2.3/funcoes.csv
grep -rn -E 'import logging|getLogger' src/vicky > $G3/M3.2.3/grep-logging.txt
```

**Quais são as funções críticas.** A ficha define como críticas as funções do orquestrador que fazem orquestração de APIs, manipulação de banco de dados e scraping. Para que a lista não dependa de quem inspeciona, o inventário de `funcoes.csv` traz toda função de nível de módulo e todo método de classe de `pipeline.py`, e marca como crítica a que atende a pelo menos um critério:

| Critério | Coluna | Regra |
|----------|--------|-------|
| Integração externa | `criterio_integracao` | O corpo usa um nome importado de `llm`, `discovery`, `sources`, `openrouter_cost`, `scraper` ou `acesso_aberto` (LLM, bases de artigos, scraping, custo do OpenRouter) |
| Banco de dados | `criterio_banco` | O corpo usa um nome importado de `storage`, `db`, `web.projects`, `web.workspaces` ou `web.queries` (camada de acesso ao banco e consultas) |
| Orquestração | `criterio_orquestracao` | O nome começa com `run_`, `schedule_` ou `_step_` (pontos de entrada e etapas do pipeline) |

Função que só chama outra função crítica, sem usar diretamente um desses módulos, não é marcada. Função aninhada conta como parte da função que a contém.

**Quando a função tem log.** A ficha pede o uso explícito da biblioteca `logging` do Python. Conta como log a chamada a `logging.<nível>(...)` ou a um objeto criado por `logging.getLogger` (`logger.info`, `log.exception` e semelhantes). `print`, `traceback.print_exc` e o registro de status do `job` no banco não contam como log pela ficha, mas o inventário os registra (`chamadas_print`, `traceback_print_exc`, `registro_em_job`) para a análise da Fase 4.

**Inspeção.** A1 e A2, separados, abrem `pipeline.py` no commit avaliado e conferem cada linha de `funcoes.csv` em `inspecao.md`: se a marcação de crítica está certa pela regra acima e se a contagem de chamadas a `logging` bate com o código. A inspeção confere a regra, não a substitui: se um avaliador achar erro no inventário, a correção vai para `extrair.py` e a coleta inteira roda de novo (seção 7). B é o número de funções com `critica = True` e A, as críticas com `chamadas_logging` maior que zero.

### 4.7 M3.3.1: completude de testes automatizados

```bash
DATABASE_URL= $T/python -m pytest --cov=src/vicky/ tests/ -p no:cacheprovider -rfEs \
  --junitxml=$G3/M3.3.1/junit.xml \
  --cov-report=term --cov-report=json:$G3/M3.3.1/coverage.json \
  > $G3/M3.3.1/pytest-cov.txt 2>&1
```

É o comando da Fase 2 com quatro acréscimos que não mudam a medição: `-p no:cacheprovider` evita gravar cache na cópia; `-rfEs` lista no fim os testes com falha, erro ou pulados e o motivo; `--junitxml` grava o resultado de cada teste; e o relatório JSON dá os números sem arredondamento. Como `--cov` recebe uma pasta, o coverage.py também conta os arquivos que nenhum teste importou, com 0% de cobertura. O valor é `covered_lines / num_statements` do campo `totals` de `coverage.json`, e não a porcentagem inteira da linha `TOTAL` do terminal, que é arredondada. Linhas marcadas com `pragma: no cover` saem do denominador, como o coverage.py faz por padrão.

## 5. Registro

Tudo o que a coleta produz fica em `dados/avaliacao/G3/`, uma pasta por métrica, como descreve o [README da pasta](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_FRANCES_ALLEN/blob/main/dados/avaliacao/G3/README.md):

```text
dados/avaliacao/G3/
├── README.md
├── coletar.sh, extrair.py, calcular.py      # scripts da coleta e do cálculo
├── ferramentas.in, ferramentas.lock         # radon, flake8 e pylint, com hash
├── testes.in, testes.lock                   # pytest e pytest-cov, com hash
├── resultados.csv                           # valor e nível das seis métricas
└── M3.x.y/
    ├── ambiente.txt     # data e hora da coleta, commit, SO, Python e versão de cada ferramenta
    ├── <saídas brutas>  # exatamente o que a ferramenta escreveu (ver README)
    └── resultado.md     # valor, A, B, contagens auxiliares e nível
```

Além da saída bruta, cada pasta recebe `ambiente.txt` e `resultado.md`, gerados pelo script, e M3.2.3 recebe `inspecao.md`, preenchido por A1 e A2. **Nada é editado à mão**, com exceção de `inspecao.md`: um número só muda se a saída bruta mudar. A1 sobe os dados num commit cuja mensagem diz o commit avaliado e a data da coleta.

## 6. Cálculo

O `calcular.py` lê apenas as saídas brutas e aplica a fórmula da ficha de cada métrica, com a regra de contagem da seção 4, e o nível pela [tabela de níveis](../fase-2/niveis-e-julgamento.md#1-niveis-de-pontuacao-por-metrica). Pode ser rodado sozinho, sem repetir a coleta:

```bash
$F/python -I dados/avaliacao/G3/calcular.py dados/avaliacao/G3
```

| Métrica | Arquivo lido | Valor calculado |
|---------|--------------|-----------------|
| M3.1.1 | `imports.csv`, `arquivos-py.txt` | Pares distintos dividido pelo número de arquivos, com duas casas |
| M3.1.2 | `radon-cc.json` | 1 menos (funções com CC acima de 10 dividido por funções), em % |
| M3.2.1 | `flake8-violacoes.txt`, `arquivos-py.txt` | Arquivos sem violação dividido por arquivos, em % |
| M3.2.2 | `pylint-duplicate-code.txt`, `radon-raw.json` | Linhas duplicadas dividido por LOC, vezes 100 |
| M3.2.3 | `funcoes.csv` | Críticas com `logging` dividido por críticas, em % |
| M3.3.1 | `coverage.json`, `junit.xml` | `covered_lines` dividido por `num_statements`, vezes 100; não calcula se houver teste com falha ou erro |

Da métrica para a questão e da questão para o objetivo valem as [regras do G3](../fase-2/niveis-e-julgamento.md#4-regras-do-g3-manutenibilidade), aplicadas na Fase 4: média dos pontos das métricas, M3.1.2 bloqueadora em Q3.1 e Q3.3 limitando o G3.

### 6.1 Coleta de 14/11/2026

Primeira execução do método, no commit `c2ae570`, repetida do zero na mesma máquina (ambientes novos e outra pasta de trabalho) com os mesmos A, B e valores nas seis métricas e saídas brutas iguais, salvo data, caminho e ordem das chaves do JSON do radon. A repetição por A2 em outra máquina, pedida na seção 7, ainda não foi feita. Os números completos estão em `dados/avaliacao/G3/resultados.csv` e no `resultado.md` de cada pasta.

| Métrica | A | B | Valor | Nível pela Fase 2 |
|---------|--:|--:|------:|-------------------|
| M3.1.1 | 78 | 38 | 2,05 | Excelente |
| M3.1.2 | 11 | 47 | 76,6% | Aceitável |
| M3.2.1 | 2 | 38 | 5,3% | Insatisfatório |
| M3.2.2 | 28 | 18.927 | 0,15% | Excelente |
| M3.2.3 | 0 | 33 | 0,0% | Insatisfatório |
| M3.3.1 | 4.750 | 7.519 | 63,17% | Aceitável |

A análise desses valores, a comparação com as hipóteses H3.1 a H3.3 e o julgamento do G3 ficam para a Fase 4.

## 7. Discordância e repetição

**Quem repete.** A2 roda o mesmo `coletar.sh`, na própria máquina, sem olhar o resultado de A1 até terminar. A coleta está confirmada quando o `resultados.csv` de A2 é igual ao de A1 em todas as colunas, exceto a data (`git diff dados/avaliacao/G3/resultados.csv`). A2 registra a repetição em `dados/avaliacao/G3/repeticao.md` (data, sistema, versões de `ambiente.txt` e resultado da comparação) e descarta as próprias saídas brutas com `git checkout -- dados/avaliacao/G3/`, para que fique no repositório uma única coleta.

**Quando os números divergem.** Divergência não se resolve com média nem com escolha de um dos valores. A1 e A2 comparam os `ambiente.txt` e as saídas brutas das duas coletas até achar a causa:

| Causa provável | Sinal | O que fazer |
|----------------|-------|-------------|
| Versão diferente de ferramenta ou de Python | `ambiente.txt` difere | Refazer com as versões da seção 3.2 |
| Postgres ou Stripe disponíveis na máquina | Menos de 27 pulados em `pytest-cov.txt` | Parar o Postgres ou rodar em máquina sem a chave, e refazer |
| Commit diferente | `commit_vicky` difere | Refazer no commit `c2ae570` |
| Defeito de script | Mesmo ambiente, saída bruta igual, resultado diferente | Corrigir `calcular.py` ou `extrair.py`, refazer as duas coletas e registrar a correção no histórico desta página |

**Teste com falha ou pulado em M3.3.1.**

- **Falha ou erro:** o `calcular.py` não calcula a métrica e marca "não medida". A1 roda a coleta de novo uma vez, para descartar falha passageira. Se a falha se repetir e vier do ambiente (dependência faltando, versão errada), corrige o ambiente e refaz. Se vier do próprio VICKY, A1 e A2 registram o teste e a mensagem em `M3.3.1/falhas.md`, e a métrica é declarada não aplicável, como manda a regra do G3 na Fase 2; nenhum valor é estimado.
- **Pulado:** os 27 pulados da seção 3.6 fazem parte do ambiente de referência e não invalidam a coleta. As linhas que eles executariam contam como não cobertas, porque o método mede a suíte que qualquer integrante consegue rodar. Pulado com motivo diferente desses três é tratado como falha.
- **Falha esperada (`xfail`):** são testes que o próprio VICKY marca como falha conhecida; as linhas que executam até falhar contam como cobertas, como o coverage.py registra.

**Divergência na inspeção de M3.2.3.**

1. A1 e A2 preenchem as colunas próprias em `inspecao.md`, sem ver a do outro.
2. Em cada linha em que discordam, os dois reabrem o trecho do código e aplicam a regra da seção 4.6. A decisão e o motivo vão para a coluna `consenso`.
3. Se a divergência mostrar que o inventário está errado (por exemplo, um módulo de banco que a regra não lista), a regra é corrigida em `extrair.py`, vale para todas as funções e a coleta inteira roda de novo. `funcoes.csv` não é editado à mão.
4. Sem consenso, A3 decide olhando apenas o código e a regra, e a linha recebe `decidido_por = A3`.

**Quando refazer a coleta inteira:** mudança em `extrair.py` ou `calcular.py`, troca de versão de ferramenta ou de Python, ou saída bruta perdida. A data nova vai para `ambiente.txt`, e o motivo, para o histórico desta página.

## Histórico de versão

| Versão | Data | Descrição | Autor(a) | Revisor(a) |
|--------|------|-----------|----------|------------|
| 0.1 | 04/11/2026 | Criação da página | Lucas Avelar | - |
| 0.2 | 09/11/2026 | Esqueleto com o que a Fase 2 define e os pontos em aberto para o responsável | Gabriel Fae | - |
| 0.3 | 14/11/2026 | Método completo: justificativa, ambiente e versões, comando e regra de contagem por métrica, registro, cálculo por script, discordância e repetição, e a coleta de 14/11/2026 no commit `c2ae570` | Lucas Avelar | - |
