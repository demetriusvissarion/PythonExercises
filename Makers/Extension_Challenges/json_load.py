import requests
import json
def load_data_from_url(url):
    response = requests.get(url)    
    data = response.json()
    return data

data = load_data_from_url("https://jsonplaceholder.typicode.com/users")
# https://example.org/my.json
if data:
    print(data)