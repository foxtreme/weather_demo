from app.exceptions import DecodingError
from app.thirdparty.open_weather.open_weather import OpenWeather
import json


class WeatherDemoController(object):

    def get_weather_info(self, city, country):
        open_weather_response = OpenWeather.get_weather_info(city, country)
        response_text = open_weather_response.text
        try:
            return json.loads(response_text)
        except ValueError as e:
            raise DecodingError(response_text)

    def get_weather_forecast(self, city, country, days):
        return "Let's hope for the best {} {} {}".format(city, country, days)
