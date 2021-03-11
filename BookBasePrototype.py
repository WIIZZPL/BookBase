import sqlite3

#Setting up the database

db = sqlite3.connect('liblary.db')
cursor = db.cursor()

#Creating the tables in the database

cursor.execute("""CREATE TABLE IF NOT EXISTS books (
        ID INTEGER PRIMARY KEY,
        Title TEXT NOT NULL,
        Author INTEGER NOT NULL,
        Subject INTEGER NOT NULL,
        Owned bool DEFAULT false,
        Read bool DEFAULT false
    )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS authors (
        ID INTEGER PRIMARY KEY,
        Author TEXT NOT NULL
    )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS subjects (
        ID INTEGER PRIMARY KEY,
        Subject TEXT NOT NULL
    )""")
cursor.execute("""CREATE VIEW IF NOT EXISTS liblary AS
        SELECT A.ID, A.Title, A.Author, subjects.Subject, A.Owned, A.Read FROM
            (SELECT books.ID, books.Title, authors.Author, books.Subject, books.Owned, books.Read FROM books LEFT JOIN authors ON books.Author = authors.ID) AS A
            LEFT JOIN subjects ON A.Subject = subjects.ID
    """)

cursor.execute("INSERT INTO authors (Author) VALUES ('Robert')")
cursor.execute("INSERT INTO authors (Author) VALUES ('Benjamin')")
cursor.execute("INSERT INTO authors (Author) VALUES ('Vicky')")
cursor.execute("INSERT INTO authors (Author) VALUES ('Ika')")
cursor.execute("INSERT INTO subjects (Subject) VALUES ('Finance')")
cursor.execute("INSERT INTO subjects (Subject) VALUES ('Cooking')")
cursor.execute("INSERT INTO subjects (Subject) VALUES ('Philosophy')")
cursor.execute("INSERT INTO subjects (Subject) VALUES ('Drama')")
cursor.execute("INSERT INTO books (Title, Author, Subject, Owned, Read) VALUES ('Rich dad Poor dad', 1, 1, True, True)")
cursor.execute("INSERT INTO books (Title, Author, Subject, Owned, Read) VALUES ('Inteligent Investor', 2, 1, True, False)")
cursor.execute("INSERT INTO books (Title, Author, Subject, Owned, Read) VALUES ('Life or moeny', 3, 1, False, True)")
cursor.execute("INSERT INTO books (Title, Author, Subject, Owned, Read) VALUES ('Kawa', 4, 2, False, False)")

def listAuthors():
    print("ID - Author")
    cursor.execute("SELECT * FROM authors")
    for i in cursor.fetchall():
        print("{ID} - {Author}".format(ID=i[0], Author=i[1]))

def listSubjects():
    print("ID - Author")
    cursor.execute("SELECT * FROM subjects")
    for i in cursor.fetchall():
        print("{ID} - {Subject}".format(ID=i[0], Subject=i[1]))

def listLiblary():
    print("ID - Title - Author - Subject - Owned - Read")
    cursor.execute("""SELECT * FROM liblary""")
    for i in cursor.fetchall():
        print("{ID} - {Title} - {Author} - {Subject} - {Owned} - {Read}".format(ID=i[0], Title=i[1], Author=i[2], Subject=i[3], Owned=i[4], Read=i[5]))

listAuthors()
listSubjects()
listLiblary()
