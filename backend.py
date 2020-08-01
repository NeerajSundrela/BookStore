import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(" CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)")
    conn.commit()
    conn.close()

def add(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def update(ids,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,ids))
    conn.commit()
    conn.close()

def delete(ids):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(ids,))
    conn.commit()
    conn.close()

def viewall():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=? ",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
# add("3 mistakes","chetan",2010,5643)
# add("love story","ravinder",2012,6533)
# print(viewall())