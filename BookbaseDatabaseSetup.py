import sqlite3

#Setting up the database

db = sqlite3.connect('liblary.db')
cursor = db.cursor()

#Creating the tables in the database

try:
    cursor.execute("""CREATE TABLE books (
            ID integer,
            Title text,
            Author integer,
            Subject integer,
            Owned bool,
            Read bool
        )""")
except sqlite3.OperationalError:
    pass
try:
    cursor.execute("""CREATE TABLE authors (
            ID integer,
            Author text
        )""")
except sqlite3.OperationalError:
    pass

try:
    cursor.execute("""CREATE TABLE subjects (
            ID integer,
            Subject text
        )""")
except sqlite3.OperationalError:
    pass
