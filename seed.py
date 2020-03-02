# from sqlachemy import func
from model import User
from model import Game
from model import Review
from datetime import datetime

from model import connect_to_db, db

import json
import requests



def search_games(search):

    url = 'https://api-v3.igdb.com/games'
    headers = {
        'user-key':'97bc20f840f5a7f739642f1b0615bb37',
        'Accept': 'application/json'
    }

    data = 'fields name, platforms, genres, release_dates, cover; limit 50; search "{0}";'.format(search)

    json_data = requests.get(url=url, headers=headers, data=data).json()
    return json_data
    # print(type(json_data))

    for game in json_data:
        print(game['name'])


def get_game_by_id(game_id):

    url = 'https://api-v3.igdb.com/games'
    headers = {
        'user-key':'97bc20f840f5a7f739642f1b0615bb37',
        'Accept': 'application/json'
    }

    data = '''fields name, platforms, genres, release_dates, cover;
              where id = {0};
              limit 5;'''.format(game_id)
    print(data)

    json_data = requests.get(url=url, headers=headers, data=data).json()
    return json_data
    # print(type(json_data))

    for game in json_data:
        print(game['name'])    

def get_cover_url_by_id(igdb_id):
    """Get cover image from game's id."""
    print('id', igdb_id)
    url = 'https://api-v3.igdb.com/covers'
    headers = {
        'user-key':'97bc20f840f5a7f739642f1b0615bb37',
        'Accept': 'application/json'
    }

    data = '''fields url;
              where game = {0};
              limit 1;'''.format(igdb_id)

    image_url = requests.get(url=url, headers=headers, data=data).json()
    print('imageurl')
    print(image_url)

    image_url = image_url[0]
    image_url =image_url['url']
    return image_url


def get_genre(genre_ids):
    """Convert genre ID to genre"""
    genres =[]
    genre_list = {34:"Visual Novel",
                  33:"Arcade",
                  32:"Indie",
                  31:"Adventure",
                  30:"Pinball",
                  26:"Quiz/Trivia",
                  25:"Hack and slash/Beat 'em up",
                  24:"Tactical",
                  16:"Turn-based strategy (TBS)",
                  15:"Strategy",
                  14:"Sport",
                  13:"Simulator",
                  12:"Role-playing (RPG)",
                  11:"Real Time Strategy (RTS)",
                  10:"Racing",
                  9:"Puzzle",
                  8:"Platform",
                  7:"Music",
                  5:"Shooter",
                  4:"Fighting",
                  2:"Point-and-click"}

    for genre_id in genre_ids:
        genre = genre_list[genre_id]
        genres.append(genre)

    genres = str(genres).strip('[]')
    return genres


def get_released_date(game_availabe_unixs):
    """Convert unix timestamp into date"""
    game_avaiable_dates =[]

    for game_available_unix in game_availabe_unixs:
    
        timestamp = datetime.fromtimestamp(game_available_unix)
        game_available_dates = timestamp.strftime('%d-%m-%y %H:%M:%S')
        game_avaiable_dates.append(game_available_dates)

    game_available_dates = str(game_avaiable_dates).strip('[]')
    return game_available_dates

