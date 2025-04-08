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

# ✅ Get unique years & vehicle types
years = sorted(df["Year"].unique())
vehicle_types = df["Vehicle_Type"].unique()

# ✅ Initialize Dash App
app = dash.Dash(__name__)
app.title = "Automobile Sales Dashboard"

# ✅ Define Layout
app.layout = html.Div(children=[
    html.H1("Automobile Sales Dashboard", style={'textAlign': 'center'}),

    # 🔹 Year Dropdown
    html.Label("Select Year:"),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': str(year), 'value': year} for year in years],
        value=years[0],  # Default selection
        clearable=False
    ),

    # 🔹 Vehicle Type Dropdown
    html.Label("Select Vehicle Type:"),
    dcc.Dropdown(
        id='vehicle-dropdown',
        options=[{'label': v, 'value': v} for v in vehicle_types],
        value=vehicle_types[0],  # Default selection
        clearable=False
    ),

    # 🔹 Output Graph
    dcc.Graph(id='sales-graph')
])

# ✅ Define Callback to Update Graph
@app.callback(
    Output('sales-graph', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('vehicle-dropdown', 'value')]
)
def update_graph(selected_year, selected_vehicle):
    print("🔹 Callback Triggered!")  # Debug print
    print(f"🔹 Selected Year: {selected_year}, Selected Vehicle: {selected_vehicle}")

    # ✅ Filter dataframe based on selection
    filtered_df = df[(df["Year"] == selected_year) & (df["Vehicle_Type"] == selected_vehicle)]
    print(f"🔹 Filtered Data:\n{filtered_df.head()}")  # Check the first few rows

    # ✅ Handle case where no data is available
    if filtered_df.empty:
        return px.scatter(title="No Data Available for Selected Filters")

    # ✅ Create line chart
    fig = px.line(filtered_df, x="Month", y="Automobile_Sales",
                  title=f"Sales Trend for {selected_vehicle} in {selected_year}",
                  labels={"Automobile_Sales": "Sales", "Month": "Month"})
    return fig

# ✅ Run the App
if __name__ == '__main__':
    app.run_server(debug=True)



