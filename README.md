# Say Weather

This is the simple project that will show the realtime weather data.
You can retrieve weather data through the name of the city or the coordinates of the location.

## How to use : 

<i>Import the weather class first and then create a constructor for SearchWeather or CoordinateWeather</i>


<img src="https://i.ibb.co/dpPtYCZ/git2.png">


<b>OR</b>


<img src="https://i.ibb.co/CBQbgys/git1.png">

<b><h3>You can easily retrieve different type weather data by using this following code : </h3></b>

* Function : get_coordinates() will return coordinates of the location ie. Longitude and Latitude
   <code>print(what_is_weather.get_coordinates())</code>

* Function : get_city_data() will return name of city

   <code>print(what_is_weather.get_city_data())</code>

* Function : get_date() will return realtime date

   <code> print(what_is_weather.get_date())</code>

 * Function : get_weather() will return realtime weather ie. Rain, Clear, Cloud
 
    <code>print(what_is_weather.get_weather())</code>

* Function : get_weather_description() will return realtime weather description ie. clear sky, few clouds, smoke

    <code>print(what_is_weather.get_weather_description())</code>

* Function : get_temperature() will return realtime temperature according to location in Centigrade ie. 35◦C

   <code> print(what_is_weather.get_temperature())</code>

* Function : get_pressure() will return realtime Atmospheric pressure of the given location in Centigrade ie. 999 mbar

   <code> print(what_is_weather.get_pressure())</code>

* Function : get_humidity() will return realtime humidity in % ie. 56 %

    <code>print(what_is_weather.get_humidity())</code>

* Function : get_cloudiness() will return realtime cloudiness in % ie. 18 %

    <code>print(what_is_weather.get_cloudiness())</code>

* Function : get_sunirise_sunset() will return sunrise and sunset time ie. Sunrise : 5:55 Sunset : 19:27

    <code>print(what_is_weather.get_sunirise_sunset())</code>

* Function : get_wind_sd() will return wind speed and direction ie. Wind : 5.1 m/s (200◦)

    <code>print(what_is_weather.get_wind_sd())</code>
    
## Built with :
<a href="https://openweathermap.org/"><h3>    Openweathermap API</h3></a>
