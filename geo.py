from datetime import datetime
from timezonefinder import TimezoneFinder
from pytz import timezone
from sunnyday import Weather
from random import uniform
from folium import Marker

class Geopoint(Marker):
    
    latitude_range = (-90, 90)
    
    def __init__(self, latitude, longitude):
        super().__init__(location = [latitude, longitude])
        self.latitude = latitude
        self.longitude = longitude
        
    def closest_parallel(self):
        return round(self.latitude)
    
    def get_time(self):
        timezone_string = TimezoneFinder().timezone_at(lat = self.latitude, lng = self.longitude)
        time_now = datetime.now(timezone(timezone_string))
        print(timezone_string)
        return time_now
    
    def get_weather(self):
        weather = Weather(apikey = '4eb220c7777ddfb6a5c9d6ee0922289a', lat = self.latitude, lon = self.longitude)
        return weather.next_12h_simplified()
    
    @classmethod
    def random(cls):
        return cls(latitude = uniform(-90, 90), longitude = uniform(-180, 180))


    
