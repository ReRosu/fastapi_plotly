import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

import numpy as np
import pandas as pd

def x2(x):
    return x*x

def get_plot_html(f_x: float, t_x:float, step: float):
    x = np.arange(f_x, t_x, step)
    fig = px.scatter(x=x,y=x2(x))
    return fig.to_html()