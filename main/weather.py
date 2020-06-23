# Example :
# import weather
# # Enter city name to get the date
#     what_is_weather = weather.SearchWeather("California")
#
#     # Function : get_coordinates() will return coordinates of the location ie. Longitude and Latitude
#     print(what_is_weather.get_coordinates())
#
#     # Function : get_city_data() will return name of city
#     print(what_is_weather.get_city_data())
#
#     # Function : get_date() will return realtime date
#     print(what_is_weather.get_date())
#
#     # Function : get_weather() will return realtime weather ie. Rain, Clear, Cloud
#     print(what_is_weather.get_weather())
#
#     # Function : get_weather_description() will return realtime weather description ie. clear sky, few clouds, smoke
#     print(what_is_weather.get_weather_description())
#
#     # Function : get_temperature() will return realtime temperature according to location in Centigrade ie. 35◦C
#     print(what_is_weather.get_temperature())
#
#     # Function : get_pressure() will return realtime Atmospheric pressure of the given location in Centigrade ie. 999 mbar
#     print(what_is_weather.get_pressure())
#
#     # Function : get_humidity() will return realtime humidity in % ie. 56 %
#     print(what_is_weather.get_humidity())
#
#     # Function : get_cloudiness() will return realtime cloudiness in % ie. 56 %
#     print(what_is_weather.get_cloudiness())
#
#     # Function : get_sunirise_sunset() will return sunrise and sunset time ie. Sunrise : 5:55 Sunset : 19:27
#     print(what_is_weather.get_sunirise_sunset())
#
#     # Function : get_wind_sd() will return wind speed and direction ie. Wind : 5.1 m/s (200◦)
#     print(what_is_weather.get_wind_sd())

# Example 2 :
# import weather
# # Enter city name to get the date
#     what_is_weather = weather.CoordinateWeather("California")
#
#     # Function : get_coordinates() will return coordinates of the location ie. Longitude and Latitude
#     print(what_is_weather.get_coordinates())
#
#     # Function : get_city_data() will return name of city
#     print(what_is_weather.get_city_data())
#
#     # Function : get_date() will return realtime date
#     print(what_is_weather.get_date())
#
#     # Function : get_weather() will return realtime weather ie. Rain, Clear, Cloud
#     print(what_is_weather.get_weather())
#
#     # Function : get_weather_description() will return realtime weather description ie. clear sky, few clouds, smoke
#     print(what_is_weather.get_weather_description())
#
#     # Function : get_temperature() will return realtime temperature according to location in Centigrade ie. 35◦C
#     print(what_is_weather.get_temperature())
#
#     # Function : get_pressure() will return realtime Atmospheric pressure of the given location in Centigrade ie. 999 mbar
#     print(what_is_weather.get_pressure())
#
#     # Function : get_humidity() will return realtime humidity in % ie. 56 %
#     print(what_is_weather.get_humidity())
#
#     # Function : get_cloudiness() will return realtime cloudiness in % ie. 56 %
#     print(what_is_weather.get_cloudiness())
#
#     # Function : get_sunirise_sunset() will return sunrise and sunset time ie. Sunrise : 5:55 Sunset : 19:27
#     print(what_is_weather.get_sunirise_sunset())
#
#     # Function : get_wind_sd() will return wind speed and direction ie. Wind : 5.1 m/s (200◦)
#     print(what_is_weather.get_wind_sd())

# To search the weather data according to coordinates then use CoordinateWeather Constructor
#
# Developer : Chandan Gadhavi

# Date : 22-6-2020
##

import urllib.request
import json
import time


def get_date(real_unix_date):
    real_date = time.gmtime(real_unix_date)
    date_day = real_date.tm_mday
    date_month = real_date.tm_mon
    date_year = real_date.tm_year

    return f"Date : {date_day}-{date_month}-{date_year}"

def get_sunrise(real_unix_sec, gmt_unix_sec):
    real = time.gmtime(real_unix_sec)
    gmt2 = gmt_unix_sec
    if gmt2 < 0 :
        gmt2 = gmt2 * -1
    gmt = time.gmtime(gmt2)
    a = real.tm_hour
    x = real.tm_min
    b = gmt.tm_hour
    y = gmt.tm_min
    if x + y >= 60:
        a = a + 1
        z = x + y - 60
    else:
        z = (x) + (y)
    if gmt_unix_sec < 0:
        c = a-b
    else:
        c = a+b
    if c > 24:
        c = c - 24

    if z < 10:
        return (f"Sunrise : {c}:0{z}")
    else:
        return (f"Sunrise : {c}:{z}")


