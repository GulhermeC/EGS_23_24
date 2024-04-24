from sqlalchemy import Column, DateTime, String, MetaData, Table
from sqlalchemy.dialects.postgresql import UUID
from databases import Database
import uuid

metadata = MetaData()

schedule_table = Table(
    "schedules",
    metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("time", DateTime),
    Column("locationId", String),
    Column("person_name", String)
)

DATABASE_URL = "postgresql://calendar:password123@localhost/calendar"
database = Database(DATABASE_URL)
