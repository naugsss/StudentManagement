from utils.database_connection import DatabaseConnection


PATH = 'C:\\Users\\anaugaraiya\PycharmProjects\pythonProject\student_data.db'


def display_student_marks():
    with DatabaseConnection(PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM student_marks')
        student_marks = cursor.fetchall()
        if len(student_marks) == 0:
            print("No records found, please insert some data. ")
        else:
            for student in student_marks:
                print(f"UID:{student[0]}, Physics:{student[1]}, Chemistry:{student[2]}, Maths: {student[3]}, English:{student[4]}")
