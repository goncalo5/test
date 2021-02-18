import stats


max_cp_leagues = {
    "great": 1500,
    "ultra": 2500
}

def get_max_stats_product(pokemon="", league="great"):
    print(league, max_cp_leagues[league])
    _max = 0
    best_ivs = (-1,-1,-1)
    for double_level in range(1, 51*2):
        level = double_level / 2
        cp_min_ivs = stats.calc_cp(pokemon, level, (0, 0, 0))
        cp_max_ivs = stats.calc_cp(pokemon, level, (15, 15, 15))
        if cp_min_ivs > max_cp_leagues[league]:
            continue
        if cp_max_ivs < max_cp_leagues[league]:
            continue
        print(level, cp_min_ivs, cp_max_ivs)
        for atk_iv in range(16):
            for def_iv in range(16):
                for sta_iv in range(16):
                    ivs = (atk_iv, def_iv, sta_iv)
                    if stats.calc_cp(pokemon, level, ivs) > max_cp_leagues[league]:
                        continue
                    stats_product = stats.calc_stats_product(pokemon, level, ivs)
                    if stats_product >= _max:
                        _max = stats_product
                        best_ivs = ivs
                        print(best_ivs)
    return _max