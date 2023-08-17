from controller.add_marks import marks_data
from controller.add_student import Student
from controller.delete_student import delete_data
from controller.list_student import list_data
from controller.search_student import search_data
from controller.update_student import update_data


def prompt_add_data():
    student = Student()
    student.add_data()


def prompt_delete_data():
    delete_data()


def prompt_list_data():
    list_data()


def prompt_update_data():
    update_data()


def prompt_search_data():
    search_data()


def prompt_student_marks():
    marks_data()
