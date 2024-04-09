import requests
def load_data_from_url(url):
    response = requests.get(url)    
    data = response.json()
    return data

# data = load_data_from_url("https://jsonplaceholder.typicode.com/users")
# https://example.org/my.json
# if data:
#     print(data)

import json
def load_data_from_file(filename):
    file_path = 'Makers/Extension_Challenges/' + filename
    with open(file_path) as my_file: 
        data = json.load(my_file)
        return data
    
# data = load_data_from_file('test.json')
# if data:
#     print(data)


def get_films_by_director(filename, director):
    file_path = 'Makers/Extension_Challenges/' + filename
    with open(file_path) as my_file: 
        movies_list= json.load(my_file)

        films_by_director = []
        for movie_dict in movies_list:
            if movie_dict['director'] == director:
                films_by_director.append(movie_dict['name'])
    
    return films_by_director


# data = get_films_by_director("test.json", "Frank Darabont")
# if data:
#     print(data)


def get_films_by_actor(filename, desired_actor):
    file_path = 'Makers/Extension_Challenges/' + filename
    with open(file_path) as my_file: 
        movies_list= json.load(my_file)

        films_by_actor = []
        for movie_dict in movies_list:
            if desired_actor in movie_dict['stars']:
                films_by_actor.append(movie_dict['name'])
    
    return films_by_actor

# data = get_films_by_actor("test.json", 'James Caan')
# if data:
#     print(data)



def get_films_with_minimum_rating(filename, rating):
    file_path = 'Makers/Extension_Challenges/' + filename
    with open(file_path) as my_file: 
        movies_list= json.load(my_file)

        films_by_actor = []
        for movie_dict in movies_list:
            if movie_dict['imdb_rating'] >= rating:
                films_by_actor.append(movie_dict['name'])
    
    return films_by_actor

# data = get_films_with_minimum_rating("test.json", 9.3)
# if data:
#     print(data)


def get_films_within_year_range(filename, start_year, end_year):
    file_path = 'Makers/Extension_Challenges/' + filename
    with open(file_path) as my_file: 
        movies_list= json.load(my_file)

        films_within_year_range = []
        for movie_dict in movies_list:
            if movie_dict['year'] in range(start_year, end_year):
                films_within_year_range.append(movie_dict['name'])
    
    return films_within_year_range

# data = get_films_within_year_range("test.json", 1994, 1996)
# if data:
#     print(data)



def order_films_chronologically(filename):
    file_path = 'Makers/Extension_Challenges/' + filename
    with open(file_path) as my_file: 
        movies_list= json.load(my_file)

        # extract all years in a list
        films_years = []
        for movie_dict in movies_list:
            films_years.append(movie_dict['year'])

        # sort list chronologically
        films_years = sorted(films_years)

        # loop throught the list and create new list with film name for each year
        result = []
        for year in films_years:
            for movie_dict in movies_list:
                if movie_dict['year'] == year:
                    result.append(movie_dict['name'])
        
        print(result)

        return result

# data = order_films_chronologically("test.json")
# if data:
#     print(data)


def order_films_most_recent_first(filename):
    file_path = 'Makers/Extension_Challenges/' + filename

    with open(file_path) as my_file: 
        movies_list= json.load(my_file)

        # extract all years in a list
        films_years = []
        for movie_dict in movies_list:
            films_years.append(movie_dict['year'])

        # sort list chronologically
        films_years = sorted(films_years, reverse=True)

        # loop throught the list and create new list with film name for each year
        result = []
        for year in films_years:
            for movie_dict in movies_list:
                if movie_dict['year'] == year:
                    result.append(movie_dict['name'])

        return result
    
# data = order_films_most_recent_first("test.json")
# if data:
#     print(data)


def all_actors_starting_with_letter(filename, letter):
    file_path = 'Makers/Extension_Challenges/' + filename

    with open(file_path) as my_file: 
        movies_list= json.load(my_file)

        # extract all actors starting with the specified letter in a list
        actors = []
        for movie_dict in movies_list:
            for actor in movie_dict['stars']:
                if actor.lower()[0] == letter:
                    actors.append(actor)

        # sort list chronologically
        actors = sorted(actors)
        # remove duplicates
        actors = list(dict.fromkeys(actors))

        return actors

data = all_actors_starting_with_letter("test.json", 'a')
if data:
    print(data)