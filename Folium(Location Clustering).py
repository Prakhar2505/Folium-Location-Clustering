#Importing important libraries
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from folium.plugins import FastMarkerCluster

#Importing Dataset
population = pd.read_csv("in.csv")
df = population.copy()

#Intializing center of the map
my_map = folium.Map(location=[df['lat'].mean(), 
                                df['lng'].mean()],
                                zoom_start=5)

#Intializing cluster object
mc = MarkerCluster()

#creating a Marker for each point in df.  Each point will get a popup with their zip
for row in df.itertuples():
    d=row.city+" population : "+str(row.population)
    mc.add_child(folium.Marker(location=[row.lat, row.lng],popup=d))

#Appending to the map    
my_map1.add_child(mc)

#Saving to a HTML file
my_map1.save(" my_map.html ") 