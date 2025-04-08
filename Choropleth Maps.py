import numpy as np
import pandas as pd
import folium
df_can = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.csv')
print(df_can.head())
print(df_can.shape)
import requests
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/world_countries.json"
response = requests.get(url)
with open("world_countries.json", "wb") as f:
    f.write(response.content)

print(df_can.head())
print(df_can.shape)
world_geo = r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/world_countries.json'
world_map = folium.Map(location=[0, 0], zoom_start=2, tiles='cartodbpositron')
world_map.save('world_map.html')
import webbrowser
webbrowser.open('world_map.html')

