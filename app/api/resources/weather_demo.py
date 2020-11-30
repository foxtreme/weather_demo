from flask import jsonify
from flask_restful import Resource, reqparse
from app.controllers.weather_demo import WeatherDemoController


class WeatherDemoResource(Resource):

    def get(self):
        data = WeatherDemoController().get_weather_info()
        return jsonify({"data": data})
