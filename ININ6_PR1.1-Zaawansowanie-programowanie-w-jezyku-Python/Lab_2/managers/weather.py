import requests
from datetime import datetime
from string import Template


class WeatherManager:
    CITY_ID = 523920
    URL = Template("https://www.metaweather.com/api/location/$cityId/$year/$month/$day/")
    
    @staticmethod
    def get_weather_for_date(date: datetime):
        url = WeatherManager.URL.substitute(
            cityId=WeatherManager.CITY_ID,
            year=date.year,
            month=date.month,
            day=date.day
        )
        weather_measurements = requests.get(url).json()
        return weather_measurements[0]["weather_state_name"]
