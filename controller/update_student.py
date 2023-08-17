import json

from utils.database import update_student_data


def update_data():
    user_input = input("Enter the user id of the user in which you wish to make changes : ")
    if len(user_input) != 0:
        print("Enter the updated values for the following : ")

        name = input("Name : ")
        email = input("Email : ")
        number = input("Number : ")

        update_student_data(user_input, name, email, number)
    else:
        print("Please enter valid input")
        update_data()