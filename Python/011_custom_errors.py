
# this is also sufficient to have a class to inherit from another class
# class MyCustomError(TypeError):
#    pass

# class MyCustomError_with_code(Exception:
# you dont have to use TypeError or other predifined Error types. You could use a generic one called Exception

class MyCustomError_with_code(TypeError):
    """
    Here you can describe you function purpose
    In a multi line string
    And this is called a DocString
    """
    def __init__(self, message, code):
        super().__init__(f'The error code : {code} with message : {message}')
        self.code = code

raise MyCustomError_with_code('This is the error message', 500)

# DocString is a special text added in a form of a multiline string and can be added to the begining of a file
# or bellow a class, or method or function.
# Its purpose is to describe them, and there are special reports that extarct all DocString for documentation purposes

