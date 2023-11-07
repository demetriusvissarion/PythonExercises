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

data = get_films_by_actor("test.json", 'James Caan')
if data:
    print(data)