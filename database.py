import sqlite3
from sqlite3 import Error

DATABASE = 'books.db'

def create_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Error as e:
        print(e)

def create_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                book_name TEXT,
                date_started DATE,
                date_ended DATE,
                rating INTEGER
            )
        ''')
        conn.commit()
        conn.close()
    except Error as e:
        print(e)

def insert_book(book_name, date_started, date_ended, rating):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO books (book_name, date_started, date_ended, rating)
            VALUES (?, ?, ?, ?)
        ''', (book_name, date_started, date_ended, rating))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)

def fetch_all_books():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        conn.close()
        return books
    except Error as e:
        print(e)

def fetch_book(book_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books WHERE id=?', (book_id,))
        book = cursor.fetchone()
        conn.close()
        return book
    except Error as e:
        print(e)

def update_book(book_id, book_name, date_started, date_ended, rating):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE books
            SET book_name=?, date_started=?, date_ended=?, rating=?
            WHERE id=?
        ''', (book_name, date_started, date_ended, rating, book_id))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)

def delete_book(book_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
        conn.commit()
        conn.close()
    except Error as e:
        print(e)
