-- Create user table
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL default 1
);

-- Creating some default test users
INSERT INTO user (
    first_name,
    last_name,
    hobbies
    ) VALUES (
    "Alex",
    "Garcia",
    "Running"
    );

INSERT INTO user (
    first_name,
    last_name,
    hobbies
    ) VALUES (
    "Mickey",
    "Felps",
    "Swimming"
    );

INSERT INTO user (
    first_name,
    last_name,
    hobbies
    ) VALUES (
    "Albert",
    "Eint",
    "Math"
    );