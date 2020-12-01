from app.exceptions import DecodingError
from app.thirdparty.open_weather.open_weather import OpenWeather
from app.util.utils import cardinal, mps_to_kmph, wind_term, convert_date, current_date, cloudiness
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
        if isinstance(city, str) and isinstance(country, str) and len(country) == 2:
            try:
                open_weather_response = OpenWeather.get_weather_info(city, country)
                response_text = open_weather_response.text
                json_response = json.loads(response_text)
                return self._format_response(city, country, json_response)
            except ValueError as e:
                raise DecodingError(response_text)
        else:
            message = "The format of the city ({city}) and/or country ({country}) you are entering is incorrect, " \
                      "please check them and try again.".format(
                city=city,
                country=country
            )
            return message

    def get_weather_forecast(self, city, country, day):
        """
        Returns weather forecast for a given day
        :param city: string, the name of the city. Ie, "Medellin"
        :param country: string, the code of the country. Ie, "CO"
        :param day: int, number between 0 and 6, 0 for today
        :return: string, the external api response
        """
        if 0 <= day <= 6:
            try:
                open_weather_response = OpenWeather.get_weather_forecast(city.capitalize())
                response_text = open_weather_response.text
                json_response = json.loads(response_text)
                if day == 0:
                    json_response["forecast"] = json_response.get("current")
                elif 0 < day < 7 and json_response.get("daily"):
                    forecast = json_response.get("daily")[day - 1]
                    json_response["forecast"] = forecast
                return self._format_forecast_response(day, city, country, json_response)
            except ValueError as e:
                raise DecodingError(e)
            except Exception as e:
                return "An error has occurred, Perhaps your selected city is not recognized. Description: {}".format(e)
        else:
            return "The day ({day}) you are trying to forecast is out of range".format(day=day)


    def _format_forecast_response(self, day, city, country, data):
        """
        Formats the external api response
        :param day: int, number between 0 and 6, 0 for today
        :param city: string, the name of the city. Ie, "Medellin"
        :param country: string, the code of the country. Ie, "CO"
        :param data: dictionary, the external api response
        :return: dictionary, the formatted response
        """
        if day == 0:
            key = "current"
            temperature_key = data.get("current").get("temp")
        else:
            key = "forecast"
            temperature_key = data.get("forecast").get("temp").get("day")
        wind_degree = data.get(key).get("wind_deg")
        wind_speed = data.get(key).get("wind_speed")
        cloudiness_percentage = data.get(key).get("clouds")
        wind_speed_kmh = mps_to_kmph(wind_speed)
        wind_direction = ""
        wind_desc = ""
        cloudiness_desc = ""
        for direction in cardinal:
            if direction.get("min") <= wind_degree < direction.get("max"):
                wind_direction = direction.get("direction")
                continue
        for term in wind_term:
            if term.get("min") <= wind_speed_kmh < term.get("max"):
                wind_desc = term.get("term")
                continue
        for term in cloudiness:
            if term.get("min") <= cloudiness_percentage < term.get("max"):
                cloudiness_desc = term.get("term")

        response = {
            "location_name": "{}, {}".format(city.capitalize(), country.upper()),
            "temperature": "{} °C".format(temperature_key),
            "wind": "{} {} m/s, {}".format(wind_desc, wind_speed, wind_direction),
            "cloudiness": "{}".format(cloudiness_desc),
            "pressure": "{} hpa".format(data.get(key).get("pressure")),
            "humidity": "{}%".format(data.get(key).get("humidity")),
            "sunrise": "{}".format(convert_date(data.get(key).get("sunrise"))),
            "sunset": "{}".format(convert_date(data.get(key).get("sunset"))),
            "geo_coordinates": "[{}, {}]".format(data.get("lat"), data.get("lon")),
            "requested_time": "{}".format(current_date())
        }
        if data.get("forecast"):
            response["forecast"] = data.get("forecast")
        return response


    def _format_response(self, city, country, data):
        """
        Formats the external api response
        :param city: string, the name of the city. Ie, "Medellin"
        :param country: string, the code of the country. Ie, "CO"
        :param data: dictionary, the external api response
        :return: dictionary, the formatted response
        """
        wind_degree = data.get("wind").get("deg")
        wind_speed = data.get("wind").get("speed")
        cloudiness_percentage = data.get("clouds").get("all")
        wind_speed_kmh = mps_to_kmph(wind_speed)
        wind_direction = ""
        wind_desc = ""
        cloudiness_desc = ""
        for direction in cardinal:
            if direction.get("min") <= wind_degree < direction.get("max"):
                wind_direction = direction.get("direction")
                continue
        for term in wind_term:
            if term.get("min") <= wind_speed_kmh < term.get("max"):
                wind_desc = term.get("term")
                continue
        for term in cloudiness:
            if term.get("min") <= cloudiness_percentage < term.get("max"):
                cloudiness_desc = term.get("term")

        response = {
            "location_name": "{}, {}".format(city.capitalize(), country.upper()),
            "temperature": "{} °C".format(data.get("main").get("temp")),
            "wind": "{} {} m/s, {}".format(wind_desc, wind_speed, wind_direction),
            "cloudiness": "{}".format(cloudiness_desc),
            "pressure": "{} hpa".format(data.get("main").get("pressure")),
            "humidity": "{}%".format(data.get("main").get("humidity")),
            "sunrise": "{}".format(convert_date(data.get("sys").get("sunrise"))),
            "sunset": "{}".format(convert_date(data.get("sys").get("sunset"))),
            "geo_coordinates": "[{}, {}]".format(data.get("coord").get("lat"), data.get("coord").get("lon")),
            "requested_time": "{}".format(current_date())
        }

        return response
