CREATE TABLE IF NOT EXISTS schedules (
  id VARCHAR PRIMARY KEY,
  time TIMESTAMP,
  "locationId" VARCHAR,
  person_name VARCHAR
);
