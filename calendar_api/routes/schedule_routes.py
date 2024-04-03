# schedule_routes.py
from fastapi import APIRouter, HTTPException, status, Body
from typing import List
from crud import create_schedule, get_schedule, get_schedules, update_schedule, delete_schedule
from schemas import Schedule

router = APIRouter()

@router.get("/schedules/", response_model=List[Schedule])
async def list_schedules():
    return await get_schedules()

@router.post("/schedules/", response_model=Schedule, status_code=status.HTTP_201_CREATED)
async def create_a_schedule(schedule: Schedule):
    return await create_schedule(schedule)

@router.get("/schedule/{schedule_id}", response_model=Schedule)
async def read_schedule(schedule_id: str):
    schedule = await get_schedule(schedule_id)
    if schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule

@router.put("/schedule/{schedule_id}", response_model=Schedule)
async def update_a_schedule(schedule_id: str, schedule: Schedule):
    updated_schedule = await update_schedule(schedule_id, schedule)
    if updated_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return updated_schedule

@router.delete("/schedule/{schedule_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_schedule(schedule_id: str):
    await delete_schedule(schedule_id)
    return {"message": "Schedule deleted successfully"}

