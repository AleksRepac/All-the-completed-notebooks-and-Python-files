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
df_rec = df[df['Recession'] == 1]   
sns.lineplot(data=df_rec, x='unemployment_rate', y='Automobile_Sales', 
             hue='Vehicle_Type', style='Vehicle_Type', dashes=False)
plt.ylim(0, 850)
plt.legend(loc=(0.05, 0.3))
plt.show()