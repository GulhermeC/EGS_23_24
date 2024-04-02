from databases import Database

DATABASE_URL = "postgresql://user:password@localhost/calendar"
database = Database(DATABASE_URL)