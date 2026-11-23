# M3.2.3 - Completude de logs do sistema

Arquivo gerado por `calcular.py` a partir das saídas brutas desta pasta. Não editar à mão.

| Campo | Valor |
|-------|-------|
| Data da coleta | 2026-11-23 12:23 -0300 |
| Commit avaliado | `7e9ccd81a49693d4f811ae074200de4884f4afe8` (2026-11-23 12:17:43 -0300) |
| Valor | 100,0% |
| A | 43 |
| B | 43 |
| Nível pela Fase 2 | Excelente |

## Contagens

- Funções e métodos de `pipeline.py` inventariados: 69
- B (funções críticas pela regra do método): 43
- A (funções críticas com chamada à biblioteca `logging`): 43
- `import logging` ou `getLogger` em `src/vicky/`: 2 ocorrências
- Informativo, fora da fórmula: funções críticas com `print` ou `traceback.print_exc`: 0; com registro de status em `job` no banco: 16
