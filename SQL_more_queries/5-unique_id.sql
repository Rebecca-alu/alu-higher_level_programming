-- creates the table unique_id, id has a default value of 1 and must be unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
