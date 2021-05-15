from os import X_OK
from folium import Map, Marker, Popup
from geo import Geopoint

# Create latitude and longitude values
latitude = 40.4
longitude = -3.47

# Create a Geopoint Instance
geopoint = Geopoint(latitude = latitude, longitude = longitude)

# folium Map Instance and add to map
myMap = Map(location= [latitude, longitude])

weather_status = geopoint.get_weather()
print(weather_status)
popup_content = f""" 
{weather_status[0][0][-8:-6]}h: {weather_status[0][1]}°F <img src="https://openweathermap.org/img/wn/{weather_status[0][3]}@2x.png" width="35">
<hr style="margin: 1px;">
{weather_status[1][0][-8:-6]}h: {weather_status[1][1]}°F <img src="https://openweathermap.org/img/wn/{weather_status[1][3]}@2x.png" width="35">
<hr style="margin: 1px;">
{weather_status[2][0][-8:-6]}h: {weather_status[2][1]}°F <img src="https://openweathermap.org/img/wn/{weather_status[2][3]}@2x.png" width="35">
<hr style="margin: 1px;">
{weather_status[3][0][-8:-6]}h: {weather_status[3][1]}°F <img src="https://openweathermap.org/img/wn/{weather_status[3][3]}@2x.png" width="35">
<hr style="margin: 1px;">
"""


popup = Popup(popup_content, max_width=400)



popup.add_to(geopoint)
geopoint.add_to(myMap)

myMap.save('map.html')

print('checked')