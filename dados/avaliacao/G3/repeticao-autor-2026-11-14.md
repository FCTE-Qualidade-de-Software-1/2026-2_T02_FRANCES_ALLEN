# G3: repetição da coleta pelo autor (14/11/2026)

Segunda execução do `coletar.sh` sobre o commit `c2ae570`, feita pelo autor da primeira coleta na mesma máquina, com ambientes novos e outra pasta de trabalho. Não substitui a repetição independente por A2 em outra máquina, pedida na seção 7 do [Método do G3](../../../docs/fase-3/metodo-g3.md); essa repetição será registrada em `repeticao.md`.

As saídas brutas desta segunda execução não foram mantidas no repositório, para que fique uma única coleta (a de 21:00). Ficam aqui a saída do script, o `resultados.csv` e as versões do ambiente. Os caminhos locais de pasta foram omitidos.

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

## resultados.csv da segunda execução

```text
metrica,nome,valor,A,B,nivel,commit,data_coleta
M3.1.1,Acoplamento de componentes,"2,05",78,38,Excelente,c2ae570,2026-11-14 21:03 -0300
M3.1.2,Adequação da complexidade ciclomática,"76,6%",11,47,Aceitável,c2ae570,2026-11-14 21:03 -0300
M3.2.1,Conformidade de estilo PEP 8,"5,3%",2,38,Insatisfatório,c2ae570,2026-11-14 21:03 -0300
M3.2.2,Densidade de código duplicado,"0,15%",28,18927,Excelente,c2ae570,2026-11-14 21:03 -0300
M3.2.3,Completude de logs do sistema,"0,0%",0,33,Insatisfatório,c2ae570,2026-11-14 21:03 -0300
M3.3.1,Completude de testes automatizados,"63,17%",4750,7519,Aceitável,c2ae570,2026-11-14 21:03 -0300
```

## Ambiente (`ambiente.txt`)

```text
data_coleta=2026-11-14 21:03 -0300
commit_vicky=c2ae5704b9770fbc33156fb3f457c4e8c63e5007
data_commit=2026-09-29 20:51:15 -0300
so=Darwin 25.6.0 arm64
macos=26.6.2
uv=uv 0.12.5 (210d1f678 2026-08-14 aarch64-apple-darwin)
python=Python 3.12.13
radon=6.0.1
flake8=7.5.0 (mccabe: 0.7.0, pycodestyle: 2.15.0, pyflakes: 4.1.0, radon: 6.0.1)
pylint=pylint 4.1.4
pytest=pytest 9.2.0
pytest-cov=7.1.0
coverage=7.17.3
```

## Comparação com a coleta registrada

As colunas `metrica`, `nome`, `valor`, `A`, `B` e `nivel` são iguais às de `resultados.csv` (coleta de 14/11/2026 21:00) nas seis métricas; só `data_coleta` difere (21:03).
