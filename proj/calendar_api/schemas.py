from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class Schedule(BaseModel):
    id: UUID
    time: datetime
    locationId: str = Field(..., alias='locationId')
    person_name: str

class ScheduleUpdate(BaseModel):
    time: datetime
    locationId: str = Field(..., alias='locationId')
    person_name: str
