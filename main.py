from ossapi import Ossapi
from src.config import API_ID, API_SECRET, API_CALLBACK # type: ignore
from src.general import startUpInput
from src.scorepost import askInput, generateScorepost
from src.recommend import recommendationParams, findRecommendation, printRecommendations

# todo (general)
#   help command that lists all possible inputs
#   recommend command that lists fun maps (whole point of the bot)
#   command that allows you to swap user

# todo (specific to this file)
#   create interface (or interact with IRC) so its not cli
#   dict with all commands from src/
#   make a while (true) loop that continually asks for commands until bot is shut off

# input api key info from config, should be int/str/str
client_id = API_ID
client_secret = API_SECRET
callback_url = API_CALLBACK

# authenticate the api, get user data
api = Ossapi(client_id, client_secret, callback_url)
id, mode = startUpInput()

postType = askInput()
generateScorepost(api, id, postType, mode)