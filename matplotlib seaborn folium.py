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
response = requests.get(URL)
text = io.StringIO(response.text)
df = pd.read_csv(text)
print(df.head())
print (df.columns)
print(df.describe())
df_new=df.groupby('Year')['Automobile_Sales'].mean()
df_new.plot(x=df_new.index, y=df_new.values)
plt.figure(figsize=(10,6))
plt.xlabel('Year')
plt.ylabel('Average Sales in Thousands')
plt.title('Average Sales in Thousands Over the Time')
plt.show()