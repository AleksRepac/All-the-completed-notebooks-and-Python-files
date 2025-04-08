import folium
canada_map = folium.Map(location=[56.130, -106.35], zoom_start=4)
canada_map.save('canada_map.html')
import webbrowser
webbrowser.open('canada_map.html')
world_map = folium.Map(zoom_start=2)
webbrowser.open('world_map.html')
