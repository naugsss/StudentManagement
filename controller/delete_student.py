import json

from utils.database import delete_student_data


def delete_data():
    user_input = input("Enter the user ID which you want to delete : ")
    delete_student_data(user_input)
