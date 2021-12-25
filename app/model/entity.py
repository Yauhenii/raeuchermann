from datetime import date

from pydantic.main import BaseModel


class Entity(BaseModel):
    e_name: str
    e_number: float
    e_date: date
