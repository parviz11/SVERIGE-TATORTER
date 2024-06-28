import geopandas as gpd
import pandas as pd
import json
from utils import conversion

import plotly.express as px

# Read data

'''
The data was downloaded from SCB (Statistikmyndigheten),
National Statistics Bureau of Sweden.
Source link: https://www.scb.se/vara-tjanster/oppna-data/oppna-geodata/tatorter/
'''


gpkg_file = 'data/Tatorter_1980_2020.gpkg'

# Load the data
gdf = gpd.read_file(gpkg_file, layer='To2020_SR99TM')

# Instantiate the CoordinateTransformer class
transformer = conversion.CoordinateTransformer()

# Swap the coordinates

''' Swap x an y coordinates to be consistent with
the way that Plotly maps reads the data.'''

gdf['geometry'] = gdf['geometry'].apply(transformer.swap_coordinates)

gdf['geometry'] = gdf['geometry'].apply(transformer.transform_geometry)

''' Swap x an y coordinates to be consistent with
the way that Plotly maps reads the data.'''

gdf['geometry'] = gdf['geometry'].apply(transformer.swap_coordinates)

# Convert to geojson
geojson_data = gdf.to_json()

# Parse the GeoJSON string
geojson_obj = json.loads(geojson_data)

fig = px.choropleth_mapbox(gdf, geojson=geojson_obj, featureidkey='properties.TATORTSKOD',
                           locations='TATORTSKOD', color='BEF',
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 55, "lon": 12},
                           opacity=0.5,
                           labels={'BEF':'Population'},
                           hover_data={'TATORT': True, 'BEF': True, 'TATORTSKOD': False}
                          )

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()