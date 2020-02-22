import json
import requests

url= 'https://api-v3.igdb.com/games'
headers= {'user-key': '97bc20f840f5a7f739642f1b0615bb37'}
args = {'fields': '*'}
res = requests.get(url, headers=headers, params=args)

games = json.loads(res.text)

with open("games.json", "w") as data_file:
    json.dump(games, data_file, indent=2)