from app.config import open_weather_config
import requests


class OpenWeather(object):

    @staticmethod
    def get_weather_info(city, country):

        url = open_weather_config.get("CURRENT_URL").format(
            api_key=open_weather_config.get("API_KEY"),
            city=city,
            country=country
        )
        response = requests.get(url)
        return response
