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
df = pd.read_csv(URL)
print(df.head())
print (df.columns)
print(df.describe())
df_new=df.groupby('Year')['Automobile_Sales'].mean()
plt.figure(figsize=(10,6))
plt.plot(df_new.index, df_new.values, marker='o', color='blue', label="Average Automobile Sales")
plt.xlabel('Year')
plt.ylabel('Average Sales in Thousands')
plt.title('Average Sales in Thousands Over the Years')
plt.legend()
plt.grid(True)
plt.show()