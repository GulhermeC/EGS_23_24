from sqlalchemy import Column, String, DateTime, create_engine, MetaData, Table
from databases import Database

metadata = MetaData()

schedule_table = Table(
    "schedules",
    metadata,
    Column("id", String, primary_key=True),
    Column("time", DateTime),
    Column("locationId", String),
    Column("person_name", String)
)

DATABASE_URL = "postgresql://calendar:password123@localhost/calendar"
database = Database(DATABASE_URL)
