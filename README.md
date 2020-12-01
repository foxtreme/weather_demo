# weather_demo
REST API to get weather information from a city

<h2>How to run </h2>
<ul>
<li>Install any pending dependencies with pip3 install -r requirements.txt</li>
<li>cd to <i>weather_demo</i> folder</li>
<li>type in the terminal <code>python api.py</code></li>
</ul>

<h2>Testing with Postman</h2>
<h4>Testing by city and country code</h4>
 URL: http://127.0.0.1:5000/weather?city=medellin&country=CO
 <br>
 METHOD: GET
 <br>
 EXAMPLE OF RESPONSE:
 <pre>
 {
    "data": {
        "cloudiness": "Mostly Cloudy/Considerable cloudiness",
        "geo_coordinates": "[6.25, -75.56]",
        "humidity": "56%",
        "location_name": "Medellin, CO",
        "pressure": "1027 hpa",
        "requested_time": "2020-12-01 16:34:21.858091",
        "sunrise": "5:58",
        "sunset": "17:45",
        "temperature": "20.09 °C",
        "wind": "Gentle Breeze 4.1 m/s, east-southeast"
    }
}
 </pre>
 <h4>Testing forecast by city and country code</h4>
 The number at the end of the base url corresponds to the day between 0 and 6
 <br>
 URL: http://127.0.0.1:5000/weather/5?city=medellin&country=CO
 <br>
 METHOD: GET
 <br>
 EXAMPLE OF RESPONSE:
 <pre>
 {
    "data": {
        "cloudiness": "Mostly Cloudy/Considerable cloudiness",
        "forecast": {
            "clouds": 85,
            "dew_point": 14.8,
            "dt": 1607270400,
            "feels_like": {
                "day": 24.91,
                "eve": 24.23,
                "morn": 17,
                "night": 17.45
            },
            "humidity": 57,
            "pop": 1,
            "pressure": 1014,
            "rain": 13.75,
            "sunrise": 1607252431,
            "sunset": 1607294815,
            "temp": {
                "day": 23.64,
                "eve": 22.28,
                "max": 23.88,
                "min": 16.21,
                "morn": 16.21,
                "night": 16.82
            },
            "uvi": 1,
            "weather": [
                {
                    "description": "moderate rain",
                    "icon": "10d",
                    "id": 501,
                    "main": "Rain"
                }
            ],
            "wind_deg": 50,
            "wind_speed": 0.3
        },
        "geo_coordinates": "[6.24, -75.57]",
        "humidity": "57%",
        "location_name": "Medellin, CO",
        "pressure": "1014 hpa",
        "requested_time": "2020-12-01 16:25:26.308560",
        "sunrise": "6:0",
        "sunset": "17:46",
        "temperature": "23.64 °C",
        "wind": "Light Air 0.3 m/s, northeast"
    }
}
 </pre>

 