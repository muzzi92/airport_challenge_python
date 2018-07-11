from weather import Weather

class TestWeather:

    def test_random_returns_stormy_when_int_1(self):
        weather = Weather()
        assert weather.forecast(1) == 'stormy'
