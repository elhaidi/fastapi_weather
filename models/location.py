from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):
    city: str
    state: Optional[str]
    country: str
