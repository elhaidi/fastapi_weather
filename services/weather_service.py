"""
    this mudule will contain some function to work
    with  OPEN Weaher API weather API.
"""

import requests
import httpx
from typing import Optional, Tuple
from fastapi import Response
from models.validation_error import ValidationError

api_key: Optional[int] = None


async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:

    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}'
    async with httpx.AsyncClient() as client:
        resp: Response = await client.get(url)
        if resp.status_code != 200:
            raise ValidationError(resp.text, status_code=resp.status_code)
    data = resp.json()

    return data['main']


def validate_units(city: str, state: Optional[str], country: str, unit: str) -> Tuple[str, Optional[str], str, sr]:
    # validae the city
    city = city.lower().strip()

    # validate the country
    if not country:
        country = 'us'
    else:
        country = country.lower().split()
    if len(country) != 2:
        error = f"Invalid country: {country}. It must be a two letter abbreviation such as US or GB."
        raise ValidationError(error_msg=error, status_code=400)

    # valdiate state:
    if state:
        state = state.strip().lower()

    if state and len(state) != 2:
        error = f"Invalid state: {state}. It must be a two letter abbreviation such as CA or KS (use for US only)."
        raise ValidationError(status_code=400, error_msg=error)
    # validate the units
    if unit:
        unit = unit.lower().strip()
    valid_unit = {'metric', 'imperial', 'standard'}
    if unit not in valid_unit:
        error = f'Invalid unis {unit}, it must be in {valid_unit}'
        raise ValidationError(error_msg=error, status_code=400)
    return city, state, country, unit
