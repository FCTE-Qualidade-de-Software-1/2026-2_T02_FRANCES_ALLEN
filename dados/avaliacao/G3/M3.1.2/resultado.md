# M3.1.2 - Adequação da complexidade ciclomática

Arquivo gerado por `calcular.py` a partir das saídas brutas desta pasta. Não editar à mão.

| Campo | Valor |
|-------|-------|
| Data da coleta | 2026-11-14 21:00 -0300 |
| Commit avaliado | `c2ae5704b9770fbc33156fb3f457c4e8c63e5007` (2026-09-29 20:51:15 -0300) |
| Valor | 76,6% |
| A | 11 |
| B | 47 |
| Nível pela Fase 2 | Aceitável |

## Contagens

- A (funções e métodos com CC > 10, notas C a F): 11
- B (funções e métodos de `pipeline.py`; a linha de classe do radon não entra): 47
- Funções acima do limiar: `run_full_pipeline` (84, F), `_step_rotate_terms` (45, F), `_build_expansion_queries` (40, E), `_step_verify_bloqueante` (38, E), `_step_search` (31, E), `_step_analyze` (17, C), `_extract_english_keyword_groups` (16, C), `_step_discovery` (13, C), `_step_double_check` (13, C), `run_discovery_only` (13, C), `is_pipeline_zombie` (11, C)
