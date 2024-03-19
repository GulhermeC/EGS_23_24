from fastapi import FastAPI, HTTPException
from models import Schedule
from typing import List
import logging

from logger import setup_logger

setup_logger()

# Define startup and shutdown event handlers
async def startup_event():
    logging.info("Application startup")

async def shutdown_event():
    logging.info("Application shutdown")

app = FastAPI()

# Attach lifespan event handlers
app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)

# Mock database
db: List[Schedule] = []

@app.get("/v1/schedules", response_model=List[Schedule])
async def list_schedules():
    logging.info("Listing all schedules")
    return db

@app.post("/v1/schedules", response_model=Schedule, status_code=201)
async def create_schedule(schedule: Schedule):
    logging.info(f"Creating a new schedule: {schedule}")
    db.append(schedule)
    return schedule

@app.get("/v1/schedule/{schedule_id}", response_model=Schedule)
async def get_schedule(schedule_id: str):
    logging.info(f"Retrieving schedule with ID: {schedule_id}")
    for schedule in db:
        if schedule.id == schedule_id:
            return schedule
    logging.warning(f"Schedule not found: ID {schedule_id}")
    raise HTTPException(status_code=404, detail="Schedule not found")

@app.put("/v1/schedule/{schedule_id}", response_model=Schedule)
async def update_schedule(schedule_id: str, schedule_update: Schedule):
    logging.info(f"Updating schedule with ID: {schedule_id}")
    for i, schedule in enumerate(db):
        if schedule.id == schedule_id:
            db[i] = schedule_update
            return schedule_update
    logging.warning(f"Failed to update: Schedule not found with ID {schedule_id}")
    raise HTTPException(status_code=404, detail="Schedule not found")

@app.delete("/v1/schedule/{schedule_id}", status_code=204)
async def delete_schedule(schedule_id: str):
    logging.info(f"Attempting to delete schedule with ID: {schedule_id}")
    for i, schedule in enumerate(db):
        if schedule.id == schedule_id:
            del db[i]
            return
    logging.warning(f"Failed to delete: Schedule not found with ID {schedule_id}")
    raise HTTPException(status_code=404, detail="Schedule not found")