def get_console(console_ids):
    """Get Console from console ID"""

    consoles =[]
    consoles_list ={240:"Zeebo",
                    239:"Blu-ray Player",
                    238:"DVD Player",
                    237:"Sol-20",
                    236:"Exidy Sorcerer",
                    203:"Stadia",
                    170:"Google Stadia",
                    169:"Xbox Series X",
                    167:"PlayStation 5",
                    166:"Pokémon mini",
                    165:"PlayStation VR",
                    164:"Daydream",
                    163:"SteamVR",
                    162:"Oculus VR",
                    161:"Windows Mixed Reality",
                    160:"Nintendo eShop",
                    159:"Nintendo DSi",
                    158:"Commodore CDTV",
                    157:"NEC PC-6000 Series",
                    156:"Thomson MO5",
                    155:"Tatung Einstein",
                    154:"Amstrad PCW",
                    153:"Dragon 32/64",
                    152:"FM-7",
                    151:"TRS-80 Color Computer",
                    150:"Turbografx-16/PC Engine CD",
                    149:"PC-98",
                    148:"AY-3-8607",
                    147:"AY-3-8606",
                    146:"AY-3-8605",
                    145:"AY-3-8603",
                    144:"AY-3-8710",
                    143:"AY-3-8760",
                    142:"PC-50X Family",
                    141:"AY-3-8610",
                    140:"AY-3-8500",
                    139:"1292 Advanced Programmable Video System",
                    138:"VC 4000",
                    137:"New Nintendo 3DS",
                    136:"Neo Geo CD",
                    135:"Hyper Neo Geo 64",
                    134:"Acorn Electron",
                    133:"Philips Videopac G7000",
                    132:"Amazon Fire TV",
                    131:"Nintendo PlayStation",
                    130:"Nintendo Switch",
                    129:"Texas Instruments TI-99",
                    128:"PC Engine SuperGrafx",
                    127:"Fairchild Channel F",
                    126:"TRS-80",
                    125:"PC-8801",
                    124:"SwanCrystal",
                    123: "WonderSwan Color",
                    122:"Nuon",
                    121:"Sharp X68000",
                    120:"Neo Geo Pocket Color",
                    119:"Neo Geo Pocket",
                    118:"FM Towns",
                    117:"Philips CD-i",
                    116:"Acorn Archimedes",
                    115:"Apple IIGS",
                    114:"Amiga CD32",
                    113:"OnLive Game System",
                    112:"Microcomputer",
                    111:"Imlac PDS-1",
                    110:"PLATO",
                    109:"CDC Cyber 70",
                    108:"PDP-11",
                    107:"Call-A-Computer time-shared mainframe computer system",
                    106:"SDS Sigma 7",
                    105:"HP 3000",
                    104:"HP 2100",
                    103:"PDP-7",
                    102:"EDSAC",
                    101:"Ferranti Nimrod Computer",
                    100: "Analogue electronics",
                    99:"Family Computer (FAMICOM)",
                    98:"DEC GT40",
                    97:"PDP-8",
                    96:"PDP-10",
                    95: "PDP-1",
                    94:"Commodore Plus/4",
                    93:"Commodore 16",
                    92:"SteamOS",
                    91:"Bally Astrocade",
                    90:"Commodore PET",
                    89:"Microvision",
                    88:"Odyssey",
                    87:"Virtual Boy",
                    86:"TurboGrafx-16/PC Engine",
                    85:"Donner Model 30",
                    84:"SG-1000",
                    82:"Web browser",
                    80:"Neo Geo AES",
                    79:"Neo Geo MVS",
                    78:"Sega CD",
                    77:"Sharp X1",
                    75:"Apple II",
                    74:"Windows Phone",
                    73:"BlackBerry OS",
                    72:"Ouya",
                    71:"Commodore VIC-20",
                    70:"Vectrex",
                    69:"BBC Microcomputer System",
                    68:"ColecoVision",
                    67:"Intellivision",
                    66:"Atari 5200",
                    65:"Atari 8-bit",
                    64:"Sega Master System",
                    63:"Atari ST/STE",
                    62:"Atari Jaguar",
                    61:"Atari Lynx",
                    60:"Atari 7800",
                    59:"Atari 2600",
                    58:"Super Famicom",
                    57:"WonderSwan",
                    56:"WiiWare",
                    55:"Mobile",
                    53:"MSX2",
                    52:"Arcade",
                    51:"Family Computer Disk System",
                    50:"3DO Interactive Multiplayer",
                    49:"Xbox One",
                    48:"PlayStation 4",
                    47:"Virtual Console (Nintendo)",
                    46:"PlayStation Vita",
                    45:"PlayStation Network",
                    44:"Tapwave Zodiac",
                    42:"N-Gage",
                    41:"Wii U",
                    39:"iOS",
                    38:"PlayStation Portable",
                    37:"Nintendo 3DS",
                    36:"Xbox Live Arcade",
                    35:"Sega Game Gear",
                    34:"Android",
                    33:"Game Boy",
                    32:"Sega Saturn",
                    30:"Sega 32X",
                    29:"Sega Mega Drive/Genesis",
                    27:"MSX",
                    26:"ZX Spectrum",
                    25:"Amstrad CPC",
                    24:"Game Boy Advance",
                    23:"Dreamcast",
                    22:"Game Boy Color",
                    21:"Nintendo GameCube",
                    20:"Nintendo DS",
                    19:"Super Nintendo Entertainment System (SNES)",
                    18:"Nintendo Entertainment System (NES)",
                    16:"Amiga",
                    15:"Commodore C64/128",
                    14:"Mac",
                    13:"PC DOS",
                    12:"Xbox 360",
                    11:"Xbox",
                    9:"PlayStation 3",
                    8:"PlayStation 2",
                    7:"PlayStation",
                    6:"PC (Microsoft Windows)",
                    5:"Wii",
                    4:"Nintendo 64",
                    3:"Linux"}

    for console_id in console_ids:
        console = consoles_list[console_id]
        consoles.append(console)

    consoles = str(consoles).strip('[]')

    return consoles

# def get_cover(cover_id):
#     """Get cover from cover ID"""








 