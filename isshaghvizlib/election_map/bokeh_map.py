from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, HoverTool, LinearColorMapper, ColorBar
from bokeh.palettes import Blues
from bokeh.io import output_notebook


def create_election_map(gdf, value_column="turnout", title="Election Turnout"):
    output_notebook()

    # Remove datetime columns (JSON fix)
    gdf_clean = gdf.copy()
    for col in gdf_clean.columns:
        if gdf_clean[col].dtype.name.startswith("datetime"):
            gdf_clean = gdf_clean.drop(columns=[col])

    # Detect admin level
    hover_map = {
        "ADM1_EN": "wilaya",
        "ADM2_EN": "moughataa",
        "ADM3_EN": "commune",
    }

    area_field = None
    area_label = None
    for col, label in hover_map.items():
        if col in gdf_clean.columns:
            area_field = col
            area_label = label
            break

    geo_source = GeoJSONDataSource(
        geojson=gdf_clean.to_json()
    )

    color_mapper = LinearColorMapper(
        palette=Blues[8],
        low=gdf_clean[value_column].min(),
        high=gdf_clean[value_column].max()
    )

    p = figure(
        title=title,
        tools="pan,wheel_zoom,reset",
        x_axis_location=None,
        y_axis_location=None
    )

    p.grid.grid_line_color = None

    p.patches(
        "xs",
        "ys",
        source=geo_source,
        fill_color={"field": value_column, "transform": color_mapper},
        line_color="white",
        line_width=0.4
    )

    if area_field:
        p.add_tools(
            HoverTool(tooltips=[
                (area_label, f"@{area_field}"),
                ("Turnout (%)", f"@{value_column}{{0.2f}}")
            ])
        )

    p.add_layout(
        ColorBar(color_mapper=color_mapper, label_standoff=8),
        "right"
    )

    return p
