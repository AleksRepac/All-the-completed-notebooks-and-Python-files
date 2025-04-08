import numpy as np
import pandas as pd
import matplotlib as plt
import plotly.express as px
import seaborn as sns
import folium
import requests
import json
import os
import datetime
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly
import io
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
df = pd.read_csv(URL)
print(df.head())
print (df.columns)
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import requests
#response=requests.get(URL)
#df = pd.read_csv(io.StringIO(response.text))
#app=dash.Dash(__name__)
#app.layout=html.Div(children=[
    html.H1("Automobile Sales Dashboard", style={'text-align':'center'}),
    html.Label("Select Year:"),
    dcc.Dropdown(
        id='year-dropdown',
                 options=[{'label': str(year), 'value': year} for year in sorted(df['Year'].unique())],
                 value=df['Year'].min(),
                    clearable=False),
    html.Label("Select Vehicle Type:"),
    dcc.Dropdown(
        id='vehicle-dropdown',
                 options=[{'label': vtype, 'value': vtype} for vtype in df['Vehicle_Type'].unique()],
                 value=df['Vehicle_Type'].unique()[0],
                    clearable=False),
    dcc.Graph(id='sales-graph')
])
if __name__=='__main__':
   #app.run_server(debug=True)