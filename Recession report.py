import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import flask
print(flask.__version__)
# Load the dataset
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
df = pd.read_csv(URL)

# ✅ Ensure column names do not have spaces
df.columns = df.columns.str.strip()

# ✅ Filter data for recession years
df_recession = df[df["Recession"] == 1]

# ✅ Define statistics to analyze
recession_stats = {
    "Automobile Sales": "Automobile_Sales",
    "Consumer Confidence Index": "Consumer_Confidence",
    "Advertising Expenditure": "Advertising_Expenditure",
    "Unemployment Rate": "unemployment_rate"
}

# ✅ Initialize Dash app
app = dash.Dash(__name__)

# ✅ Define layout
app.layout = html.Div(children=[
    html.H1("Recession Report Dashboard", style={'textAlign': 'center'}),
    
    # Dropdown for selecting statistics
    html.Label("Select Recession Statistic:"),
    dcc.Dropdown(
        id="stat-dropdown",
        options=[{"label": key, "value": value} for key, value in recession_stats.items()],
        value="Automobile_Sales",
        clearable=False
    ),

    # Graph output
    dcc.Graph(id="recession-graph")
])

# ✅ Callback to update graph based on selected statistic
@app.callback(
    Output("recession-graph", "figure"),
    Input("stat-dropdown", "value")
)
def update_graph(selected_stat):
    fig = px.line(
        df_recession, x="Year", y=selected_stat,
        title=f"Recession Report: {selected_stat}",
        labels={selected_stat: "Value", "Year": "Year"}
    )
    return fig

# ✅ Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
print(f"Selected Year: {selected_year}, Selected Vehicle: {selected_vehicle}")