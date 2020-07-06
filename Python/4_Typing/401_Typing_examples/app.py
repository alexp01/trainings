from typing import List,Dict
import sqlite3

Book = Dict(str, Union(str,int))

def func_that_has_no_return() -> None: # We add the type that is returned so that if this fct is assigned to a var it wil give a warning
    print('There is no return in this function')

def funct_that_returns_a_list_of_dict () -> List[Dict]: # List and Dict exists in the Typing package
    return [{'a':1, 'b':2}]

def function_with_param (name: str, age : int) -> int:
    if age > 100
        return 1
    else:
        return 0

def db_connection() -> sqlite3.Connection: # we must return a Connection class type variable
    return sqlite3.connect()

var1 = func_that_has_no_return()
print(var1)

print (funct_that_returns_a_list_of_dict())

print(function_with_param(4,5)) # the first argument has a yellow backgroun, wth a warning also, than its a int and not a str

connection1_var = db_connection()

