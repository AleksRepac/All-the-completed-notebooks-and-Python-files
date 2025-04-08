import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
# ✅ Load dataset
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
df = pd.read_csv(URL)
print(df.head())
print (df.columns)
df["Year"] = df["Year"].astype(int)  # Ensure Year is integer
df["Vehicle_Type"] = df["Vehicle_Type"].astype(str)
app = dash.Dash(__name__)
year_options = [{"label": str(y), "value": y} for y in sorted(df["Year"].unique())]
vehicle_options = [{"label": v, "value": v} for v in df["Vehicle_Type"].unique()]
app.layout = html.Div([
    html.H1("Automobile Sales Statistics Dashboard", style={'textAlign': 'center', 'color': 'blue'}),

    # Dropdowns
    html.Div([
        html.Label("Year:"),
        dcc.Dropdown(
            id="year-dropdown",
            options=year_options,
            value=df["Year"].unique()[0],  # Default to first year
            placeholder="Select Year"
        ),
        html.Label("Vehicle Type:"),
        dcc.Dropdown(
            id="vehicle-dropdown",
            options=vehicle_options,
            value=df["Vehicle_Type"].unique()[0],  # Default to first vehicle type
            placeholder="Select Vehicle Type"
        )
    ], style={'display': 'flex', 'flexDirection': 'column', 'width': '50%', 'margin': 'auto'}),
    html.Div([
        dcc.Graph(id="sales-trend-graph", className="graph"),
        dcc.Graph(id="economic-indicators-graph", className="graph")
    ], id="output-container", className="charts-container")
])
@app.callback(
    [Output("sales-trend-graph", "figure"),
     Output("economic-indicators-graph", "figure")],
    [Input("year-dropdown", "value"),
     Input("vehicle-dropdown", "value")]
)
def update_graph(selected_year, selected_vehicle):
    # Filter the dataset based on the selected year and vehicle type
    filtered_df = df[(df["Year"] == selected_year) & (df["Vehicle_Type"] == selected_vehicle)]

    # Create the sales trend graph
    sales_trend_fig = px.line(
        filtered_df,
        x="Month",
        y="Sales",
        title="Sales Trend",
        labels={"Month": "Month", "Sales": "Number of Sales"}
    )

    # Create the economic indicators graph
    economic_indicators_fig = px.bar(
        filtered_df,
        x="Month",
        y="Economic_Indicator",
        title="Economic Indicators",
        labels={"Month": "Month", "Economic_Indicator": "Economic Indicator Value"}
    )

    return sales_trend_fig, economic_indicators_fig
if __name__ == '__main__':
    app.run_server(debug=True)