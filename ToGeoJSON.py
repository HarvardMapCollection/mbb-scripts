import pandas as pd
import geopandas

df = pd.read_csv('/Users/daveweimer/Desktop/WFH/BlackBoston/2020-08-23-TestOutput.csv',encoding='utf-8-sig')

gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df['LONG'], df['LAT']))

gdf.to_file("/Users/daveweimer/Desktop/WFH/BlackBoston/2020-08-23-TestOutput.geojson", driver='GeoJSON')