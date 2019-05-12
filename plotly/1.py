import plotly.plotly as py
from plotly.offline import iplot , plot as offpy
fig = py.get_figure('https://plot.ly/~jackp/8715', raw=True)
iplot(fig)
print(offpy(fig, filename='33.html', auto_open=True, show_link=False))