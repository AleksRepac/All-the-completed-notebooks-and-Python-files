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
app=dash.Dash(__name__)
app.title='Automobile Sales'
app.layout=html.Div(children=[
    html.H1('Automobile Sales', style={'textAlign':'center'}),
    html.P('This dataset represents historical automobile sales data. The data is monthly, spanning a period of 10 years, from 2007 to 2017. The data is broken down by month, year, automobile sales, vehicle type, and recession status.'),
    dcc.Graph(figure=px.line(df, x='Month', y='Automobile_Sales', title='Automobile Sales'))
])
if __name__=='__main__':
    app.run_server(debug=True)
app._plotlyjs_url = 'https://cdn.plot.ly/plotly-2.4.2.min.js'
app.run_server(debug=True, use_reloader=False)
# The code above creates a Dash app that displays a line plot of automobile sales data. The data is read from a CSV file and displayed using Plotly Express. The app displays the title 'Automobile Sales' and a brief description of the dataset. The line plot shows the automobile sales data over time.
# To display the result, you can run the script in your terminal or command prompt. 
# Once the script is executed, open a web browser and navigate to the URL provided in the terminal (usually http://127.0.0.1:8050/).
# The Dash app will display the line plot and other components in the browser.
python app.py #ovo sam koristio kako bih pokrenuo aplikaciju u terminalu i proverio da se radi o http://127.0.0.1:8050/
