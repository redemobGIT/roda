"""
kepler_map.py — Minimal Kepler.gl helper for plotting networks.

Usage (inside scripts/ notebook):

    import sys, os
    sys.path.append(os.path.abspath(".."))  # add parent folder to sys.path

    import kepler_map

    metric = "cc_betweenness_10000_ang"
    kmap = kepler_map.make_map(weighted_nodes_gdf, metric)
    kmap  # display

    # Optionally save:
    kepler_map.save_map_html(kmap, "network_kepler.html", read_only=False)
"""

import json
from typing import Iterable, Optional
import geopandas as gpd
from keplergl import KeplerGl


def _to_wgs84_geojson(gdf: gpd.GeoDataFrame) -> dict:
    """Return GeoJSON FeatureCollection in WGS84."""
    if gdf.crs is None:
        raise ValueError("GeoDataFrame must have a CRS to convert to WGS84.")
    gdf_ll = gdf.to_crs(4326) if gdf.crs.to_epsg() != 4326 else gdf
    return json.loads(gdf_ll.to_json())


def _build_default_config(
    metric: str,
    *,
    line_width: float = 1.5,
    color_scale: str = "quantile",
    color_range: str = "Uber Viz Sequential 1",
    map_style: str = "dark",
    tooltip_fields: Optional[Iterable[str]] = None,
    data_id: str = "edges",
) -> dict:
    """Return a minimal Kepler config for a line layer colored by `metric`."""
    tooltip_cfg = {
        "fieldsToShow": {data_id: [{"name": metric, "format": None}]},
        "enabled": True,
    }
    if tooltip_fields:
        extra = [f for f in tooltip_fields if f != metric]
        tooltip_cfg["fieldsToShow"][data_id] = (
            [{"name": metric, "format": None}]
            + [{"name": f, "format": None} for f in extra]
        )

    return {
        "version": "v1",
        "config": {
            "visState": {
                "layers": [
                    {
                        "id": "network-lines",
                        "type": "line",
                        "config": {
                            "dataId": data_id,
                            "label": "Network",
                            "columns": {"geojson": "geometry"},
                            "isVisible": True,
                            "visConfig": {
                                "opacity": 0.9,
                                "thickness": line_width,
                                "colorRange": {"name": color_range},
                            },
                        },
                        "visualChannels": {
                            "colorField": {"name": metric, "type": "real"},
                            "colorScale": color_scale,
                        },
                    }
                ],
                "interactionConfig": {"tooltip": tooltip_cfg},
            },
            "mapStyle": {"styleType": map_style},
        },
    }


def make_map(
    edges_gdf: gpd.GeoDataFrame,
    metric: str,
    *,
    height: int = 700,
    line_width: float = 1.5,
    color_scale: str = "quantile",
    color_range: str = "Uber Viz Sequential 1",
    map_style: str = "dark",
    tooltip_fields: Optional[Iterable[str]] = None,
    config: Optional[dict] = None,
    config_path: Optional[str] = None,
) -> KeplerGl:
    """Create a KeplerGl map for a LineString network colored by `metric`."""
    if metric not in edges_gdf.columns:
        raise KeyError(f"Metric column not found: {metric}")

    data_geojson = _to_wgs84_geojson(edges_gdf)

    if config is None and config_path:
        with open(config_path, "r", encoding="utf-8") as fh:
            config = json.load(fh)
    if config is None:
        config = _build_default_config(
            metric,
            line_width=line_width,
            color_scale=color_scale,
            color_range=color_range,
            map_style=map_style,
            tooltip_fields=tooltip_fields,
        )

    return KeplerGl(height=height, data={"edges": data_geojson}, config=config)


def save_map_html(kmap: KeplerGl, file_name: str, *, read_only: bool = False) -> None:
    """Save a KeplerGl object to a standalone HTML file."""
    kmap.save_to_html(file_name=file_name, read_only=read_only)
