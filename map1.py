import folium   #Folium library needed to create any map object
import pandas   #We need to import pandas to read the csv and the json files

data = pandas.read_csv("Volcanoes.txt") # file can be found in the same directory
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):  # color pointed measures are created by making color_producer function
    if elevation < 1000:
        return "green"
    elif 1000<= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location =[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain") # we enter latitude and longitude data to start the map

fg_volcanoes = folium.FeatureGroup(name="Volcanoes") #FeatureGroup is a part of folium which comes handy to insert less layers.

for lt, ln, el in zip(lat, lon, elev):
    fg_volcanoes.add_child(folium.CircleMarker(location=[lt, ln], radius = 10, color='grey', popup=str(el) + " m", 
    fill_color=color_producer(el), color_opacity=0.7))

fg_population = folium.FeatureGroup(name="Population")

fg_population.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-Sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000
else 'yellow' if 1000000 <= x['properties'] ['POP2005'] < 2500000 else 'red'})) #Here we input the population data, file is found at the same directory


map.add_child(fg_volcanoes)
map.add_child(fg_population)
map.add_child(folium.LayerControl())
map.save("Map1.html") 