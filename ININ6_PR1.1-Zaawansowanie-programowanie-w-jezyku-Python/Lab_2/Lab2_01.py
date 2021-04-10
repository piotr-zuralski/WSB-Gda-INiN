import requests
import time

from holiday import Holiday

"""
Public holidays in Poland for current year
"""


def add_cross_to_holiday_name(holiday):
    holiday["localName"] = "✝ {0:s}".format(holiday["localName"])
    return holiday


holidaysApiUrl = f"https://date.nager.at/api/v2/PublicHolidays/{time.strftime('%Y')}/PL"
holidays = requests.get(holidaysApiUrl).json()
# print(holidays)

# filter
non_fixed_holidays = list(filter(lambda x: x["fixed"] is False, holidays))
# print(non_fixed_holidays)
# del non_fixed_holidays

# map
non_fixed_holidays = list(map(add_cross_to_holiday_name, non_fixed_holidays))
# print(non_fixed_holidays)

holidays_objects = []
for item in holidays:
    holidays_objects.append(Holiday(item['date'], item['localName'], item['name']))
# print(holidays_objects)
