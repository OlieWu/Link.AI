from dotenv import load_dotenv
import os
import secrets
import asyncio
import hashlib
import base64
import flask
import string
import random
from urllib.parse import urlencode
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, jsonify
from flask_cors import CORS
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'], methods=['GET', 'POST'], allowed_headers=['Content-Type', 'Authorization'])
app.config['CORS_HEADERS'] = 'Content-Type'
SPOTIFY_REDIRECT_URI = "http://localhost:5000/callback" # TODO: update to our main app page
global_data = {
    "sp_oauth": None,
    "sp": None,
    "auth_url": None,
}

def generate_random_string(length):
  """Generates a random string of the specified length."""
  chars = string.ascii_letters + string.digits
  return ''.join(random.choice(chars) for _ in range(length))

@app.route('/login', methods=['GET'])
def login():
    load_dotenv()
    SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
    SPOTIFY_SCOPES = ["user-top-read", "user-read-recently-played", "playlist-read-private", "playlist-read-collaborative", "user-read-private", "user-read-email"]
    
    global_data["sp_oauth"] = SpotifyOAuth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, scope=SPOTIFY_SCOPES)
    global_data["auth_url"] = global_data["sp_oauth"].get_authorize_url()

    return jsonify({"url": global_data["auth_url"]})



@app.route('/callback', methods=['GET'])
def callback():
    # auth_url = global_data["sp_oauth"].get_authorize_url()
    code = global_data["sp_oauth"].parse_response_code(global_data["auth_url"])

    token_info = global_data["sp_oauth"].get_access_token(code)
    access_token = token_info['access_token']

    global_data["sp"] = spotipy.Spotify(auth=access_token)

    # TODO: do database action here
    print("hungry")

    return flask.redirect("/")


# def get_token():
#     load_dotenv()
#     client_id = os.getenv("CLIENT_ID")
#     client_secret = os.getenv("CLIENT_SECRET")
#     auth_string = client_id + ":" + client_secret
#     auth_bytes = auth_string.encode("utf-8")
#     auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

#     url = "https://accounts.spotify.com/api/token"
#     headers = {
#         "Authorization": "Basic " + auth_base64,
#         "Content-Type": "application/x-www-form-urlencoded"
#     }

#     data = {"grant_type": "client_credentials"}
#     result = post(url, headers=headers, data=data)
#     json_result = json.loads(result.content)
#     token = json_result["access_token"]

#     return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}