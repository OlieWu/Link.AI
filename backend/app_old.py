from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
import spotipy
import os

from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

# Retrieve environment variables
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Setup Spotify client credentials
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


def get_song_recommendations(sp, seed_genres, target_features):
    # Request only the top 10 recommendations
    recommendations = sp.recommendations(
        seed_genres=seed_genres, limit=10, **target_features)
    recommended_tracks = []

    for track in recommendations['tracks']:
        recommended_tracks.append(
            (track['name'], track['artists'][0]['name'], track['external_urls']['spotify']))

    return recommended_tracks


# Define seed genres and target features for the recommendations
seed_genres = ['pop', 'rap', 'edm', 'indie']  # Example genres
target_features = {
    'target_energy': 0.7,
    'target_loudness': -5.0,
    'target_danceability': 0.8,
    'target_liveness': 0.3,
    'target_valence': 0.75,
    'target_instrumentalness': 0.0
}


# target_features = {
#     'target_energy': 0.3,
#     'target_valence': 0.2,
#     'target_danceability': 0.4,
#     'target_loudness': -10,
#     'target_liveness': 0.1,
#     'target_tempo': 100,
#     'target_instrumentalness': 0.1
# }

# seed_genres = ['sad', 'acoustic', 'piano', 'ballads']

# Fetch song recommendations based on the specified parameters
res = get_song_recommendations(sp, seed_genres, target_features)


collection.update_one(
    {'username': 'olieoil'},
    {'$set': {'API_recs': []}}
)

update_result = collection.update_one(
    {'username': 'olieoil'},
    {'$push': {'API_recs': {'$each': res}}}
)

for song in res:
    print(f"{song[0]} by {song[1]}")
