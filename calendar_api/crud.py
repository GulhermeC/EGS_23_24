from database import database
from schemas import Schedule
from models import schedule_table

async def get_schedules():
    query = schedule_table.select()
    return await database.fetch_all(query)

async def create_schedule(schedule: Schedule):
    query = schedule_table.insert().values(
        id=schedule.id,  # This is the primary key
        time=schedule.time,
        locationId=schedule.locationId,
        person_name=schedule.person_name  # Ensure this is included in your schema and passed here
    )
    last_record_id = await database.execute(query)
    return {**schedule.dict(), "id": schedule.id}  # Return with id

async def get_schedule(id: str):
    query = schedule_table.select().where(schedule_table.c.id == id)
    return await database.fetch_one(query)

async def update_schedule(id: str, schedule: Schedule):
    query = schedule_table.update().where(schedule_table.c.id == id).values(
        time=schedule.time,
        locationId=schedule.locationId,
        person_name=schedule.person_name  # Make sure to update this field if it's being changed
    )
    await database.execute(query)
    return {**schedule.dict(), "id": id}

async def delete_schedule(id: str):
    query = schedule_table.delete().where(schedule_table.c.id == id)
    await database.execute(query)
    
async def get_schedules_by_person_name(person_name: str):
    query = schedule_table.select().where(schedule_table.c.person_name == person_name)
    return await database.fetch_all(query)

