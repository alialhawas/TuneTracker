import requests
import json
import config 
import os 

from utils.index import get_token_header , get_top_artists



print(get_top_artists(os.getenv['access_token']))
