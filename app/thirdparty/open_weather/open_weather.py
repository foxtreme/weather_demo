import logging
import os
import pandas as pd
import pathlib
import requests
from app.config import open_weather_config, logging_config


class OpenWeather(object):
    """
    Class to handle the requests to open weather external api
    """

    @staticmethod
    def get_weather_info(city, country):
        """
        Returns current weather info based on city and country
        :param city: string, the name of the city. Ie, "Medellin"
        :param country: string, the code of the country. Ie, "CO"
        :return: string, the external api response
        """
        headers = {'content-type': 'application/json'}
        url = open_weather_config.get("CURRENT_URL").format(
            api_key=open_weather_config.get("API_KEY"),
            city=city,
            country=country
        )
        response = requests.get(url=url, headers=headers)
        content_type = response.headers["Content-Type"]
        logging.basicConfig(
            filename=logging_config.get("FILENAME"),
            level=logging.DEBUG
        )
        logging.debug('Response header Content-Type {}'.format(content_type))
        return response

    @staticmethod
    def get_weather_forecast(city):
        """
        Returns weather forecast for a given day
        :param city: string, the name of the city. Ie, "Medellin"
        :return: string, the external api response
        """
        current_dir = pathlib.Path(__file__).parent
        path = os.path.join(str(current_dir), "worldcities.csv")
        df = pd.read_csv(path)
        lat_series = df[df["city_ascii"] == city]["lat"]
        lon_series = df[df["city_ascii"] == city]["lng"]
        lat = lat_series.values[0]
        lon = lon_series.values[0]

        headers = {'content-type': 'application/json'}
        url = open_weather_config.get("ONE_CALL_URL").format(
            api_key=open_weather_config.get("API_KEY"),
            lat=lat,
            lon=lon,
            part=open_weather_config.get("EXCLUSIONS")
        )
        response = requests.get(url=url, headers=headers)
        content_type = response.headers["Content-Type"]
        logging.basicConfig(
            filename=logging_config.get("FILENAME"),
            level=logging.DEBUG
        )
        logging.debug('Response header Content-Type {}'.format(content_type))
        return response
