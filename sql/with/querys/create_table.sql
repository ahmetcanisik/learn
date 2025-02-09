-- Create a users table.

CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(24) UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password VARCHAR(24) NOT NULL,
    login_date DATETIME NOT NULL,
);

-- Create Customers table.

CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INT NOT NULL,
    country VARCHAR(5) NOT NULL
);