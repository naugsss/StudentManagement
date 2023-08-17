from helper.prompt_menu_functions import prompt_list_data, prompt_search_data
from utils.authentication import Verify


def menu():
    print(" ")
    print("Select the operation you wish to perform : ")
    print(" ")
    print("1. List all the student ")
    print("2. Search for any specific student ")
    print("3. Exit ")
    user_input = int(input("Enter your choice : "))
    student_menu(user_input)


def student_display():
    student = Verify()
    student.get_details()
    value = student.verify_data("student")
    if value:
        menu()


def student_menu(user_input):
    if user_input == 1:
        prompt_list_data()
    elif user_input == 2:
        prompt_search_data()
    elif user_input == 3:
        return
    else:
        print("Wrong input, please try again.")
    menu()
