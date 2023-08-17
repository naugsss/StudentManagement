import sqlite3


class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    # enter method is used when we enter the context manager
    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    # exit method is used when we leave the context manager
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_type or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
