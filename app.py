from contextlib import asynccontextmanager
import string
import random
import os
import requests

from typing import Union
from urllib.parse import urlencode 

from fastapi import FastAPI
from fastapi.responses import RedirectResponse








@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)





@app.get("/fetch_data")
def fetch_data():
    return get



@app.get("/login")
def login():

    N = 16

    state = ''.join(random.choices(string.ascii_lowercase +
							string.digits, k=N))

    scope = 'user-read-private user-read-email'

    params = {
        'response_type': 'code',
        'client_id': os.getenv['CLIENT_ID'],
        'scope': scope,
        'redirect_uri': os.getenv['REDIRECT_URI'],
        'state': state
    }

    query_string = urlencode(params)

    url = f"https://www.example.com?{query_string}"


    return RedirectResponse(url=url)