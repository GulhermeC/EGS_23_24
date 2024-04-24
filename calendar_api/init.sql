CREATE TABLE IF NOT EXISTS schedules (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  time TIMESTAMP,
  "locationId" VARCHAR,
  person_name VARCHAR
);
