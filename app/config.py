cache_config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 12
}

open_weather_config = {
    "API_KEY": "a8720333e3c9b3aa14f12840073213cc",
    "ONE_CALL_URL": "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}",
    "CURRENT_URL": "http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric",
    "EXCLUSIONS": "minutely,hourly,alerts"
}
