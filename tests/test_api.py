import pytest
import api as weather_demo


@pytest.fixture
def client():
    weather_demo.app.config['TESTING'] = True

    with weather_demo.app.test_client() as client:
        yield client

def test_get_current_weather():
    with weather_demo.app.test_client() as c:
        rv = c.get('/weather_demo?city=cali&country=CO')
        assert rv.data is not None

def test_get_forecast_weather():
    with weather_demo.app.test_client() as c:
        rv = c.get('/weather_demo/3?city=cali&country=CO')
        assert rv.data is not None
