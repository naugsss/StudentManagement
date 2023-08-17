from utils.database_connection import DatabaseConnection

PATH = 'C:\\Users\\anaugaraiya\PycharmProjects\pythonProject\student_data.db'


def create_marks_table():
    with DatabaseConnection(PATH) as connection:
        # now the below set of statements are inside the context manager block
        # this creates a new variable connection, and then we use that to create cursor
        cursor = connection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS student_marks (uid integer primary key, physics integer, chemistry integer, maths integer, english integer)')


def validate_student(uid):
    with DatabaseConnection(PATH) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM student_data WHERE uid = ?', (uid,))
        user_details = cursor.fetchone()

        if user_details is None:
            print("No such student exists.")
            print("")
            return False
        return True


def add_marks(uid, physics, chemistry, maths, english):
    with DatabaseConnection(PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM student_marks WHERE uid = ?', (uid,))
        user_details = cursor.fetchone()
        if user_details is None:
            cursor.execute('INSERT INTO student_marks VALUES(?,?,?,?,?)', (uid, physics, chemistry, maths, english))
            print("Marks added successfully")
            print("")
        else:
            cursor.execute('UPDATE student_marks set physics = ?, chemistry = ?, maths = ?, english = ? where uid = ?', (physics, chemistry, maths, english, uid))
            print("Marks added successfully")
            print("")


def marks_data():
    create_marks_table()
    uid = input("Enter user ID of the student : ")
    value = validate_student(uid)
    if not value:
        return
    print("Enter marks in each of the following subject")
    physics = int(input("Physics : "))
    while physics > 100 or physics < 0:
        print("Please enter valid marks in between 0 and 100")
        physics = int(input("Physics : "))

    chemistry = int(input("Chemistry : "))
    while chemistry > 100 or chemistry < 0:
        print("Please enter valid marks in between 0 and 100")
        chemistry = int(input("Chemistry : "))

    maths = int(input("Maths : "))
    while maths > 100 or maths < 0:
        print("Please enter valid marks in between 0 and 100")
        physics = int(input("Maths : "))

    english = int(input("English : "))
    while english > 100 or english < 0:
        print("Please enter valid marks in between 0 and 100")
        physics = int(input("English : "))
    add_marks(uid, physics, chemistry, maths, english)
