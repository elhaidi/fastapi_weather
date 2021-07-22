""" 
    this mudule will contain some function to work 
    with  OPEN Weaher API weather API.
"""

import requests
import httpx
from typing import Optional

api_key: Optional[int] = None


async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()

    return data['main']
