import fastapi
from models.location import Location
from services import weather_service
from fastapi import Depends
from typing import Optional
from pydantic import BaseModel


router = fastapi.APIRouter()
# define a pydantic class to do the validation


@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    response = await weather_service.get_report_async(loc.city, loc.state, loc.country, units)
    return response
