import sqlite3

# all methods return none as default
# When block of WIth will be called, in case an error will happen, it will stil execute the dunder exit function.
# The 3 parameters in the exit dunder method, contain already information about the error
# To generate an error, just add the same book name to the DB

class DatabaseConnection:

    def __init__(self,db_name):
        self.db = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db)
        return  self.connection

    def __exit__(self,exec_type, exec_val, exec_tb): # If an error is raised in the With block, we just close the connection without commmiting.
        if exec_tb or exec_type or exec_val: # equivalent with exe_tb is not None etc...
            self.connection.close
            print('Info about the error parameters: \n')
            print('exec_type: {exec_type} \n')
            print('exec_val: {exec_val} \n')
            print('exec_tb: {exec_tb} \n')  # tb is from TraceBack
        else:
            self.connection.commit()
            self.connection.close()


