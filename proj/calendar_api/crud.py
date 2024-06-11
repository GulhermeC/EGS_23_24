from uuid import UUID
from database import database
from schemas import Schedule, ScheduleUpdate
from models import schedule_table

async def get_schedules():
    query = schedule_table.select()
    return await database.fetch_all(query)

async def create_schedule(schedule: Schedule):
    query = schedule_table.insert().values(
        id=schedule.id,
        time=schedule.time,
        locationId=schedule.locationId,
        person_name=schedule.person_name
    )
    last_record_id = await database.execute(query)
    return {**schedule.dict(), "id": schedule.id}

async def get_schedule(id: UUID):
    query = schedule_table.select().where(schedule_table.c.id == id)
    return await database.fetch_one(query)

async def update_schedule(id: UUID, schedule_update: ScheduleUpdate):
    # Update this function to use ScheduleUpdate
    query = schedule_table.update().where(schedule_table.c.id == id).values(
        time=schedule_update.time,
        locationId=schedule_update.locationId,
        person_name=schedule_update.person_name
    )
    await database.execute(query)
    return await get_schedule(id)

async def delete_schedule(id: UUID):
    query = schedule_table.delete().where(schedule_table.c.id == id)
    await database.execute(query)
    
async def get_schedules_by_person_name(person_name: str):
    query = schedule_table.select().where(schedule_table.c.person_name == person_name)
    return await database.fetch_all(query)

