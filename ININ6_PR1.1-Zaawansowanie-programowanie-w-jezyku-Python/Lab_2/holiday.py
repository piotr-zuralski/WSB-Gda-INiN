from datetime import datetime

from managers.weather import WeatherManager

class Holiday:
    def __init__(self, date, local_name, name):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.local_name = local_name
        self.name = name
        self.weather = WeatherManager.get_weather_for_date(self.date)
    
    def __repr__(self):
        return f"{self.local_name} ({self.weather}) ({self.date.year})"