def get_sunset(real_unix_sec, gmt_unix_sec):
    real = time.gmtime(real_unix_sec)
    gmt = time.gmtime(gmt_unix_sec)
    a = real.tm_hour
    b = gmt.tm_hour
    x = real.tm_min
    y = gmt.tm_min
    if x + y >= 60:
        a = a + 1
        z = x + y - 60
    else:
        z = x + y

    if z<10:
        return (f"Sunset : {a + b}:0{z}")
    else:
        return (f"Sunset : {a + b}:{z}")


class Weather():

    

    def __init__(self):
        self.theJSON = None

    def get_coordinates(self):
        if "lon" in self.theJSON["coord"] and "lat" in self.theJSON["coord"]:
            coordinate_longitude = self.theJSON["coord"]["lon"]
            coordinate_latitude = self.theJSON["coord"]["lat"]
            return f"Coordinates : {coordinate_latitude} {coordinate_longitude}"
        else:return 0

    def get_city_data(self):
        if "name" in self.theJSON:
            location_city = self.theJSON["name"]
            return f"City : {location_city}"
        else:
            return 0

    def get_date(self):
        if "dt" in self.theJSON:
            location_date = get_date(self.theJSON["dt"])
            return location_date
        else:return 0

    def get_weather(self):
        if "main" in self.theJSON["weather"][0]:
            location_weather = self.theJSON["weather"][0]["main"]
            return f"Weather : {location_weather}"
        else:return 0

    def get_weather_description(self):
        if "description" in self.theJSON["weather"][0]:
            location_weather_description = self.theJSON["weather"][0]["description"]
            return f"Description : {location_weather_description}"
        else:return 0

    def get_temperature(self):
        if "temp" in self.theJSON['main']:
            location_tempreture = int(self.theJSON['main']["temp"])
            return f"Temperature : {location_tempreture- 273}◦C"
        else:return 0


    def get_pressure(self):
        if "pressure" in self.theJSON["main"]:
            location_pressure = int(self.theJSON['main']["pressure"])
            return f"Pressure : {location_pressure} mbar"
        else:return 0

    def get_humidity(self):
        if "humidity" in self.theJSON["main"]:
            location_humidity = int(self.theJSON['main']["humidity"])
            return f"Humidity : {location_humidity} %"
        else:return 0

    def get_sunirise_sunset(self):
        if "sunrise" in self.theJSON["sys"] and "sunset" in self.theJSON["sys"]:
            location_sunrise = get_sunrise(self.theJSON["sys"]["sunrise"], self.theJSON["timezone"])
            location_sunset = get_sunset(self.theJSON["sys"]["sunset"], self.theJSON["timezone"])
            return f"{location_sunrise} {location_sunset}"
        return 0
    def get_wind_sd(self):
        if "speed" in self.theJSON["wind"] and "deg" in self.theJSON["wind"]:
            location_wind_sp = self.theJSON["wind"]["speed"]
            location_wind_de = self.theJSON["wind"]["deg"]
            return f"Wind : {location_wind_sp} m/s ({location_wind_de}◦)"
        else:return 0

    def get_cloudiness(self):
        if "all" in self.theJSON["clouds"]:
            location_cloudiness = self.theJSON["clouds"]["all"]
            return f"Cloudiness : {location_cloudiness}%"
        else:return 0

class SearchWeather(Weather):
    def __init__(self, city_name):
        super().__init__()
        self._city_name = city_name
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=b86aa9d6c324bb3158f287b73ec1bfe8"
        web = urllib.request.urlopen(url)
        data = web.read()
        self.theJSON = json.loads(data)

class CoordinateWeather(Weather):
    def __init__(self, lat,long):
        super().__init__()
        c_long = long
        c_lat = lat
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={c_lat}&lon={c_long}&appid=b86aa9d6c324bb3158f287b73ec1bfe8"
        web = urllib.request.urlopen(url)
        data = web.read()
        self.theJSON = json.loads(data)



