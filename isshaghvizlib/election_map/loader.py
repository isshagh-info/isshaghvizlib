from pathlib import Path
import geopandas as gpd
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"


def load_adm(level="adm2"):
    """
    Load administrative boundaries (ADM0–ADM3)
    """
    if level not in ["adm1", "adm2", "adm3"]:
        raise ValueError("level must be adm1, adm2 or adm3")

    shp_path = DATA_DIR / level / f"mrt_admbnda_{level}_ansade_20240327.shp"

    if not shp_path.exists():
        raise FileNotFoundError(f"Shapefile not found: {shp_path}")

    gdf = gpd.read_file(shp_path)
    return gdf.to_crs("EPSG:4326")


def load_results():
    """
    Load election results CSV
    """
    return pd.read_csv(
        DATA_DIR / "results_elections_rim_2019-2024.csv"
    )
