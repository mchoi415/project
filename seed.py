from sqlachemy import func
from model import User
from model import Game
from model import Review
from datetime import datetime

from model import connect_to_db, connect_to_db
from server import app

import json
url= 'https://api-v3.igdb.com/games'
headers= {'userkey': '97bc20f840f5a7f739642f1b0615bb37'}

