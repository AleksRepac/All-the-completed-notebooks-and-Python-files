import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the dataset
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
df = pd.read_csv(URL)

# Extract unique years for dropdown
years = sorted(df["Year"].unique())

# Create a Dash app
app = dash.Dash(__name__)
app.title = "Yearly Report Statistics"

# Layout of the app
app.layout = html.Div([
    html.H1("Yearly Report Statistics", style={'textAlign': 'center'}),

    # Dropdown for selecting year
    html.Label("Select Year:"),
    dcc.Dropdown(
        id="year-dropdown",
        options=[{"label": str(year), "value": year} for year in years],
        value=years[0],  # Default value (first year)
        clearable=False
    ),

    # Graph Output
    dcc.Graph(id="yearly-statistics-graph")
])

# Callback to update graph based on selected year
@app.callback(
    Output("yearly-statistics-graph", "figure"),
    Input("year-dropdown", "value")
)
def update_graph(selected_year):
    # Filter data for the selected year
    df_year = df[df["Year"] == selected_year]

    # Create a bar chart to show statistics for the selected year
    fig = px.bar(
        df_year,
        x="Month",
        y=["Automobile_Sales", "Consumer_Confidence", "unemployment_rate"],
        barmode="group",
        title=f"Yearly Report Statistics for {selected_year}",
        labels={"value": "Statistics", "Month": "Month"},
    )

    return fig

# Run the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)
