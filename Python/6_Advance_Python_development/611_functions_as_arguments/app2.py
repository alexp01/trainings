
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/18514856#questions
# Another examples of functions as argument

movies = [
    {"name" : "Matrix", "director" : "Dir1"},
    {"name" : "Titanic", "director" : "Dir2"},
    {"name" : "French connection", "director" : "Dir3"},
    {"name" : "Asterix", "director" : "Dir4"}
]

def find_novie(expected, finder):
    found = []
    for movie in movies:
        if expected == finder(movie):
            found .append(movie)
    return found

find_by = input('What property do you search movie|director :_')
looking_for = input('What are you looking for :_')
movies_var = find_novie(looking_for, lambda movie: movie[find_by])

print(movies_var or 'No movie found')