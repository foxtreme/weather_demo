from app.exceptions import DecodingError
from app.thirdparty.open_weather.open_weather import OpenWeather
import json


class WeatherDemoController(object):
    """
    Class to handle the logic for the weather info requests
    """
    def get_weather_info(self, city, country):
        """
        Returns current weather info based on city and country
        :param city: string, the name of the city. Ie, "Medellin"
        :param country: string, the code of the country. Ie, "CO"
        :return: string, the external api response
        """
        open_weather_response = OpenWeather.get_weather_info(city, country)
        response_text = open_weather_response.text
        try:
            return json.loads(response_text)
        except ValueError as e:
            raise DecodingError(response_text)

    def get_weather_forecast(self, city, day):
        """
        Returns weather forecast for a given day
        :param city: string, the name of the city. Ie, "Medellin"
        :param day: int, number between 0 and 6, 0 for today
        :return: string, the external api response
        """
        try:
            if 0 <= day <= 6:
                open_weather_response = OpenWeather.get_weather_forecast(city)
                response_text = open_weather_response.text
                json_response = json.loads(response_text)
                if day == 0:
                    json_response["forecast"] = json_response.get("current")
                elif 0 < day < 7 and json_response.get("daily"):
                    forecast = json_response.get("daily")[day-1]
                    json_response["forecast"] = forecast
                return json_response
            else:
                return "The day you are trying to forecast is out of range"

        except ValueError as e:
            raise DecodingError(e)
