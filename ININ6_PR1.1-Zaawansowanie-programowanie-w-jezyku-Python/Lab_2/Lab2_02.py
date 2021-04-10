import requests
import time

from holiday import Holiday

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

startYear = int(time.strftime('%Y'))
endYear = startYear-6
holidays = get_easters_holidays_for_years(range(startYear, endYear))

