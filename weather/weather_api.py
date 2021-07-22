import fastapi
from typing import Optional
router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
def weather(city: str, state: Optional[str] = None, country: str = 'US', units: Optional[str] = 'metric'):
    return f"This is some report for {city} in {state} , {country} using {units} "
