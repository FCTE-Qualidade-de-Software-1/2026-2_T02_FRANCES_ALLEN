# M3.2.3 - Inspeção do inventário de funções

Ficha da inspeção da seção 4.6 do [Método do G3](../../../../docs/fase-3/metodo-g3.md). Criada por `extrair.py ficha` a partir de `funcoes.csv` e nunca sobrescrita pelo script. Cada avaliador preenche só a própria coluna com `ok` ou com o erro encontrado (crítica indevida, crítica não marcada, chamada a `logging` não contada, crítica sem registro de sucesso e de exceção), sem ver a coluna do outro. Uma crítica só entra em A se registrar em `logging` o sucesso e a exceção, como pede a ficha.

| Avaliador | Data | Sistema |
|-----------|------|---------|
| A1 | | |
| A2 | 18/11/2026 | Linux Ubuntu |

| Função | Linha | Crítica no inventário | Chamadas a `logging` | A1 | A2 | consenso | decidido_por |
|--------|------:|:---------------------:|:--------------------:|----|----|----------|--------------|
| `_reconcile_real_cost` | 41 | sim | 0 | | ok | | |
| `_schedule_reconcile` | 63 | não | 0 | | ok | | |
| `_min_required_for` | 142 | não | 0 | | ok | | |
| `run_full_pipeline` | 165 | sim | 0 | | ok | | |
| `_project_counts` | 571 | sim | 0 | | ok | | |
| `_restore_pipeline_counters` | 599 | sim | 0 | | ok | | |
| `_pending_count` | 641 | sim | 0 | | ok | | |
| `_api_key_for_project` | 660 | sim | 0 | | ok | | |
| `_step_discovery` | 673 | sim | 0 | | ok | | |
| `_step_search` | 734 | sim | 0 | | ok | | |
| `_build_strategies` | 893 | não | 0 | | ok | | |
| `_relax_query` | 911 | não | 0 | | ok | | |
| `_raw_topic_query` | 934 | não | 0 | | ok | | |
| `_step_expand_search` | 958 | sim | 0 | | ok | | |
| `_extract_english_keyword_groups` | 1019 | não | 0 | | ok | | |
| `_extract_english_keywords` | 1083 | não | 0 | | ok | | |
| `_build_expansion_queries` | 1092 | não | 0 | | ok | | |
| `_normalize_title_for_dedup` | 1204 | não | 0 | | ok | | |
| `_step_dedup` | 1245 | sim | 0 | | ok | | |
| `_step_dedup_bloqueante` | 1250 | sim | 0 | | ok | | |
| `_step_analyze` | 1322 | sim | 0 | | ok | | |
| `_step_double_check` | 1433 | sim | 0 | | ok | | |
| `_step_expand_years_window` | 1528 | sim | 0 | | ok | | |
| `rebalance_search_strings` | 1583 | sim | 0 | | ok | | |
| `_step_rotate_terms` | 1646 | sim | 0 | | ok | | |
| `recalcular_top_n` | 1824 | sim | 0 | | ok | | |
| `_step_finalize` | 1872 | sim | 0 | | ok | | |
| `_step_finalize_bloqueante` | 1877 | sim | 0 | | ok | | |
| `_step_verify` | 1903 | sim | 0 | | ok | | |
| `_step_verify_bloqueante` | 1913 | sim | 0 | | ok | | |
| `_create_job` | 2155 | sim | 0 | | ok | | |
| `_job_update` | 2160 | sim | 0 | | ok | | |
| `_job_done` | 2165 | sim | 0 | | ok | | |
| `_job_fail` | 2171 | sim | 0 | | ok | | |
| `_fail_project` | 2177 | sim | 0 | | ok | | |
| `_close_orphan_jobs` | 2182 | sim | 0 | | ok | | |
| `is_pipeline_zombie` | 2206 | sim | 0 | | ok | | |
| `reset_zombie_pipeline` | 2258 | sim | 0 | | ok | | |
| `resume_interrupted_pipelines` | 2273 | sim | 0 | | ok | | |
| `set_main_loop` | 2312 | não | 0 | | ok | | |
| `is_cancelled` | 2328 | não | 0 | | ok | | |
| `check_cancelled` | 2332 | não | 0 | | ok | | |
| `request_cancel` | 2339 | não | 0 | | ok | | |
| `_track_pipeline` | 2353 | não | 0 | | ok | | |
| `run_discovery_only` | 2364 | sim | 0 | | ok | | |
| `schedule_discovery_only` | 2418 | sim | 0 | | ok | | |
| `schedule_pipeline` | 2437 | sim | 0 | | ok | | |
