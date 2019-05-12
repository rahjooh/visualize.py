import os
import pandas as pd
from bokeh.io import show,output_file
from bokeh.models import (GMapPlot , GMapOptions , ColumnDataSource , Circle , DataRange1d, PanTool , WheelZoomTool , BoxSelectTool)
from googlemaps import Client as GoogleMaps
os.environ.get("foo")
df0 = pd.read_csv('ccc.csv')
df1 = df0[['count','lat','lon']].dropna()
df = df0.groupby(('name')).count()
print(df)
df1 =  pd.concat([df1, df], axis=1, join='inner')
print(df1)

df = df1
map_options = GMapOptions(lat = 53.6880 , lng=32.4279  , map_type='roadmap',zoom=3)
api_key =os.environ.get('API_KEY')
api_key='AIzaSyCvllwPPFlcF6SF8e2WJBhErb9IYOuqUyk'

plot = GMapPlot(x_range=DataRange1d(),y_range=DataRange1d() , map_options=map_options , api_key=api_key)
plot.add_tools(PanTool(),WheelZoomTool(),BoxSelectTool())

baseline = df['CityName'].min() - 1.0
scale = 2.5
print(type(df['lat']))
source = ColumnDataSource(data=dict(lat = df['lat'].values.tolist() ,
                                    lon= df['lon'].values.tolist(),
                                    rad = [(i-baseline) for i in df['CityName'].values.tolist()]))

circle = Circle(x="lon", y="lat",size="rad",fill_color='blue',fill_alpha=0.5)

plot.add_glyph(source,circle)
output_file('Iran.html')
show(plot)