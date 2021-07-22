import fastapi
from models.location import Location
from services import weather_service
from fastapi import Depends
from typing import Optional
from pydantic import BaseModel


router = fastapi.APIRouter()
# define a pydantic class to do the validation


@router.get("/api/weather/{city}")
def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    return weather_service.get_report(loc.city, loc.state, loc.country, units)
