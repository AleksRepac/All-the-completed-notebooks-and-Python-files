import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# ✅ Load dataset
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
df = pd.read_csv(URL)
df["Year"] = df["Year"].astype(int)  # Ensure Year is integer
df["Vehicle_Type"] = df["Vehicle_Type"].astype(str)  # Ensure Vehicle_Type is string
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

    # Output container
    html.Div([
        dcc.Graph(id="sales-trend-graph", className="graph"),
        dcc.Graph(id="economic-indicators-graph", className="graph")
    ], id="output-container", className="charts-container")
])


# ✅ Define callback to update graphs
@app.callback(
    [Output("sales-trend-graph", "figure"),
     Output("economic-indicators-graph", "figure")],
    [Input("year-dropdown", "value"),
     Input("vehicle-dropdown", "value")]
)
def update_graph(selected_year, selected_vehicle):
    # Filter data
    filtered_df = df[(df["Year"] == selected_year) & (df["Vehicle_Type"] == selected_vehicle)]
    
    # Sales Trend Graph
    if not filtered_df.empty:
        sales_fig = px.line(
            filtered_df,
            x="Month",
            y="Automobile_Sales",
            title=f"Sales Trend for {selected_vehicle} in {selected_year}",
            labels={"Month": "Month", "Automobile_Sales": "Sales"}
        )
    else:
        sales_fig = px.line(title="No Data Available for the Selected Filters")

    # Economic Indicators Graph
    if not filtered_df.empty:
        economic_fig = px.line(
            filtered_df,
            x="Month",
            y=["Consumer_Confidence", "GDP"],
            title=f"Economic Indicators for {selected_year}",
            labels={"Month": "Month", "value": "Index"},
        )
    else:
        economic_fig = px.line(title="No Data Available for the Selected Filters")

    return sales_fig, economic_fig


# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)