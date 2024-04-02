# crud.py
from database import database
from schemas import Schedule

async def get_schedules():
    query = schedules.select()
    return await database.fetch_all(query)
