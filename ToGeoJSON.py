import pandas as pd
import geopandas

df = pd.read_csv('Leaflet_TestOutput.csv',encoding='utf-8-sig')

gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df['LONG'], df['LAT']))

gdf.to_file("historical_data.geojson", driver='GeoJSON')