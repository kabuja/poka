import pathlib
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd 

dash.register_page(__name__)

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

df=pd.read_csv(r'C:\Users\felix\Desktop\clien\KingKong\src\data\data2.csv')

layout = html.Div(
    [
        dcc.Dropdown([x for x in df.year.unique()], id='cont-choice', style={'width':'50%'}),
        dcc.Graph(id='line-fig',
                  figure=px.bar(df, x='country', y='population',title='WorldWide Population Distribution Per Year'))
    ]
)
