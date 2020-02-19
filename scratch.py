import requests
import json

url = "https://api-v3.igdb.com/search"

payload = "fields game.name;\nsearch \"sonic\";"
headers = {
  'user-key': '97bc20f840f5a7f739642f1b0615bb37',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

games = json.loads(response.text)

for game in games:
    print(game)

