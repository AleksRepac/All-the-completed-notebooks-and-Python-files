import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update
import datetime as dt
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
df =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv')
df['Month'] = pd.to_datetime(df['Date']).dt.month_name() #used for the names of the months
df['Year'] = pd.to_datetime(df['Date']).dt.year
app.layout = html.Div(children=[html.H1("Wildfire Data Dashboard", style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
                                html.Div([html.Div([html.H2("Select the year", style={'margin-right': '2em'})])
                                ,dcc.Dropdown(id='dropdown-year', multi=False, clearable=False, value=2016, options=[{'label': x, 'value': x} for x in sorted(df['Year'].unique())], style={'width': '50%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'}),]),
@app.callback(Output('wildfire-activity', 'figure'), [Input('dropdown-year', 'value')]))
def update_graph(selected_year):
    filtered_df = df[df['Year'] == selected_year]
    fig = px.scatter(filtered_df, x='Date', y='Estimated_fire_area', color='Month', size='Estimated_fire_area', hover_data=['Date', 'Estimated_fire_area'], title='Estimated Fire Area Over Time')
    fig.update_layout(title='Estimated Fire Area Over Time', xaxis_title='Date', yaxis_title='Estimated Fire Area', title_x=0.5)
    return fig
if __name__ == '__main__':
    app.run_server(debug=True)
app.run_server()

                                