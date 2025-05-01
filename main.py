from ossapi import Ossapi

# input api key info, should be int/str/str
client_id = None
client_secret = None
callback_url = None

# authenticate the api
api = Ossapi(client_id, client_secret, callback_url)
