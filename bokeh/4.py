
import os
import pandas as pd
from bokeh.io import show,output_file
from bokeh.models import (GMapPlot , GMapOptions , ColumnDataSource , Circle , DataRange1d, PanTool , WheelZoomTool , BoxSelectTool)
from googlemaps import Client as GoogleMaps
os.environ.get("foo")
df0 = pd.read_csv('ccc.csv')
df=df0
print(df0)
map_options = GMapOptions(lat = 35.6892 , lng=51.3890  , map_type='roadmap',zoom=6)
api_key =os.environ.get('API_KEY')
api_key='AIzaSyCvllwPPFlcF6SF8e2WJBhErb9IYOuqUyk'

plot = GMapPlot(x_range=DataRange1d(),y_range=DataRange1d() , map_options=map_options , api_key=api_key)
# plot.add_tools(PanTool(),WheelZoomTool(),BoxSelectTool())

baseline = df['count'].min() - 1.0
scale = 2.5
print(type(df['lat']))
source = ColumnDataSource(data=dict(lat = df['lat'].values.tolist() ,
                                    lon= df['lon'].values.tolist(),
                                    rad = [(i-baseline) for i in df['count'].values.tolist()]))

circle = Circle(x="lon", y="lat",size="rad",fill_color='blue',fill_alpha=0.3)

plot.add_glyph(source,circle)
output_file('Iran.html')
show(plot)