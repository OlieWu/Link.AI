from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import google.generativeai as genai
import getpass
import os
import json
from IPython.display import Image
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)
API_INFO_PATH = "/Users/edwin/Link.AI/langchain/recommendation_api_info.txt"

JSON_FORMAT = '''{
    Target_energy :
    Target_loudness :
    Target_dancebility :
    Target_liveness :
    Target_valence :
    Seed_genres :
    Target_instrumentalness :

}'''

# # Load the API info from the environment
# if "GOOGLE_API_KEY" not in os.environ:
#     os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")

api_key = os.environ["GOOGLE_API_KEY"]


# Get local images
'''
def get_image_path(image_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, "pic_database/" + image_name)
    return image_path
'''

# Get image from URL
def get_image_path():
    # Initialize Google API Client
    genai.configure(api_key=api_key)
    file_path = "sample_data/gemini_logo.png"

    display_name = "Gemini Logo"
    file_response = genai.upload_file(path=file_path, display_name=display_name)




def analyze_image(image_url):
    llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")

    # content = requests.get(image_url).content
    # Image(content)

    Image(image_url)

    # Call Gemini API to analyze the image
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": "To the best of your ability, descirbe the what's in this image or video as detailed as possible. Take a deep breath, you can do this!",
            },
            {"type": "image_url", "image_url": image_url},
        ]
    )
    results = llm.invoke([message])
    return results


def evalutaion(JSON_format, api_info, environment_description, text_mood, text_music_types, text_more_details):
    llm = ChatGoogleGenerativeAI(model='gemini-pro')
    prompt = PromptTemplate.from_template(
        "Imagine you are now a professional musician, and you want to provide some features to Spotify for song recommendations. Output in the following JSON format: {JSON_format}. Follow the guidance and number limit on API info: {api_info}."
        "Imagine that you can see : {environment_description}. You are in a mood of: {text_mood}. You like these music types: {text_music_types}. More details: {text_more_details}."
    )
    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=False
    )

    response = chain.invoke({"JSON_format": JSON_format, "api_info": api_info, "environment_description": environment_description,
                            "text_mood": text_mood, "text_music_types": text_music_types, "text_more_details": text_more_details})
    return response


def mood_eval(text_mood, text_music_types, text_more_details, image_name="sea.jpg"):

    try:

        image_path = get_image_path(image_name)  # get the image path locally

        # get the description from Gemini API
        environment_description = analyze_image(image_path)

        with open(API_INFO_PATH, 'r') as file:
            api_info = file.read()

        # Generate the evaluation result JSON based on the input
        response = evalutaion(JSON_FORMAT, api_info, environment_description,
                              text_mood, text_music_types, text_more_details)

        evaluation_result = response['text']

        evaluation_json = json.loads(evaluation_result)

        # Extracting the seed_genres and converting from a string to a list
        seed_genres = evaluation_json['Seed_genres'].split(', ')

        # Removing the seed_genres from json_data to isolate target_features
        del evaluation_json['Seed_genres']

        # The rest of the json_data dictionary is your target_features
        target_features = evaluation_json

        return target_features, seed_genres, environment_description

    except Exception as e:
        print(e)
        return None, None, None


# # Example usage
# response = mood_eval("happy", "pop, rock", "My favortiate singer is Taylor Swift.", "sea.jpg")
# print(response)

# Example response
'''
This is a photo of a small tropical island with white sand beaches and palm trees. 
The water is crystal clear and there is a small boat anchored in the foreground. 
In the background, a larger boat is sailing on the horizon. 
The sky is blue and there are some white clouds.
'''
# image_name = "sea.jpg"
# temp_text_mood = "happy"
# temp_text_music_types = "pop, rock"
# temp_text_more_details = "My favortiate singer is Taylor Swift."
