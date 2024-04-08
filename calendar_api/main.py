from fastapi import FastAPI, HTTPException, Depends, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from schemas import Schedule
from typing import List
from database import database
from routes.schedule_routes import router as schedule_router
import logging
import crud

from logger import setup_logger

setup_logger()

# Define startup and shutdown event handlers
async def startup_event():
    logging.info("Application startup")
    await database.connect()

async def shutdown_event():
    logging.info("Application shutdown")
    await database.disconnect()

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

app.include_router(schedule_router)


#@app.on_event("startup")
#async def startup():
#    await database.connect()

#@app.on_event("shutdown")
#async def shutdown():
#    await database.disconnect()

# LIST ALL SCHEDULES
@app.get("/v1/schedules", response_model=List[Schedule], dependencies=[Depends(validate_token)])
async def list_schedules() -> List[Schedule]:
    logging.info("Listing all schedules")
    return await crud.get_schedules()

# CREATE SCHEDULE
@app.post("/v1/schedules", response_model=Schedule, status_code=201, dependencies=[Depends(validate_token)])
async def create_schedule(schedule: Schedule):
    logging.info(f"Creating a new schedule: {schedule}")
    return await crud.create_schedule(schedule)

# GET SCHEDULE
@app.get("/v1/schedule/{schedule_id}", response_model=Schedule, dependencies=[Depends(validate_token)])
async def get_schedule(schedule_id: str) -> Schedule:
    logging.info(f"Retrieving schedule with ID: {schedule_id}")
    schedule = await crud.get_schedule(schedule_id)
    if schedule is None:
        logging.warning(f"Schedule not found: ID {schedule_id}")
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule

# UPDATE SCHEDULE
@app.put("/v1/schedule/{schedule_id}", response_model=Schedule, dependencies=[Depends(validate_token)])
async def update_schedule(schedule_id: str, schedule_update: Schedule):
    logging.info("Updating schedule with ID: %s", schedule_id)
    updated_schedule = await crud.update_schedule(schedule_id, schedule_update)
    if updated_schedule is None:
        logging.warning(f"Failed to update: Schedule not found with ID {schedule_id}")
        raise HTTPException(status_code=404, detail="Schedule not found")
    return updated_schedule

# DELETE SCHEDULE
@app.delete("/v1/schedule/{schedule_id}", status_code=204, dependencies=[Depends(validate_token)])
async def delete_schedule(schedule_id: str):
    logging.info(f"Attempting to delete schedule with ID: {schedule_id}")
    await crud.delete_schedule(schedule_id)
    return Response(status_code=204)
