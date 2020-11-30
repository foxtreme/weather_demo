#!flask/bin/python
from flask import Flask, jsonify
from flask_caching import Cache
from app.config import cache_config
from flask import request

from app.controllers.weather_demo import WeatherDemoController

cache = Cache(config=cache_config)
app = Flask(__name__)
cache.init_app(app)


@app.route("/weather", methods=["GET"])
@app.route("/weather/<int:days>", methods=["GET"])
@cache.memoize(2)
def get(days=None):
    city = request.args.get("city")
    country = request.args.get("country")
    weather_demo_controller = WeatherDemoController()
    if days:
        data = weather_demo_controller.get_weather_forecast(city, country, days)
    else:
        data = weather_demo_controller.get_weather_info(city, country)
    return jsonify({"data": data})


if __name__ == "__main__":
    app.run(debug=True)
