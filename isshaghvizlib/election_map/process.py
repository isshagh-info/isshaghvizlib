def compute_turnout(gdf, results_df, level="adm2"):
    """
    Compute turnout and merge with administrative boundaries
    """

    results = results_df.copy()
    results["turnout"] = (
        results["nb_votes"] / results["registered_voters"]
    ) * 100

    # Mapping admin level → join keys
    level_map = {
        "adm1": ("ADM1_EN", "wilaya"),
        "adm2": ("ADM2_EN", "moughataa"),
        "adm3": ("ADM3_EN", "commune"),
    }

    geo_col, res_col = level_map[level]

    # Aggregate turnout
    turnout_agg = (
        results.groupby(res_col, as_index=False)
        .agg({"turnout": "mean"})
    )

    # Normalize text (VERY IMPORTANT)
    turnout_agg[res_col] = (
        turnout_agg[res_col].str.upper().str.strip()
    )
    gdf[geo_col] = gdf[geo_col].str.upper().str.strip()

    merged = gdf.merge(
        turnout_agg,
        left_on=geo_col,
        right_on=res_col,
        how="left"
    )

    return merged
