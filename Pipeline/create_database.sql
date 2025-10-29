DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS logins;

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    surname TEXT NOT NULL,
    middle_initials TEXT,
    dob DATE,
    age_last_birthday INTEGER,
    favourite_colour TEXT,
    favourite_animal TEXT,
    favourite_food TEXT,
    gender TEXT,
    password TEXT NOT NULL,
    city TEXT,
    county TEXT,
    postcode TEXT,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    mobile TEXT,
    rqf TEXT,
    education TEXT,
    salary REAL,
    currency CHAR(3) CHECK(currency IN ('GBP', 'EUR')) NOT NULL,
    website_visits_last_30_days INTEGER,
    country_code CHAR(2) CHECK(country_code IN ('UK', 'FR')) NOT NULL
);

CREATE TABLE IF NOT EXISTS logins (
    login_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    login_timestamp DATETIME
);