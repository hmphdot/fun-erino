from ossapi import Ossapi
from src.config import API_ID, API_SECRET, API_CALLBACK # type: ignore
from src.scorepost import askInput, generateScorepost

# input api key info from config, should be int/str/str
client_id = API_ID
client_secret = API_SECRET
callback_url = API_CALLBACK

# authenticate the api
api = Ossapi(client_id, client_secret, callback_url)

id, postType, mode = askInput()
generateScorepost(api, id, postType, mode)