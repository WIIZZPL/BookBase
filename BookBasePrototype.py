import sqlite3

#Setting up the database

db = sqlite3.connect('liblary.db')
cursor = db.cursor()

#Creating the tables in the database

cursor.execute("""CREATE TABLE IF NOT EXISTS books (
        ID integer PRIMARY KEY,
        Title text NOT NULL,
        Author integer NOT NULL,
        Subject integer NOT NULL,
        Owned bool DEFAULT false,
        Read bool DEFAULT false
    )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS authors (
        ID integer PRIMARY KEY,
        Author text NOT NULL
    )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS subjects (
        ID integer PRIMARY KEY,
        Subject text NOT NULL
    )""")
