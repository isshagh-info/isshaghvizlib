from isshaghvizlib.election_map.loader import load_adm, load_results
from isshaghvizlib.election_map.process import merge_shapes_results
from isshaghvizlib.election_map.bokeh_map import create_election_map

# Choose administrative level
ADM_LEVEL = "adm2"

# Load data
gdf = load_adm(ADM_LEVEL)
results = load_results()

# Merge
merged = merge_shapes_results(gdf, results, ADM_LEVEL)

# Create map
create_election_map(
    merged,
    value_column="turnout",
    title="Election Turnout by Moughataa (Mauritania)",
    output_html="election_map.html"
)
