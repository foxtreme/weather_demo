from flask_restful import Api
from app import app
from app.api.resources.weather_demo import WeatherDemoResource

weather_demo_api = Api(app)

weather_demo_api.add_resource(
    WeatherDemoResource,
    "/weather_demo"
)

if __name__ == "__main__":
    app.run()
