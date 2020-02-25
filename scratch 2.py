# import json
# import requests

# url = "https://api-v3.igdb.com/games"

# payload = "fields name,platforms, release_dates, cover;\nsearch \"final fantasy\";\nlimit 50;"
# headers = {
#   'user-key': '97bc20f840f5a7f739642f1b0615bb37',
#   'Content-Type': 'application/json'
# }

# response = requests.get(url, headers=headers, data = payload)


# json_data = requests.get(url, headers=headers, data=payload).json()

# for game in json_data:
#     print(game['name'])
 


import json
# import requests

# url= 'https://api-v3.igdb.com/games'
# headers= {'user-key': '97bc20f840f5a7f739642f1b0615bb37'}
# payload = "fields name,platforms, release_dates, cover;\nsearch \"final\";\nlimit 50;"
# json_data = requests.get(url, headers=headers, data=payload).json()


# print(type(json_data))

# for game in json_data:
#     print(game['name'], game['cover'])


import requests

search = input('Search: ')

url = 'https://api-v3.igdb.com/games'
headers = {
    'user-key':'97bc20f840f5a7f739642f1b0615bb37',
    'Accept': 'application/json'
}

data = 'fields name; limit 10; search "{0}";'.format(search)

json_data = requests.get(url=url, headers=headers, data=data).json()

print(type(json_data))

for game in json_data:
    print(game['name'])