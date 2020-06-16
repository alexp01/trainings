# https://www.udemy.com/course/the-complete-python-course/learn/lecture/18470984#overview

movie_list = [
    {
        "Name" : "Matrix",
        "Year" : "1999",
        "Director" : "Lana Wachowski",
        "location" : "R4",
        "Position" : "34"
    },
    {
        "Name": "Titanic",
        "Year": "1997",
        "Director": "James Cameron",
        "location": "R1",
        "Position": "02"
    },
    {
        "Name": "Fight Club",
        "Year": "1999",
        "Director": "David Fincher",
        "location": "R4",
        "Position": "78"
    }
]


def find_year(year_to_search):
    found_by_year = 0
    for movie in movie_list:
        if movie["Year"] == year_to_search:
            found_by_year = 1
            print (f"The movie { movie['Name']} is from the {movie['Year']} year")
    print ("\n")
    return found_by_year

def add_movie():
    name_movie = input ("1. Movie name : \n_")
    name_year = input("1. Movie year : \n_")
    name_director = input("1. Movie diector : \n_")
    name_location = input("1. Movie location : \n_")
    name_Position = input("1. Movie position : \n_")
    dict2 =    {
        "Name": name_movie,
        "Year": name_year,
        "Director": name_director,
        "location": name_location,
        "Position": name_Position
                }
    movie_list.append (dict2)

def delete_movie(index_movie):
    del movie_list[index_movie]

def find_director(director_to_search):
    found_by_year = 0
    for movie in movie_list:
        if director_to_search.lower() in movie["Director"].lower():
            found_by_year = 1
            print (f"The movie { movie['Name']} has {movie['Director']} as Director")
    return found_by_year



input_text = "        MENU OPTION ->  Pres 1 to ADD, 2 to REMOVE, 3 to Search and Q gor QUIT \n_"
get_option = input(input_text)
while get_option != "Q":
    if get_option == "1":
        add_movie()
        last = len(movie_list)
        print(f"\n The last added movie to the colection is {movie_list[last-1]}\n")
    elif get_option == "2":
        index_movie = int(input ("Give the index of the movie that you want to delete /n_"))
        delete_movie(index_movie)
        print(f"We have deleted the movie with index {index_movie}\n The list of movies is \n {movie_list}")
    elif get_option == "3":
        input_text_for_search = "       SUBMENU OPTION 3 (Search) -> Search movie by Year of Director \n press 1 for  Year and 2 for Director \n OR Q for main menu \n_"
        get_option_for_search = input(input_text_for_search)
        while get_option_for_search != "Q":
            if get_option_for_search == "1":
                year_to_search = input("\nWhat year ? :_  ")
                found_by_year = find_year(year_to_search)
                if found_by_year == 0:
                    print ("\n We could not find any movie with your criteria")
                else:
                    print (f"\n We found {found_by_year} movies matching your criterias\n")
            elif get_option_for_search == "2":
                director_to_search = input("\nWhat Director ? - ")
                find_director(director_to_search)
            else:
                print("We could not find any movie with your criteria")
            get_option_for_search = input(input_text_for_search)
    else: print("unknown command")
    get_option = input(input_text)






