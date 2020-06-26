def read_from_file(file_name):
    with open(file_name , 'r') as file:
        return file.readlines()

def write_to_file(text_to_write, file_name):
    with open(file_name, 'w') as file:
        file.write(text_to_write)