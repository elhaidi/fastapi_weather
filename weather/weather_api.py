import fastapi
from models.validation_error import ValidationError
from models.location import Location
from services import weather_service
from fastapi import Depends
from typing import Optional
from pydantic import BaseModel
from fastapi import Response


router = fastapi.APIRouter()
# define a pydantic class to do the validation


@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    try:
        response = await weather_service.get_report_async(loc.city, loc.state, loc.country, units)
    except ValidationError as err:
        return Response(content=err.error_msg, status_code=err.status_code)
    return response
