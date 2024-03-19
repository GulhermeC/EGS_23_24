from pydantic import BaseModel, Field
from datetime import datetime

class Schedule(BaseModel):
    id: str
    guardId: str = Field(alias='guardId')
    time: datetime
    locationId: str = Field(alias='locationId')
