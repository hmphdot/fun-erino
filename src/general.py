from ossapi import Ossapi, UserLookupKey
from src.config import API_ID, API_SECRET, API_CALLBACK

commands = {
    '!h': "help",
    '!c': "config",
    '!s': "scorepost",
    '!r': "recommend",
    '!x': "exit"
}

def initApi():
    # input api key info from config, should be int/str/str
    client_id = API_ID
    client_secret = API_SECRET
    callback_url = API_CALLBACK

    return Ossapi(client_id, client_secret, callback_url)

def startUpInput(api):
    # below asks user input
    name = input("Hi! Welcome to fun-erino, the tillerino ripoff! Please enter your osu! user: ")
    print("Thank you! The input user can be changed at any time with the command !c. You can also use !h to " \
    "display all available commands.")
    print("Current gamemode is user's default; support for changing will be added in the future.")
    subject = api.user(user=name, key=UserLookupKey.USERNAME)

    return subject

def printHelp():
    for command in commands:
        print(command, "-", commands.get(command))