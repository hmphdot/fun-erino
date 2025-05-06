from src.general import commands, initApi, startUpInput, printHelp
from src.scorepost import askInput, generateScorepost
from src.recommend import recommendationParams, findRecommendation, printRecommendations

# authenticate the api, get user data
api = initApi()
subject = startUpInput(api)

# infinite loop to continually get user input
while True:
    userCommand = commands.get(input().lower())
    match userCommand:
        case "help":
            printHelp()
        case "config":
            subject = startUpInput()
        case "scorepost":
            postType = askInput()
            generateScorepost(api, subject, postType)
        case "recommend":
            mods, playstyle = recommendationParams()
            titles, recs = findRecommendation(api, subject, mods, playstyle)
            printRecommendations(titles, recs)
        case "exit":
            print("See you next time!")
            quit()
        case _:
            print("Sorry, I don't know what to do with the above command.")