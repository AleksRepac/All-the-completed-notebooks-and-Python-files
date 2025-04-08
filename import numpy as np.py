import numpy as np
import pandas as pd
import folium
#print('Folium installed and imported!')
world_map = folium.Map()
world_map
import webbrowser
#webbrowser.open('https://www.google.com/maps')
#world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)
world_map
#webbrowser.open('https://www.google.com/maps')
mexico_latitude = 23.6345
mexico_longitude = -102.5528
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude], zoom_start=4)
mexico_map
map_filename = 'mexico_map.html'
mexico_map.save(map_filename)
#webbrowser.open(map_filename)
mexico_map = folium.Map(location=[23.6345, -102.5528], zoom_start=6, tiles='CartoDB dark_matter')
mexico_map.save('mexico_map.html')
#webbrowser.open('mexico_map.html')
df_incidents = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')
print(df_incidents.head())
print(df_incidents.shape)
limit = 100
df_incidents = df_incidents.iloc[0:limit, :]
df_incidents.shape
print(df_incidents.shape)
latitude = 37.77
longitude = -122.42
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)
sanfran_map
incidents = folium.map.FeatureGroup()
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=5,
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )
sanfran_map.add_child(incidents)
map_filename = 'sanfran_map.html'
sanfran_map.save(map_filename)
webbrowser.open(map_filename)
latitude = list(df_incidents.Y)
longitude = list(df_incidents.X)
labels = list(df_incidents.Category)
for lat, lng, label in zip(latitude, longitude, labels):
    folium.Marker([lat, lng], popup=label).add_to(sanfran_map)
sanfran_map.add_child(incidents)
map_filename = 'sanfran_map.html'
sanfran_map.save(map_filename)
webbrowser.open(map_filename)