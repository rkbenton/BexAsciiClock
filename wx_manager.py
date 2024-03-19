"""
Weather manager.
"""

import requests


class WxManager:

    @staticmethod
    def get_wx_string(api_url: str | None) -> str:
        """
        Call api.weather.gov and get the weather forecast for Seattle.
        :param api_url: if None, will default to 'https://api.weather.gov/gridpoints/SEW/130,65/forecast',
        the forecast for Seattle. Otherwise, the given URL will be used.'
        :return: A string describing the wx forecast, or an error string.
        """
        default_seattle = 'https://api.weather.gov/gridpoints/SEW/130,65/forecast'
        if api_url is None:
            api_url = default_seattle
        weather_str = ""
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                weather_data = response.json()
                weather_str = "Seattle Weather:\n" + weather_data['properties']['periods'][0]['detailedForecast']
                weather_str = weather_str.replace('.', '.\n')
            else:
                weather_str = f"Failed to fetch weather data. ({response.status_code})"
        except Exception as e:
            weather_str = "ugh: " + str(e)
        return weather_str
