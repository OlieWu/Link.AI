import getpass
import os
import requests
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")

# System Prompt New Summarization Chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
llm = ChatGoogleGenerativeAI(model='gemini-pro')


# def text_summarziation(pdfurl: str = None):
#     prompt = PromptTemplate.from_template('Answer only a numerical probabillity. Evaluate the probability that this person with following post like {topic}: {input_text}')
#     chain = LLMChain(
#         llm=llm,
#         prompt=prompt,
#         verbose=True
#     )

#     topic = 'sushi'
#     input_text = ' I got the Soft Shell Crab roll, and WOW was that probably the best sushi I’ve had in years. Super reasonably priced, tasty, and great presentation as well. Service was great, the vibes were immaculate, would highly recommend coming here. I certainly will be coming again'
#     response = chain.invoke({"topic": topic, "input_text": input_text})
#     # response = chain.invoke(topic=topic, input_text=input_text)
#     return response



class GeminiProChain:
    def __init__(self, llm):
        self.llm = llm

    def invoke(self, input_text):
        prompt = PromptTemplate.from_template(
            "Imagine you are now a new reporter reading news and trying to summarize them. You should output your result to be neutral and concise. Limit to 100 words. News Content: {input_text}"
        )
        chain = LLMChain(llm=self.llm, prompt=prompt, verbose=True)
        response = chain.invoke({"input_text": input_text})
        return response

# Usage 
chain = GeminiProChain(llm=llm)

response = chain.invoke(input_text)

print(response.text)
