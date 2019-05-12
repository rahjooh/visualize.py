import folium , pandas as pd

x1 = pd.ExcelFile("../../data/iran provineces lon lat.xlsx")
df = x1.parse("Sheet1")
print(df)



map_object = folium.Map(location=[35.6892,51.389], zoom_start=6, tiles="Stamen toner")
for i in range(31):
    folium.Marker([float(df['lat'][i]),float(df['lon'][i])], popup=str(df['state name farsi'][i])+'  :  '+str(df['pos count'][i])+ ' پذیرنده').add_to(map_object)
marker = folium.features.Marker([64.127573, -21.903975], popup="Icelandic Meteorology Office")
marker = folium.features.Marker([64.1573, -21.9975], popup="Icelandi Office")
map_object.add_child(marker)
folium.Map.save(map_object, "index.html")