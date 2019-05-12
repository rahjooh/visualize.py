import plotly.plotly as py
import pandas as pd
from plotly.offline import plot as offpy
import plotly.graph_objs as go
trace = go.Heatmap(name= '1st Trace',
                       z=[1,2,3],
                       x=[4,5,6],
                       y=[7,8,9],
                       colorscale='Jet',


    )
data = [trace]
layout = dict(title='asdasdasdasd',yaxis=dict(title='yyyyyyyy',tickmode="array"),xaxis=dict(title='xxxxxxxxxxxx',tickmode="array"))
fig = go.Figure(data=data, layout=layout)
offpy(fig, show_link=False, include_plotlyjs=True,filename='d3-world-map.html')
#
#
# import plotly.figure_factory as ff
# df = pd.read_excel("1.xlsx", names = ['Country', 'Share'],skiprows = [0])
# df['Share'] = pd.Series(["{0:.1}%".format(val * 100) for val in df['Share']], index = df.index)
# data = [ dict(
#         type = 'choropleth',
#         locations = df['Country'],
#         z = df['Share'],
#         text = df['Country'],
#         colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
#             [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
#         autocolorscale = False,
#         reversescale = True,
#         marker = dict(
#             line = dict (
#                 color = 'rgb(180,180,180)',
#                 width = 0.5
#             ) ),
#         colorbar = dict(
#             autotick = False,
#             tickprefix = '$',
#             title = 'тест'),
#       ) ]
#
# layout = dict(
#     title = 'Доля низкоуглеродной электрогенерации в мировом энергобалансе',
#     geo = dict(
#         showframe = False,
#         showcoastlines = False,
#         projection = dict(
#             type = 'Mercator'
#         )
#     )
# )
#
# fig = dict( data=data, layout=layout )
# py.iplot( fig, validate=False, filename='d3-world-map' )