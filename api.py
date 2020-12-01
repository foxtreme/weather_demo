#!flask/bin/python
from app.config import cache_config
from app.controllers.weather_demo import WeatherDemoController
from flask import Flask, jsonify, request
from flask_caching import Cache


cache = Cache(config=cache_config)
app = Flask(__name__)
cache.init_app(app)
timeout = cache_config.get("CACHE_DEFAULT_TIMEOUT")


@app.route("/weather", methods=["GET"])
@app.route("/weather/<int:day>", methods=["GET"])
@cache.memoize(timeout)
def get(day=None):
    """
    Function to handle GET requests
    :param day: int, a number between 0 and 6, 0 for today
    :return: json object, the response with the weather info
    """
    city = request.args.get("city")
    country = request.args.get("country")
    weather_demo_controller = WeatherDemoController()
    if day:
        data = weather_demo_controller.get_weather_forecast(city, day)
    else:
        data = weather_demo_controller.get_weather_info(city, country)
    return jsonify({"data": data})


if __name__ == "__main__":
    app.run(debug=True)
