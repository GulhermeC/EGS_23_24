# schedule_routes.py
from fastapi import APIRouter
from crud import get_schedules

router = APIRouter()

@router.get("/schedules/")
async def list_schedules():
    return await get_schedules()
