""" this mudule will contain some function to work 
    with  OPEN Weaher API weather API.
"""
from typing import Optional

api_key: Optional[str] = None


def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:
    q = f"{city},{state},{country}"
    key = "ff82c0a5682c9c4303d915141aebd007"
    url = f" https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"
    print(url)
