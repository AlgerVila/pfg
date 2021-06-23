from typing import Dict, List
from pydantic import BaseModel

class propiedades(BaseModel):
    type: str
    value: str

class entity(BaseModel):
    id: str
    type: str
    pressure: propiedades
    temperature: propiedades
    time: propiedades