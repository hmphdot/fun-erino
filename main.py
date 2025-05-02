from ossapi import Ossapi
from src.general import commands, initApi, startUpInput, printHelp
from src.scorepost import askInput, generateScorepost
from src.recommend import recommendationParams, findRecommendation, printRecommendations

# authenticate the api, get user data
api = initApi()
id, mode = startUpInput()

# infinite loop to continually get user input
while True:
    userCommand = commands.get(input())
    match userCommand:
        case "help":
            printHelp()
        case "config":
            id, mode = startUpInput()
        case "scorepost":
            postType = askInput()
            generateScorepost(api, id, postType, mode)
        case "recommend":
            mods, playstyle = recommendationParams()
            recs = findRecommendation(mods, playstyle)
            printRecommendations(recs)
        case "exit":
            print("See you next time!")
            quit()
        case _:
            print("Sorry, I don't know what to do with the above command.")