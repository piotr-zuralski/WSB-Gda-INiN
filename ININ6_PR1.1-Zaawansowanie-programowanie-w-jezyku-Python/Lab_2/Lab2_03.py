import requests
import time

from holiday import Holiday
import matplotlib.pyplot as plt 

"""
Public holidays in Poland for current year
"""


def get_easters_holidays_for_years(years: []) -> []:
    easters = []
    for y in years:
        holidays_api_url = f"https://date.nager.at/api/v2/PublicHolidays/{y}/PL"
        holidays_list = requests.get(holidays_api_url).json()
        easters += list(filter(lambda x: x["localName"] == "Wielkanoc", holidays_list))
    return easters


endYear = int(time.strftime('%Y'))
startYear = endYear-7
holidays = get_easters_holidays_for_years(range(startYear, endYear+1))

holidays_objects = []
for item in holidays:
    holidays_objects.append(Holiday(item['date'], item['localName'], item['name']))
print(holidays_objects)

weather_measurements = set(i.weather for i in holidays_objects)
print(weather_measurements)

weather_values = []
for c in weather_measurements:
    weather_values.append(sum(i.weather == c for i in holidays_objects))


plt.figure(figsize=(8, 6))
plt.pie(weather_values, labels=weather_measurements, autopct='%.2f')
plt.title('Procentowy rozkład pogody podczas świat wielanocnych w Warszawie')
plt.savefig('wykres.png')
plt.clf()

with open('wielkanoce.txt', 'w') as file:
    for w in holidays_objects:
        file.write(f"{w.date.strftime('%Y-%m-%d')} {w.weather}\n")
