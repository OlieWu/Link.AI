import getpass
import os
import requests
from IPython.display import Image
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)
API_INFO_PATH = "/Users/edwin/Link.AI/langchain/recommendation_api_info.txt"


if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


def get_image_path(image_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, "pic_database/" + image_name)
    return image_path

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

    response = chain.invoke({"JSON_format": JSON_format, "api_info": api_info, "environment_description": environment_description, "text_mood": text_mood, "text_music_types": text_music_types, "text_more_details": text_more_details})
    return response

JSON_format = '''{
    Target_energy :
    Target_loudness :
    Target_dancebility :
    Target_liveness :
    Target_valence :
    Seed_genres :
    Target_instrumentalness :

}'''

# image_name = "sea.jpg"
# image_path = get_image_path(image_name)
# results = analyze_image(llm, image_path)
# print(results.content)
# Example response 
'''
This is a photo of a small tropical island with white sand beaches and palm trees. 
The water is crystal clear and there is a small boat anchored in the foreground. 
In the background, a larger boat is sailing on the horizon. 
The sky is blue and there are some white clouds.
'''

temp_results_content = '''
This is a photo of a small tropical island with white sand beaches and palm trees. 
The water is crystal clear and there is a small boat anchored in the foreground. 
In the background, a larger boat is sailing on the horizon. 
The sky is blue and there are some white clouds.
'''
temp_text_mood = "happy"
temp_text_music_types = "pop, rock"
temp_text_more_details = "My favortiate singer is Taylor Swift."

with open(API_INFO_PATH, 'r') as file:
    api_info = file.read()

response = evalutaion(JSON_format, api_info, temp_results_content, temp_text_mood, temp_text_music_types, temp_text_more_details)     

print(response)
