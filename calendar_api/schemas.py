from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Schedule(BaseModel):
    id: str
    time: datetime
    locationId: str = Field(..., alias='locationId')
