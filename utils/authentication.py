import hashlib
import pwinput
from utils.database_connection import DatabaseConnection

PATH = 'C:\\Users\\anaugaraiya\PycharmProjects\pythonProject\student_data.db'


def create_book_table():
    with DatabaseConnection(PATH) as connection:
        # now the below set of statements are inside the context manager block
        # this creates a new variable connection, and then we use that to create cursor
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS authentication_details(username text primary key, password text, '
                       'user_type text)')


create_book_table()


def encrypt_password(password):
    password = password.encode()
    sha256 = hashlib.sha256()
    sha256.update(password)
    string_hash = sha256.hexdigest()
    return string_hash


def create_account(username, password, user_type):
    with DatabaseConnection(PATH) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO authentication_details VALUES(?,?,?)',
                       (username, encrypt_password(password), user_type))
        print("Account created successfully")


class Verify:
    def __init__(self):
        self.username = any
        self.password = any
        self.user_type = any

    def get_details(self):
        self.username = input("Enter your username : ")
        # self.password = input("Enter your password : ")
        self.password = pwinput.pwinput(prompt="Enter your password: ", mask="*")

    def verify_data(self, user_type):
        self.user_type = user_type

        with DatabaseConnection(PATH) as connection:
            cursor = connection.cursor()
            if user_type == "admin":
                cursor.execute('SELECT * FROM authentication_details WHERE user_type = ?', ("admin",))
                user_details = cursor.fetchone()
                if user_details is None:
                    create_account(self.username, self.password, self.user_type)
                    print("User account created")
                else:
                    if user_details[0] == self.username and user_details[1] == encrypt_password(self.password):
                        return True
                    elif user_details[0] != self.username:
                        print("You are not an admin. Login as student")
                        return False
                    else:
                        print("You entered wrong password.")
                        return False

            cursor.execute('SELECT * FROM authentication_details WHERE username = ?', (self.username,))
            user_details = cursor.fetchone()
            if user_details is None:
                create_account(self.username, self.password, self.user_type)
                print("User account created")
            else:
                if self.username == user_details[0] and encrypt_password(self.password) != user_details[1]:
                    print("This user name has already been taken or you are entering wrong password.")
                    print("Please try again")
                    # self.get_details()

                elif self.username != user_details[0] or encrypt_password(self.password) != user_details[
                    1] or self.user_type != \
                        user_details[2]:
                    print("You entered wrong credentials.")
                    print("Please try again. ")
                    # self.get_details()

                else:
                    return True
