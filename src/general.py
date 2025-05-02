from ossapi import Ossapi, GameMode
from src.config import API_ID, API_SECRET, API_CALLBACK

commands = {
    '!h': "help",
    '!c': "config",
    '!s': "scorepost",
    '!r': "recommend"
}

def initApi():
    # input api key info from config, should be int/str/str
    client_id = API_ID
    client_secret = API_SECRET
    callback_url = API_CALLBACK

    return Ossapi(client_id, client_secret, callback_url)

def startUpInput():
    # dict of all mode types
    mode_types = {
        'STD': GameMode.OSU,
        'MANIA': GameMode.MANIA,
        'CATCH': GameMode.CATCH,
        'TAIKO': GameMode.TAIKO
    }
    # below asks user input
    name = input("Hi! Welcome to fun-erino, the tillerino ripoff! Please enter your osu! user: ")
    mode = mode_types.get(input("Input gamemode - STD, MANIA, CATCH, TAIKO: "))
    print("Thank you! These settings can be changed at any time with the command !c. You can also use !h to " \
    "display all available commands.")

    return name, mode

def printHelp():
    for command in commands:
        print(command, "-", commands.get(command))