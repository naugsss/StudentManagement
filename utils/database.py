import sqlite3
from .database_connection import DatabaseConnection

PATH = 'C:\\Users\\anaugaraiya\PycharmProjects\pythonProject\student_data.db'


def create_book_table():
    with DatabaseConnection(PATH) as connection:
        # now the below set of statements are inside the context manager block
        # this creates a new variable connection, and then we use that to create cursor
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS student_data(uid integer primary key, name text, email text, '
                       'phone integer)')


def add_student_data(uid, name, email, phone):
    with DatabaseConnection(PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM student_data WHERE uid = ?', (uid,))
        user_details = cursor.fetchone()

        if user_details is None:
            cursor.execute('INSERT INTO student_data VALUES(?,?,?,?)', (uid, name, email, phone))
            print("Student added successfully")
        else:
            print("This user ID already exists. Please enter different user ID")


def delete_student_data(uid):
    with DatabaseConnection(PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM student_data WHERE uid = ?', (uid,))
        student_data = cursor.fetchone()
        # print(student_data)
        if student_data is None:
            print("No such student exists.")
            return
        else:
            cursor.execute('DELETE FROM student_data WHERE uid = ?', (uid,))
            print("Student deleted successfully.")


def list_student_data():
    with DatabaseConnection(PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM student_data')
        student_data = cursor.fetchall()
        if len(student_data) == 0:
            print("No records found, please insert some data. ")
        else:
            for student in student_data:
                print(f"UID:{student[0]}, Name:{student[1]}, email: {student[2]}, Phone:{student[3]}")


def search_student_data(uid):
    with DatabaseConnection(PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM student_data WHERE uid = ?', (uid,))
        student = cursor.fetchone()
        # if student is None:
        #     print("No such student exists.")
        #     return False
        return student


def update_student_data(uid, name, email, number):
    with DatabaseConnection(PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM student_data WHERE uid = ?', (uid,))
        student_details = cursor.fetchone()
        if student_details is None:
            print("No such student exists.")
            return
        else:
            cursor.execute('UPDATE student_data SET name = ?, email = ?, number = ? WHERE uid = ?',
                       (name, email, number, uid,))
