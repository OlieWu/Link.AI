import getpass
import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
import nest_asyncio
from langchain_community.document_loaders.mongodb import MongodbLoader
from langchain_google_genai import ChatGoogleGenerativeAI

nest_asyncio.apply()
load_dotenv(find_dotenv(), override=True)

# Load the API info from the environment
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass(
        "Enter your Google API key: ")


loader = MongodbLoader(
    connection_string=os.getenv("MONGODB_CONNECTION_STRING"),
    db_name="Searchify",
    collection_name="userData",
    filter_criteria={"name": "user1"},
    field_names=["API_recs", "liked_songs", "recently_played"],
)

JSON_format = {
    "song1": {
        "title": "title1",
        "artist": "artist1",
        "link": "link1"
    },
    "song2": {
        "title": "title2",
        "artist": "artist2",
        "link": "link2"
    },
    "song3": {
        "title": "title3",
        "artist": "artist3",
        "link": "link3"
    },
    "song4": {
        "title": "title4",
        "artist": "artist4",
        "link": "link4"
    },
    "song5": {
        "title": "title5",
        "artist": "artist5",
        "link": "link5"
    }
}

# Recommend the song list based on the mood, music types, and more details. Pick both new songs and existing songs


def recommend(environment_description, text_mood, text_music_types, text_more_details):
    llm = ChatGoogleGenerativeAI(model='gemini-pro')

    song_list = loader.load()  # Load the song list from the database
    prompt = PromptTemplate.from_template(
        "Imagine you are now a professional musician, and you want to make some song recommendations to your friend based on your current mood and environment. Output in the following JSON format: {JSON_format}. Follow the guidance and number limit on API info: {api_info}."
        "Imagine that you can see : {environment_description}. You are in a mood of: {text_mood}. You like these music types: {text_music_types}. More details: {text_more_details}."
        "Please provide five song recommendation based on the above information pick from the following list. {song_list}"
    )
    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=False
    )

    response = chain.invoke({"environment_description": environment_description, "text_mood": text_mood,
                            "text_music_types": text_music_types, "text_more_details": text_more_details, "song_list": song_list})
    return response


def final_recommend(text_mood, text_music_types, text_more_details):

    # Recommend the song list based on the mood, music types, and more details
    response = recommend(text_mood, text_music_types, text_more_details)

    response_JSON = response['text']
    return response_JSON


song_list = loader.load()  # Load the song list from the database
print(song_list)
