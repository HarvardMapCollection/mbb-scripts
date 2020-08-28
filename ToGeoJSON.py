import pandas as pd
import geopandas

df = pd.read_csv('TestOutput_Double_Escape',encoding='utf-8-sig')

gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df['LONG'], df['LAT']))

gdf.to_file("TestOutput_Double_Escape.geojson", driver='GeoJSON')