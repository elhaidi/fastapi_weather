import fastapi

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
def weather(city: str):
    return "This is some reports" + city
