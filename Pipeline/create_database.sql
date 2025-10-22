DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS logins;

CREATE TABLE IF NOT EXISTS users (

[user_id] INTEGER PRIMARY KEY AUTOINCREMENT,
[first_name] TEXT NOT NULL,
[surname] TEXT NOT NULL,
[middle_initials] TEXT,
[dob] DATE,
[age_last_birthday] INTEGER,
[favourite_colour] TEXT,
[favourite_animal] TEXT,
[favourite_food] TEXT,
[gender] TEXT,
[password] TEXT,
[city] TEXT,
[county] TEXT,
[postcode] TEXT,
[email] TEXT NOT NULL UNIQUE,
[phone] TEXT,
[mobile] TEXT,
[rqf] TEXT,
[salary] INTEGER,
[website_visits_last_30_days] INTEGER
);

Create Table if not Exists logins(
[login_id] integer PRIMARY KEY AUTOINCREMENT,
[username] TEXT NOT NULL,
[login_timestamp] datetime NOT NULL
)