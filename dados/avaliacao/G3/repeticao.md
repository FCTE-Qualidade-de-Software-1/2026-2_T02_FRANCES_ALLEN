# G3: repetição independente da coleta por A2 (18/11/2026)

Repetição independente do `coletar.sh` sobre o commit `c2ae570`, executada por A2 (Guilherme Moura) em outra máquina e outro sistema operacional, sem consulta prévia às saídas de A1, conforme a seção 7 do [Método do G3](../../../docs/fase-3/metodo-g3.md).

As saídas brutas desta execução foram descartadas com `git checkout -- dados/avaliacao/G3/`, para que permaneça no repositório uma única coleta oficial (a de 14/11/2026 21:00). Ficam registrados abaixo a saída do script, o `resultados.csv` gerado, as versões do ambiente e a comparação com a coleta original. Os caminhos locais de pasta foram omitidos.

## Saída do script

```text
Commit avaliado: c2ae5704b9770fbc33156fb3f457c4e8c63e5007
M3.1.1: 2,05 (Excelente)
M3.1.2: 76,6% (Aceitável)
M3.2.1: 5,3% (Insatisfatório)
M3.2.2: 0,15% (Excelente)
M3.2.3: 0,0% (Insatisfatório)
M3.3.1: 63,17% (Aceitável)

```

## resultados.csv da repetição

```text
metrica,nome,valor,A,B,nivel,commit,data_coleta
M3.1.1,Acoplamento de componentes,"2,05",78,38,Excelente,c2ae570,2026-11-18 12:04 -0300
M3.1.2,Adequação da complexidade ciclomática,"76,6%",11,47,Aceitável,c2ae570,2026-11-18 12:04 -0300
M3.2.1,Conformidade de estilo PEP 8,"5,3%",2,38,Insatisfatório,c2ae570,2026-11-18 12:04 -0300
M3.2.2,Densidade de código duplicado,"0,15%",28,18927,Excelente,c2ae570,2026-11-18 12:04 -0300
M3.2.3,Completude de logs do sistema,"0,0%",0,33,Insatisfatório,c2ae570,2026-11-18 12:04 -0300
M3.3.1,Completude de testes automatizados,"63,17%",4750,7519,Aceitável,c2ae570,2026-11-18 12:04 -0300

```

## Ambiente (`ambiente.txt`)

```text
data_coleta=2026-11-18 12:04 -0300
commit_vicky=c2ae5704b9770fbc33156fb3f457c4e8c63e5007
data_commit=2026-09-29 20:51:15 -0300
so=Linux 7.0.0-43-generic x86_64
uv=uv 0.13.9 (x86_64-unknown-linux-gnu)
python=Python 3.12.16
radon=6.0.1
flake8=7.5.0 (mccabe: 0.7.0, pycodestyle: 2.15.0, pyflakes: 4.1.0, radon: 6.0.1)
pylint=pylint 4.1.4
pytest=pytest 9.2.0
pytest-cov=7.1.0
coverage=7.17.3
```

## Comparação com a coleta registrada

A comparação via `git diff dados/avaliacao/G3/resultados.csv` confirmou que as colunas `metrica`, `nome`, `valor`, `A`, `B`, `nivel` e `commit` são idênticas às da coleta registrada por A1 (14/11/2026 21:00) nas seis métricas; apenas `data_coleta` difere (`2026-11-18 12:04 -0300`).

Nas saídas brutas, as diferenças observadas correspondem apenas ao esperado entre ambientes distintos: data/hora, sistema operacional, tempo de execução dos testes, caminhos temporários e ordem de listagem dos arquivos em `radon-raw.txt`. A coleta do G3 está, portanto, confirmada.