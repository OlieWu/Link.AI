from dotenv import load_dotenv
import os
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import json
from recommend import final_recommend
from mood_evaluation import mood_eval

load_dotenv()
app = Flask(__name__)

# Retrieve environment variables
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')


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
    ),
    "username": ""
}

# Setup Spotify client credentials (app.py code)
client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = os.getenv('MONGO_URI')  # Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['Searchify']  # Select the 'Searchify' database
collection = db['userData']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


@app.route('/login', methods=['GET'])
def login():
    auth_url = global_data["sp_oauth"].get_authorize_url()
    return jsonify({"url": auth_url})


@app.route('/callback', methods=['GET'])
def callback():
    try:
        code = request.args.get('code')
        token_info = global_data["sp_oauth"].get_access_token(code)
        sp = spotipy.Spotify(auth=token_info['access_token'])
        global_data['sp'] = sp

        # Ensure MongoDB client setup is optimal (consider moving this to global initialization)
        MONGO_URI = os.getenv("MONGO_URI")
        client = MongoClient(MONGO_URI)
        db = client.Searchify
        user_data_collection = db.userData

        # Fetch user's Spotify username
        user_profile = sp.current_user()
        username = user_profile['display_name']
        global_data["username"] = username

        # Fetch and prepare user's liked songs (limit to 10)
        liked_songs = sp.current_user_saved_tracks(limit=10)
        liked_songs_list = [{
            'name': track['track']['name'],
            'artist': track['track']['artists'][0]['name'],
            'link': track['track']['external_urls']['spotify']
        } for track in liked_songs['items']]

        # Fetch and prepare user's recently played songs (limit to 10)
        recently_played = sp.current_user_recently_played(limit=10)
        recently_played_list = [{
            'name': track['track']['name'],
            'artist': track['track']['artists'][0]['name'],
            'link': track['track']['external_urls']['spotify']
        } for track in recently_played['items']]

        # Create a document for the user in MongoDB
        user_data_collection.insert_one({
            'username': username,
            'API_recs': [],
            'liked_songs': liked_songs_list,
            'recently_played': recently_played_list
        })

        return redirect('http://localhost:3000')
    except Exception as e:
        print(f"Error during callback processing: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500


# Define seed genres and target features for the recommendations
@app.route('/recommendations', methods=['POST'])
def recommendations():
    data = request.get_json()
    mood = data["mood"]
    music_types = data["musicTypes"]
    special_requirements = data["specialRequirements"]


    # TODO: Get image from the MongoDB. Oliver Wu can do this
    image_name = collection.find_one()

    username = global_data["username"]

    target_features, seed_genres, environment_description = mood_eval(mood, music_types, special_requirements, image_name)

    # Fetch song recommendations based on the specified parameters
    res = get_song_recommendations(sp, music_types, target_features)

    collection.update_one(
        {'username': username},
        {'$set': {'API_recs': []}}
    )

    update_result = collection.update_one(
        {'username': username},
        {'$push': {'API_recs': {'$each': res}}}
    )

    final = final_recommend(username, environment_description, mood, music_types, special_requirements)
    # print("final: " )

    # for song in final:
    #     print(f"{song[0]} by {song[1]}")

    # TODO: verify that final is a JSON
    return json.loads(final)


def get_song_recommendations(sp, seed_genres, target_features):
    # Request only the top 10 recommendations
    recommendations = sp.recommendations(
        seed_genres=seed_genres, limit=10, **target_features)
    recommended_tracks = []

    for track in recommendations['tracks']:
        recommended_tracks.append(
            (track['name'], track['artists'][0]['name'], track['external_urls']['spotify']))

    return recommended_tracks




if __name__ == '__main__':
    app.run(debug=True)
