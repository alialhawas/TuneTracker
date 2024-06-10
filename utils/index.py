from typing import Dict
from datetime import datetime, timedelta

from database.redis.index import get_redis_connection
from database.posgres.index import write_top_artists, write_top_songs

import requests
import os


redis_con = get_redis_connection()

def gen_auth_token() -> tuple[str, datetime]:
    return 'none', datetime.now() # TODO genrate token 


def test():
    return 90

def is_within_30_minutes(dt1: datetime, dt2: datetime) -> bool:
    time_difference = abs(dt1 - dt2)    
    return time_difference < timedelta(minutes=30)


def write_auth_token(token_value:str) -> None:
    expiration_time = (datetime.now() + timedelta(hours=1 , minutes= 30)).isoformat()  

    redis_con.hset('auth_tokens', 'token', token_value)
    redis_con.hset('auth_tokens', 'expiration_time', expiration_time)


def get_auth_token() -> tuple[str, datetime]:
    token = redis_con.hget('auth_tokens', 'token')
    expiration_time = redis_con.hget('auth_tokens', 'expiration_time')

    token = token.decode('utf-8') if token else None 
    expiration_time = expiration_time.decode('utf-8') if expiration_time else None

    if token is None or expiration_time is None:
        token, expiration_time = gen_auth_token()

    expiration_time_dt = datetime.fromisoformat(expiration_time)

    if is_within_30_minutes(expiration_time_dt, datetime.now()):
        token, expiration_time = gen_auth_token()
        expiration_time_dt = datetime.fromisoformat(expiration_time)

    return token, expiration_time_dt


def get_token_data (client_id: str, client_secret: str)  -> str:
    return {
    "grant_type": "client_credentials",
    "client_id": client_id, 
    "client_secret": client_secret
}

def get_header (token: str) -> Dict[str,str]:
    return {
    'Authorization': f'Bearer {token}'
}

def get_token_header() -> str:
    return {
    "Content-Type": "application/x-www-form-urlencoded"
}

def get_token (client_id: str, client_secret: str) -> str:
    res = requests.post( os.getenv['url_token'], headers=get_token_header(), data=get_token_data(client_id, client_secret))
    if res.status_code == 200:
        data = res.json()
        write_auth_token(data['access_token'], data['expires_in'])
        return data['access_token']
    else:
        raise Exception(f"Request failed with status code {res.status_code} |  condictent get token")


async def get_top_artists (token: str) -> Dict:
    res = requests.get(os.getenv['url_top_artists'], headers=get_header(token))
    if res.status_code == 200:
        return res.json()
    else:
        raise Exception(f"Request failed with status code {res.status_code} |  condictent get top artists")
    

async def get_top_songs (token: str) -> Dict:
    res = requests.get(os.getenv['url_top_songs'], headers=get_header(token))
    if res.status_code == 200:
        return res.json()
    else:
        raise Exception(f"Request failed with status code {res.status_code} |  condictent get top artists")
    


async def fetech_request(client_id: str, client_secret: str) -> Dict:
    """
    this def fetch all request of the client from the spotify api
    """
    token = get_auth_token(client_id, client_secret)


    top_artists = get_top_artists(token)
    top_songs = get_top_songs(token)

    write_top_artists(top_artists)
    write_top_songs(top_songs)


    return {
        "artists":  top_artists,
        "songs": top_songs
    }