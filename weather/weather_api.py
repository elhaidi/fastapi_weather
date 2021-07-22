import fastapi
from models.location import Location
from fastapi import Depends
from typing import Optional
from pydantic import BaseModel


router = fastapi.APIRouter()
# define a pydantic class to do the validation


@router.get("/api/weather/{city}")
def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    return f"This is some report for {loc.city} in {loc.state} , {loc.country} using {units} "
