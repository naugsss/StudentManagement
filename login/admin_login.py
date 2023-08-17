import json

from controller.display_marks import display_student_marks
from utils.authentication import Verify
from helper.prompt_menu_functions import prompt_add_data, prompt_delete_data, prompt_list_data, prompt_update_data, \
    prompt_search_data, prompt_student_marks


def menu():
    print("Which operation you wish to perform : ")

    print("1. Add a new student.")
    print("2. Enter marks of a student.")
    print("3. Delete an existing student.")
    print("4. Update details of a student.")
    print("5. Search for a student.")
    print("6. List all the student.")
    print("7. Display marks list")
    print("8. Exit.")
    print(" ")
    user_input = input("Enter a number : ")
    admin_menu(user_input)


def admin_display():
    admin = Verify()
    admin.get_details()
    value = admin.verify_data("admin")
    if value:
        menu()


def admin_menu(number):
    if number == '1':
        prompt_add_data()
    elif number == '2':
        prompt_student_marks()
    elif number == '3':
        prompt_delete_data()
    elif number == '4':
        prompt_update_data()
    elif number == '5':
        prompt_search_data()
    elif number == '6':
        prompt_list_data()
    elif number == '7':
        display_student_marks()
    elif number == '8':
        return
    else:
        print("Wrong input, please try again.")
        menu()
    menu()
