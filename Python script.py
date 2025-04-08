import pandas as pd
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
import dash
from dash.dependencies import Input, Output
import plotly.express as px
airline_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                           encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str,
                                     'Div2Airport': str, 'Div2TailNum': str})
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1()
                                                    
    html.Div(["Input Year: ",
              dcc.Input()],
             style={'font-size': 30}),
    html.Br(),
    html.Br(),
    html.Div([html.Div(),html.Div()]
style={'display': 'flex'}),
html.Div([html.Div(),html.Div()]),
style={'display': 'flex'}),
html.Div(, style={'width': '65%'})])
html.H!('Flight Delay Time Statistics', style={'textAlign': 'center', 'font-size': 30}),
html.Div(['Input Year: ', dcc.Input(id='input-year', value='2010', type='number', style={'height': '50px', 'font-size': 30})], style={'font-size': 30}),
html.Div([html.Div([dcc.Graph(id='carrier-plot')], style={'width': '49%', 'display': 'inline-block'}),
html.Div([dcc.Graph(id='weather-plot')], style={'width': '49%', 'display': 'inline-block'})], style={'display': 'flex'}),
def compute_info(year, carrier_name):
    carrier_info = airline_data[airline_data['Year'] == year]
    avg_carrier_delay = carrier_info.groupby(['UniqueCarrier'])['CarrierDelay'].mean().reset_index()
    avg_weather_delay = carrier_info.groupby(['UniqueCarrier'])['WeatherDelay'].mean().reset_index()
    return avg_carrier_delay, avg_weather_delay
@app.callback([Output('carrier-plot', 'figure'),
                Output('weather-plot', 'figure')],
                  [Input('input-year', 'value')])
def update_graph(year):
    carrier_info = airline_data[airline_data['Year'] == year]
    avg_carrier_delay = carrier_info.groupby(['UniqueCarrier'])['CarrierDelay'].mean().reset_index()
    avg_weather_delay = carrier_info.groupby(['UniqueCarrier'])['WeatherDelay'].mean().reset_index()
    fig1 = px.bar(avg_carrier_delay, x='UniqueCarrier', y='CarrierDelay', title='Average carrier delay time for different carriers')
    fig2 = px.bar(avg_weather_delay, x='UniqueCarrier', y='WeatherDelay', title='Average weather delay time for different carriers')
    return fig1, fig2
if __name__ == '__main__':