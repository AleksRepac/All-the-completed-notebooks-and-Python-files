import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# ✅ Load dataset
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
df = pd.read_csv(URL)

# Ensure correct data types
df["Year"] = df["Year"].astype(int)  
df["Vehicle_Type"] = df["Vehicle_Type"].astype(str)  

# Filter recession data
recession_df = df[df["Recession"] == 1]  # Only rows where Recession = 1

# Initialize Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([
    html.H1("Recession Report Statistics", style={'textAlign': 'center', 'color': 'blue'}),

    # Dropdown for Year selection
    html.Label("Select Year:"),
    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": str(y), "value": y} for y in sorted(recession_df["Year"].unique())],
        value=recession_df["Year"].unique()[0],  # Default to first recession year
        placeholder="Select Year"
    ),

    # Output Container for Graphs
    html.Div([
        dcc.Graph(id="recession-sales-graph", className="graph"),
        dcc.Graph(id="recession-indicators-graph", className="graph")
    ], id="output-container", className="charts-container")
])


# ✅ Define Callback for Updating Graphs
@app.callback(
    [Output("recession-sales-graph", "figure"),
     Output("recession-indicators-graph", "figure")],
    [Input("year-dropdown", "value")]
)
def update_recession_graph(selected_year):
    # Filter data for selected year
    filtered_recession = recession_df[recession_df["Year"] == selected_year]
    
    # Graph 1: Sales During Recession
    if not filtered_recession.empty:
        sales_fig = px.line(
            filtered_recession,
            x="Month",
            y="Automobile_Sales",
            title=f"Automobile Sales During Recession ({selected_year})",
            labels={"Month": "Month", "Automobile_Sales": "Sales"}
        )
    else:
        sales_fig = px.line(title="No Recession Data Available")

    # Graph 2: Recession Indicators (GDP & Consumer Confidence)
    if not filtered_recession.empty:
        indicators_fig = px.line(
            filtered_recession,
            x="Month",
            y=["Consumer_Confidence", "GDP"],
            title=f"Recession Indicators for {selected_year}",
            labels={"Month": "Month", "value": "Index"},
        )
    else:
        indicators_fig = px.line(title="No Recession Data Available")

    return sales_fig, indicators_fig


# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)