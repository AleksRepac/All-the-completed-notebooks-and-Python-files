import plotly
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
age_array=np.random.randint(25,55,60)
income_array=np.random.randint(300000,700000,3000000)
fig=go.Figure()
fig
fig.add_trace(go.Scatter(x=age_array, y=income_array, mode='markers', marker=dict(color='blue')))
fig.update_layout(title='Economic Survey', xaxis_title='Age', yaxis_title='Income')
#fig.show()
numberofbicyclessold_array=[50,100,40,150,160,70,60,45]
months_array=["Jan","Feb","Mar","April","May","June","July","August"]
fig=go.Figure()
fig
fig.add_trace(go.Scatter(x=months_array, y=numberofbicyclessold_array, marker=dict(color='green')))
fig.update_layout(title='Bicycle Sales', xaxis_title='Months', yaxis_title='Number of Bicycles Sold')
#fig.show()
score_array=[80,90,56,88,95]
grade_array=['Grade 6','Grade 7','Grade 8','Grade 9','Grade 10']
fig=px.bar(x=grade_array, y=score_array, title='Pass Percentage of Classes')
#fig.show()
heights_array=np.random.normal(160,11,200)
fig = px.histogram(x=heights_array, title='Distribution of Heights')
#fig.show()
crime_details = {
    'City' : ['Chicago', 'Chicago', 'Austin', 'Austin','Seattle','Seattle'],
    'Numberofcrimes' : [1000, 1200, 400, 700,350,1500],
    'Year' : ['2007', '2008', '2007', '2008','2007','2008'],
}
df = pd.DataFrame(crime_details)
df
bub_data = df.groupby('City')['Numberofcrimes'].sum().reset_index()
bub_data
fig = px.scatter(bub_data, x='City', y='Numberofcrimes', size='Numberofcrimes', hover_name='City', title='Crime Statistics', size_max=60)
#fig.show()
exp_percent=[20,50,10,8,12]
house_holdcategories=['Grocery','Rent','School Fees','Transport','Savings']
fig = px.pie(values=exp_percent, names=house_holdcategories, title='Household Expenses')
#fig.show()
data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])
fig = px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
    title="Family chart"
)
fig.show()