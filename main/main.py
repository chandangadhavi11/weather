##This is the simple program that will show realtime weather data of the given name of location or given coodinates of the location.
# To search the weather data according to name of the city then use SearchWeather Constructor

# Developer : Chandan Gadhavi
# Date : 22-6-2020
##
import weather
def main():

    # Enter city name to get the date
    what_is_weather = weather.SearchWeather("California")

    # Function : get_coordinates() will return coordinates of the location ie. Longitude and Latitude
    print(what_is_weather.get_coordinates())

    # Function : get_city_data() will return name of city
    print(what_is_weather.get_city_data())

    # Function : get_date() will return realtime date
    print(what_is_weather.get_date())

    # Function : get_weather() will return realtime weather ie. Rain, Clear, Cloud
    print(what_is_weather.get_weather())

    # Function : get_weather_description() will return realtime weather description ie. clear sky, few clouds, smoke
    print(what_is_weather.get_weather_description())

    # Function : get_temperature() will return realtime temperature according to location in Centigrade ie. 35◦C
    print(what_is_weather.get_temperature())

    # Function : get_pressure() will return realtime Atmospheric pressure of the given location in Centigrade ie. 999 mbar
    print(what_is_weather.get_pressure())

    # Function : get_humidity() will return realtime humidity in % ie. 56 %
    print(what_is_weather.get_humidity())

    # Function : get_cloudiness() will return realtime cloudiness in % ie. 56 %
    print(what_is_weather.get_cloudiness())

    # Function : get_sunirise_sunset() will return sunrise and sunset time ie. Sunrise : 5:55 Sunset : 19:27
    print(what_is_weather.get_sunirise_sunset())

    # Function : get_wind_sd() will return wind speed and direction ie. Wind : 5.1 m/s (200◦)
    print(what_is_weather.get_wind_sd())


if __name__ == '__main__':
    main()