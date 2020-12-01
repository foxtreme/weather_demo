import datetime
import time

cardinal = [
    {"min": 348.75, "max": 11.25, "direction": "north"},
    {"min": 11.25, "max": 33.75, "direction": "north-northeast"},
    {"min": 33.75, "max": 56.25, "direction": "northeast"},
    {"min": 56.25, "max": 78.75, "direction": "east-northeast"},
    {"min": 78.75, "max": 101.25, "direction": "east"},
    {"min": 101.25, "max": 123.75, "direction": "east-southeast"},
    {"min": 123.75, "max": 146.25, "direction": "southeast"},
    {"min": 146.25, "max": 168.75, "direction": "south-southeast"},
    {"min": 168.75, "max": 191.25, "direction": "south"},
    {"min": 191.25, "max": 213.75, "direction": "southwest"},
    {"min": 213.75, "max": 236.25, "direction": "south-southwest"},
    {"min": 236.25, "max": 258.75, "direction": "southwest"},
    {"min": 258.75, "max": 281.25, "direction": "west-southwest"},
    {"min": 281.25, "max": 303.75, "direction": "west"},
    {"min": 303.75, "max": 326.25, "direction": "west-northwest"},
    {"min": 326.25, "max": 348.75, "direction": "northwest"},
    {"min": 326.25, "max": 348.75, "direction": "north-northwest"}
]

wind_term = [
    {"min": 0, "max": 1, "term": "Calm"},
    {"min": 1, "max": 5, "term": "Light Air"},
    {"min": 6, "max": 11, "term": "Light Breeze"},
    {"min": 12, "max": 19, "term": "Gentle Breeze"},
    {"min": 20, "max": 28, "term": "Moderate Breeze"},
    {"min": 29, "max": 38, "term": "Fresh Breeze"},
    {"min": 39, "max": 49, "term": "Strong Breeze"},
    {"min": 50, "max": 61, "term": "Near Gale"},
    {"min": 62, "max": 74, "term": "Gale"},
    {"min": 75, "max": 88, "term": "Strong Gale"},
    {"min": 89, "max": 102, "term": "Storm"},
    {"min": 103, "max": 117, "term": "Violent Storm"},
    {"min": 118, "max": 500, "term": "Hurricane"},
]

cloudiness = [
    {"min": 88, "max": 100, "term": "Cloudy/Overcast"},
    {"min": 70, "max": 87, "term": "Mostly Cloudy/Considerable cloudiness"},
    {"min": 51, "max": 69, "term": "Partly Sunny/Mostly Cloudy"},
    {"min": 26, "max": 50, "term": "Mostly Sunny/Partly Cloudy"},
    {"min": 6, "max": 25, "term": "Sunny/Mostly clear"},
    {"min": 0, "max": 5, "term": "Sunny/Clear"}
]

def mps_to_kmph(mps):
    return 3.6 * mps


def convert_date(ms):
    date = datetime.datetime.fromtimestamp(ms)
    return "{}:{}".format(date.hour, date.minute)


def current_date():
    return datetime.datetime.utcnow()
