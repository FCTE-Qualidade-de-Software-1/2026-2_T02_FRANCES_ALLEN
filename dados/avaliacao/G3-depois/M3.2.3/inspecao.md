# M3.2.3 - Inspeção do inventário de funções

Ficha da inspeção da seção 4.6 do [Método do G3](../../../../docs/fase-3/metodo-g3.md). Criada por `extrair.py ficha` a partir de `funcoes.csv` e nunca sobrescrita pelo script. Cada avaliador preenche só a própria coluna com `ok` ou com o erro encontrado (crítica indevida, crítica não marcada, chamada a `logging` não contada, crítica sem registro de sucesso e de exceção), sem ver a coluna do outro. Uma crítica só entra em A se registrar em `logging` o sucesso e a exceção, como pede a ficha.

| Avaliador | Data | Sistema |
|-----------|------|---------|
| A1 | | |
| A2 | | |

| Função | Linha | Crítica no inventário | Chamadas a `logging` | A1 | A2 | consenso | decidido_por |
|--------|------:|:---------------------:|:--------------------:|----|----|----------|--------------|
| `_reconcile_real_cost` | 44 | sim | 3 | | | | |
| `_schedule_reconcile` | 68 | não | 1 | | | | |
| `_min_required_for` | 147 | não | 0 | | | | |
| `_init_loop_state` | 204 | não | 1 | | | | |
| `_load_run_context` | 243 | sim | 2 | | | | |
| `_run_initial_phases` | 258 | sim | 2 | | | | |
| `_reroll_budget_left` | 280 | não | 0 | | | | |
| `_stagnation_reroll` | 288 | sim | 3 | | | | |
| `_stagnation_expand_window` | 327 | sim | 2 | | | | |
| `_handle_stagnation` | 361 | não | 1 | | | | |
| `_stop_action` | 380 | não | 3 | | | | |
| `_refresh_string_stats` | 403 | sim | 1 | | | | |
| `_analyze_pending` | 413 | sim | 1 | | | | |
| `_safe_rebalance` | 460 | não | 1 | | | | |
| `_research_expanded_sources` | 470 | sim | 1 | | | | |
| `_needs_rotate` | 483 | sim | 1 | | | | |
| `_reroll_for_ratio` | 501 | sim | 2 | | | | |
| `_ratio_check_due` | 523 | não | 0 | | | | |
| `_ratio_is_low` | 529 | não | 0 | | | | |
| `_rebalance_and_react` | 537 | não | 1 | | | | |
| `_check_inclusion_ratio` | 554 | não | 0 | | | | |
| `_expand_collection` | 571 | sim | 2 | | | | |
| `_update_stagnation` | 610 | não | 1 | | | | |
| `_log_final_invariants` | 638 | não | 2 | | | | |
| `_run_main_loop` | 659 | não | 0 | | | | |
| `run_full_pipeline` | 693 | sim | 6 | | | | |
| `_project_counts` | 760 | sim | 1 | | | | |
| `_restore_pipeline_counters` | 790 | sim | 2 | | | | |
| `_pending_count` | 836 | sim | 1 | | | | |
| `_api_key_for_project` | 857 | sim | 3 | | | | |
| `_step_discovery` | 873 | sim | 4 | | | | |
| `_step_search` | 938 | sim | 6 | | | | |
| `_build_strategies` | 1106 | não | 0 | | | | |
| `_relax_query` | 1124 | não | 0 | | | | |
| `_raw_topic_query` | 1147 | não | 0 | | | | |
| `_step_expand_search` | 1171 | sim | 3 | | | | |
| `_extract_english_keyword_groups` | 1237 | não | 0 | | | | |
| `_extract_english_keywords` | 1301 | não | 0 | | | | |
| `_build_expansion_queries` | 1310 | não | 0 | | | | |
| `_normalize_title_for_dedup` | 1422 | não | 0 | | | | |
| `_step_dedup` | 1463 | sim | 2 | | | | |
| `_step_dedup_bloqueante` | 1473 | sim | 2 | | | | |
| `_step_analyze` | 1547 | sim | 1 | | | | |
| `_step_double_check` | 1658 | sim | 1 | | | | |
| `_step_expand_years_window` | 1753 | sim | 2 | | | | |
| `rebalance_search_strings` | 1811 | sim | 2 | | | | |
| `_step_rotate_terms` | 1879 | sim | 2 | | | | |
| `recalcular_top_n` | 2059 | sim | 2 | | | | |
| `_step_finalize` | 2113 | sim | 2 | | | | |
| `_step_finalize_bloqueante` | 2123 | sim | 2 | | | | |
| `_step_verify` | 2152 | sim | 2 | | | | |
| `_step_verify_bloqueante` | 2167 | sim | 3 | | | | |
| `_create_job` | 2412 | sim | 2 | | | | |
| `_job_update` | 2423 | sim | 2 | | | | |
| `_job_done` | 2433 | sim | 2 | | | | |
| `_job_fail` | 2444 | sim | 2 | | | | |
| `_fail_project` | 2455 | sim | 2 | | | | |
| `_close_orphan_jobs` | 2465 | sim | 2 | | | | |
| `is_pipeline_zombie` | 2494 | sim | 4 | | | | |
| `reset_zombie_pipeline` | 2554 | sim | 2 | | | | |
| `resume_interrupted_pipelines` | 2571 | sim | 2 | | | | |
| `set_main_loop` | 2610 | não | 0 | | | | |
| `is_cancelled` | 2626 | não | 0 | | | | |
| `check_cancelled` | 2630 | não | 0 | | | | |
| `request_cancel` | 2637 | não | 0 | | | | |
| `_track_pipeline` | 2651 | não | 0 | | | | |
| `run_discovery_only` | 2662 | sim | 4 | | | | |
| `schedule_discovery_only` | 2720 | sim | 2 | | | | |
| `schedule_pipeline` | 2741 | sim | 2 | | | | |
