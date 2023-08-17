import re

from controller.validate_data import validate_uid, validate_mobile_number, validate_email
from utils.database import add_student_data


class Student:
    def __init__(self):
        self.uid = any
        self.name = any
        self.phone = any
        self.email = any

    def add_data(self):
        print("Please enter the following details of the student : ")
        self.uid = input("Enter your user ID: ")
        while True:

            if validate_uid(self.uid):
                break
            else:
                print("Please input integers only")
                self.uid = input("Enter your user ID: ")

        self.name = input("Enter your name : ")
        self.phone = input("Enter your phone number : ")
        while True:

            if validate_mobile_number(self.phone):
                break
            else:
                print("You entered wrong phone number. Please try again.")
                self.phone = input("Enter your phone number : ")

        self.email = input("Enter your email id : ")
        while True:
            if validate_email(self.email):
                break
            else:
                print("You entered wrong email, please try again.")
                self.email = input("Enter your email id : ")

        if validate_email(self.email) and validate_mobile_number(self.phone):
            add_student_data(self.uid, self.name, self.email, self.phone)
