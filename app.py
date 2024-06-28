from dash import Dash, html, dcc, callback, Output, Input

import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go


# Load and convert the GeoPackage file
gpkg_path = 'data/Tatorter_1980_2020.gpkg'
gdf = gpd.read_file(gpkg_path, layer='To2020_SR99TM')
gdf = gdf.to_crs(epsg=4326)

# Create the Dash app
app = Dash(__name__)

# Generate the map figure
def create_map():
    fig = go.Figure()

    # Add polygons
    for _, row in gdf.iterrows():
        x, y = row['geometry'].exterior.xy
        fig.add_trace(go.Scattermapbox(
            lon=x,
            lat=y,
            mode='lines',
            fill='toself',
            fillcolor='rgba(0,0,255,0.1)',
            line=dict(color='blue'),
            name=row['TATORT'],
            text=row['TATORT'],
            hoverinfo='text'
        ))

    fig.update_layout(
        mapbox=dict(
            style='open-street-map',
            zoom=5,
            center=dict(lat=62, lon=15)
        ),
        margin=dict(l=0, r=0, t=0, b=0)
    )

    return fig

# Layout of the Dash app
app.layout = html.Div([
    dcc.Graph(id='map', figure=create_map())
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)