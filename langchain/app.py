from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
from flask import Flask, request
from werkzeug.utils import secure_filename
import spotipy
import os
from recommend import final_recommend
from mood_evaluation import mood_eval
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

# Configure the app
load_dotenv()
app = Flask(__name__)
api_key = os.environ["GOOGLE_API_KEY"]



# Define the upload_file function
@app.route('/upload', methods=['POST'])
def upload_file():
    try: 
        if 'file' not in request.files:
            return 'No file part in the request.', 400

        file = request.files['file']

        if file.filename == '':
            return 'No selected file.', 400

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join('/path/to/save/files', filename)
            file.save(file_path)

            # Call your function to process the file
            # For example, if you're using genai.upload_file:
            display_name = filename
            file_response = genai.upload_file(path=file_path, display_name=display_name)

            return 'File uploaded and processed successfully.', 200
    except Exception as e:
        return f'An error occurred: {e}', 500

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

text_mood = "happy"
text_music_types = ['pop', 'rap', 'edm', 'indie']  # Example genres
text_more_details = "I like upbeat songs with a catchy melody"
temp_image_name = "sea.jpg"


target_features, seed_genres, environment_description = mood_eval(text_mood, text_music_types, text_more_details, temp_image_name)

# # Example target features

# # target_features = {
# #     'target_energy': 0.3,
# #     'target_valence': 0.2,
# #     'target_danceability': 0.4,
# #     'target_loudness': -10,
# #     'target_liveness': 0.1,
# #     'target_tempo': 100,
# #     'target_instrumentalness': 0.1
# # }


# seed_genres = ['sad', 'acoustic', 'piano', 'ballads']

# Fetch song recommendations based on the specified parameters
res = get_song_recommendations(sp, text_music_types, target_features)


collection.update_one(
    {'username': 'olieoil'},
    {'$set': {'API_recs': []}}
)

update_result = collection.update_one(
    {'username': 'olieoil'},
    {'$push': {'API_recs': {'$each': res}}}
)


final = final_recommend("olieoil", environment_description, text_mood, text_music_types, text_more_details)
print("final: " )

for song in res:
    print(f"{song[0]} by {song[1]}")
