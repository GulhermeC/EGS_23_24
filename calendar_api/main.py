from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from schemas import Schedule
from typing import List
from database import database
from routes.schedule_routes import router as schedule_router
import logging

from logger import setup_logger

setup_logger()

# Define startup and shutdown event handlers
async def startup_event():
    logging.info("Application startup")

async def shutdown_event():
    logging.info("Application shutdown")

# Initialize FastAPI with lifespan event handlers
app = FastAPI(on_startup=[startup_event], on_shutdown=[shutdown_event])

# Setup token authentication
security = HTTPBearer()
def validate_token(auth: HTTPAuthorizationCredentials = Depends(security)):
    if auth.credentials != "8ecadf46-9364-4e3a-b79d-182d6a259a75":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or expired token"
        )

# Mock database
db: List[Schedule] = []

app.include_router(schedule_router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/v1/schedules", response_model=List[Schedule], dependencies=[Depends(validate_token)])
async def list_schedules() -> List[Schedule]:
    """List all schedules.

    Returns:
        List[Schedule]: List of all schedules in the database
    """
    logging.info("Listing all schedules")
    return db

@app.post("/v1/schedules", response_model=Schedule, status_code=201, dependencies=[Depends(validate_token)])
async def create_schedule(schedule: Schedule):
    """Create a new schedule.

    Args:
        schedule (Schedule): New schedule to be created

    Returns:
        Schedule: Created schedule
    """
    logging.info(f"Creating a new schedule: {schedule}")
    db.append(schedule)  # type: ignore
    return schedule

@app.get("/v1/schedule/{schedule_id}", response_model=Schedule, dependencies=[Depends(validate_token)])
async def get_schedule(schedule_id: str) -> Schedule:
    """Retrieve a specific schedule by ID.

    Args:
        schedule_id (str): ID of the schedule to be retrieved

    Returns:
        Schedule: Schedule found in the database

    Raises:
        HTTPException: With status code 404 if schedule not found
    """
    logging.info(f"Retrieving schedule with ID: {schedule_id}")
    for schedule in db:
        if schedule.id == schedule_id:
            return schedule
    logging.warning(f"Schedule not found: ID {schedule_id}")
    raise HTTPException(status_code=404, detail="Schedule not found")

@app.put("/v1/schedule/{schedule_id}", response_model=Schedule, dependencies=[Depends(validate_token)])
async def update_schedule(schedule_id: str, schedule_update: Schedule):
    """Update a schedule by ID.

    Args:
        schedule_id (str): ID of the schedule to be updated
        schedule_update (Schedule): Updated schedule data

    Returns:
        Schedule: Updated schedule

    Raises:
        HTTPException: With status code 404 if schedule not found
    """
    logging.info("Updating schedule with ID: %s", schedule_id)
    for i, schedule in enumerate(db):
        if schedule.id == schedule_id:
            db[i] = schedule_update
            logging.info("Updated schedule %s to %s", schedule_id, schedule_update)
            return schedule_update
    logging.warning("Failed to update: Schedule not found with ID %s", schedule_id)
    raise HTTPException(status_code=404, detail="Schedule not found")

@app.delete("/v1/schedule/{schedule_id}", status_code=204, dependencies=[Depends(validate_token)])
async def delete_schedule(schedule_id: str):
    """Deletes a schedule by ID.

    Args:
        schedule_id (str): ID of the schedule to be deleted
    """
    logging.info("Attempting to delete schedule with ID: %s", schedule_id)
    for i, schedule in enumerate(db):
        if schedule.id == schedule_id:
            del db[i]
            logging.info("Deleted schedule with ID: %s", schedule_id)
            return
    logging.warning("Failed to delete: Schedule not found with ID %s", schedule_id)
    raise HTTPException(status_code=404, detail="Schedule not found")
