""" 
    this mudule will contain some function to work 
    with  OPEN Weaher API weather API.
"""

import requests
from typing import Optional

api_key: Optional[int] = None


def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"
    url = f" https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"
    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()
    print(data)
    return data
