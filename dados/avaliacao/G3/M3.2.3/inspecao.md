# M3.2.3 - Inspeção do inventário de funções

Ficha da inspeção da seção 4.6 do [Método do G3](../../../../docs/fase-3/metodo-g3.md). Criada por `extrair.py ficha` a partir de `funcoes.csv` e nunca sobrescrita pelo script. Cada avaliador preenche só a própria coluna com `ok` ou com o erro encontrado (crítica indevida, crítica não marcada, chamada a `logging` não contada), sem ver a coluna do outro.

| Avaliador | Data | Sistema |
|-----------|------|---------|
| A1 | | |
| A2 | | |

| Função | Linha | Crítica no inventário | Chamadas a `logging` | A1 | A2 | consenso | decidido_por |
|--------|------:|:---------------------:|:--------------------:|----|----|----------|--------------|
| `_reconcile_real_cost` | 41 | sim | 0 | | | | |
| `_schedule_reconcile` | 63 | não | 0 | | | | |
| `_min_required_for` | 142 | não | 0 | | | | |
| `run_full_pipeline` | 165 | sim | 0 | | | | |
| `_project_counts` | 571 | sim | 0 | | | | |
| `_restore_pipeline_counters` | 599 | sim | 0 | | | | |
| `_pending_count` | 641 | sim | 0 | | | | |
| `_api_key_for_project` | 660 | sim | 0 | | | | |
| `_step_discovery` | 673 | sim | 0 | | | | |
| `_step_search` | 734 | sim | 0 | | | | |
| `_build_strategies` | 893 | não | 0 | | | | |
| `_relax_query` | 911 | não | 0 | | | | |
| `_raw_topic_query` | 934 | não | 0 | | | | |
| `_step_expand_search` | 958 | sim | 0 | | | | |
| `_extract_english_keyword_groups` | 1019 | não | 0 | | | | |
| `_extract_english_keywords` | 1083 | não | 0 | | | | |
| `_build_expansion_queries` | 1092 | não | 0 | | | | |
| `_normalize_title_for_dedup` | 1204 | não | 0 | | | | |
| `_step_dedup` | 1245 | sim | 0 | | | | |
| `_step_dedup_bloqueante` | 1250 | sim | 0 | | | | |
| `_step_analyze` | 1322 | sim | 0 | | | | |
| `_step_double_check` | 1433 | sim | 0 | | | | |
| `_step_expand_years_window` | 1528 | sim | 0 | | | | |
| `rebalance_search_strings` | 1583 | sim | 0 | | | | |
| `_step_rotate_terms` | 1646 | sim | 0 | | | | |
| `recalcular_top_n` | 1824 | sim | 0 | | | | |
| `_step_finalize` | 1872 | sim | 0 | | | | |
| `_step_finalize_bloqueante` | 1877 | sim | 0 | | | | |
| `_step_verify` | 1903 | sim | 0 | | | | |
| `_step_verify_bloqueante` | 1913 | sim | 0 | | | | |
| `_create_job` | 2155 | sim | 0 | | | | |
| `_job_update` | 2160 | sim | 0 | | | | |
| `_job_done` | 2165 | sim | 0 | | | | |
| `_job_fail` | 2171 | sim | 0 | | | | |
| `_fail_project` | 2177 | sim | 0 | | | | |
| `_close_orphan_jobs` | 2182 | sim | 0 | | | | |
| `is_pipeline_zombie` | 2206 | sim | 0 | | | | |
| `reset_zombie_pipeline` | 2258 | sim | 0 | | | | |
| `resume_interrupted_pipelines` | 2273 | sim | 0 | | | | |
| `set_main_loop` | 2312 | não | 0 | | | | |
| `is_cancelled` | 2328 | não | 0 | | | | |
| `check_cancelled` | 2332 | não | 0 | | | | |
| `request_cancel` | 2339 | não | 0 | | | | |
| `_track_pipeline` | 2353 | não | 0 | | | | |
| `run_discovery_only` | 2364 | sim | 0 | | | | |
| `schedule_discovery_only` | 2418 | sim | 0 | | | | |
| `schedule_pipeline` | 2437 | sim | 0 | | | | |
