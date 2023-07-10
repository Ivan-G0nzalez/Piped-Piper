import sqlite3 as db

class SQLiteConnection:
    
    def __init__(self, database_path) -> None:
        self.database_path = database_path
        self.connection = None

    def __enter__(self):
        # return the reference of the file open
        self.connection = db.connect(self.database_path)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        # output
        if self.connection:
            self.connection.close()  