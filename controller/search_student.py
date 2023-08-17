import json

from utils.database import search_student_data


def search_data():
    user_input = input("Enter the user id of the student whom you want to search : ")

    student = search_student_data(user_input)

    if student is None:
        print("There is no such student with uid", user_input)
    else:
        print(student)
