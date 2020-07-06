import sqlite3

Class DatabaseConnection:

    def __init__(self,db_name): # this will execute when the with line is executed
        self.db = db_name
        self.connection = None

    def __enter__(self): # this will execute after the with line is executed, when the body of the with is actually executed
        self.connection = sqlite3.connect(self.db)
        return  self.connection

    def __exit__(self,exec_type, exec_val, exec_tb): # this is axecuted after thebloc of the with is executed.
        self.connection.commit()
        self.connection.close()
