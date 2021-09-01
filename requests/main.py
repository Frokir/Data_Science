import requests
import json
name = input('User name: ')

r = requests.get(f'https://api.github.com/users/{name}/repos')

r = r.json()

list_of_repo = []
for el in r:
    list_of_repo.append(el['name'])


my_dict = {"user": name, "repo": list_of_repo}


json_obj = json.dumps(my_dict)

with open('data.json', 'w') as f:
    f.write(json_obj)
