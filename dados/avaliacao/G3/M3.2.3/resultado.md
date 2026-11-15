# M3.2.3 - Completude de logs do sistema

Arquivo gerado por `calcular.py` a partir das saídas brutas desta pasta. Não editar à mão.

| Campo | Valor |
|-------|-------|
| Data da coleta | 2026-11-14 21:00 -0300 |
| Commit avaliado | `c2ae5704b9770fbc33156fb3f457c4e8c63e5007` (2026-09-29 20:51:15 -0300) |
| Valor | 0,0% |
| A | 0 |
| B | 33 |
| Nível pela Fase 2 | Insatisfatório |

## Contagens

- Funções e métodos de `pipeline.py` inventariados: 47
- B (funções críticas pela regra do método): 33
- A (funções críticas com chamada à biblioteca `logging`): 0
- `import logging` ou `getLogger` em `src/vicky/`: nenhuma ocorrência
- Informativo, fora da fórmula: funções críticas com `print` ou `traceback.print_exc`: 7; com registro de status em `job` no banco: 15
