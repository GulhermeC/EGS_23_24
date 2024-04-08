from database import database
from schemas import Schedule
from models import schedule_table

async def get_schedules():
    query = schedule_table.select()
    return await database.fetch_all(query)

async def create_schedule(schedule: Schedule):
    query = schedule_table.insert().values(
        id=schedule.id, 
        time=schedule.time, 
        locationId=schedule.locationId
    )
    await database.execute(query)
    return schedule

async def get_schedule(schedule_id: str):
    query = schedule_table.select().where(schedule_table.c.id == schedule_id)
    return await database.fetch_one(query)

async def update_schedule(schedule_id: str, schedule: Schedule):
    query = schedule_table.update().where(schedule_table.c.id == schedule_id).values(
        time=schedule.time, 
        locationId=schedule.locationId
    )
    await database.execute(query)
    return {**schedule.dict(), "id": schedule_id}

async def delete_schedule(schedule_id: str):
    query = schedule_table.delete().where(schedule_table.c.id == schedule_id)
    await database.execute(query)
