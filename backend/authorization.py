from dotenv import load_dotenv
import os
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'], methods=['GET',
     'POST'], allowed_headers=['Content-Type', 'Authorization'])
app.config['CORS_HEADERS'] = 'Content-Type'

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = "http://localhost:5000/callback"
SPOTIFY_SCOPES = ["user-library-read", "user-top-read", "user-read-recently-played",
                  "playlist-read-private", "playlist-read-collaborative", "user-read-private", "user-read-email"]

global_data = {
    "sp_oauth": SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=SPOTIFY_SCOPES
    )
}


@app.route('/login', methods=['GET'])
def login():
    auth_url = global_data["sp_oauth"].get_authorize_url()
    return jsonify({"url": auth_url})


@app.route('/callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    token_info = global_data["sp_oauth"].get_access_token(code)
    global_data['sp'] = spotipy.Spotify(auth=token_info['access_token'])
    return redirect('http://localhost:3000')


@app.route('/get-liked-songs', methods=['GET'])
def get_liked_songs():
    if 'sp' in global_data:
        tracks = global_data['sp'].current_user_saved_tracks()
        # Extracting a simple list of track names and artists for example
        track_list = [{'name': item['track']['name'], 'artist': item['track']
                       ['artists'][0]['name']} for item in tracks['items']]
        return jsonify(track_list)
    return jsonify({'error': 'Spotify client not initialized'}), 500


if __name__ == '__main__':
    app.run(debug=True)
