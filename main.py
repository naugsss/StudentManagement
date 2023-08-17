import json
from login.admin_login import admin_display
from login.student_login import student_display
from utils.database_connection import DatabaseConnection


def create_book_table():
    with DatabaseConnection('C:\\Users\\anaugaraiya\PycharmProjects\pythonProject\student_data.db') as connection:
        # now the below set of statements are inside the context manager block
        # this creates a new variable connection, and then we use that to create cursor
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS student_data(uid integer primary key, name text, email text, '
                       'number integer)')


create_book_table()

print("***********  Student Management System  ***********")


def menu():
    print("Do you want to login as Admin or Student ")
    print("if you wish to exit, please type exit")


menu()
user_input = input("Enter your choice: admin, student or exit : ")

while user_input != 'exit':
    if user_input == 'admin':
        admin_display()
    elif user_input == 'student':
        student_display()
    else:
        print("Wrong input made, please try again.")
    menu()
    user_input = input("Enter your choice: admin, student or exit : ")

