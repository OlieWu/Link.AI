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
input_text  = ''' 
Ford is recalling more than 40,000 SUVs for fuel leak issues
Paul Hoskin
Thu, April 11, 2024 at 6:07 PM EDT·3 min read
1

A Ford sign is shown at a dealership in Springfield, Pa., Tuesday, April 26, 2022.  Ford is recalling nearly 43,000 small SUVs, Wednesday, April 10, 2024, because gasoline can leak from the fuel injectors onto hot engine surfaces, increasing the risk of fires. But the recall remedy does not include repairing the fuel leaks.
A Ford sign is shown at a dealership in Springfield, Pa., Tuesday, April 26, 2022. Ford is recalling nearly 43,000 small SUVs, Wednesday, April 10, 2024, because gasoline can leak from the fuel injectors onto hot engine surfaces, increasing the risk of fires. But the recall remedy does not include repairing the fuel leaks. | Matt Rourke
The Ford Motor Company has issued a recall affecting close to 43,000 SUVs.

According to The Associated Press, some of the company’s Escape SUVs from 2022 and Bronco Sport SUVs from 2022 and 2023 are getting recalled due to concerns about their fuel injectors.

“Ford says in documents filed with U.S. safety regulators that fuel injectors can crack, and gasoline or vapor can accumulate near ignition sources, possibly touching off fires,” The Associated Press reported.

How Ford is treating the issue
The recall — which affects 42,652 vehicles that have 1.5-liter engines — will aim to remedy the cracked fuel injectors, per Autoblog. Specifically, it will involve installing a drain tube “to redirect any leaking fuel from the engine to the ground” in addition to installing a software update that adds “fuel injector leak detection to the engine control unit.”

The Associated Press reported that the software will monitor for “a pressure drop” in the fuel injection system. If it observes one, it will “disable the high pressure fuel pump, reduce engine power and cut temperatures in the engine compartment.”

The fuel injectors are mostly staying
In an email sent to The Associated Press, Ford explained that it’s not completely replacing the fuel injectors because it believes the planned repairs “will prevent the failure from occurring and protect the customer.” Additionally, the updated software will notify drivers via a dashboard warning if there’s an issue, allowing them to stop and arrange for help.

A report filed by Ford to the National Highway Traffic Safety Administration, or NHTSA, says that only about 1% of the recalled vehicles are estimated to have the defect.

“The company says in documents it has reports of five under-hood fires and 14 warranty replacements of fuel injectors, but no reports of crashes or injuries,” per The Associated Press.

The company says it will extend its warranty coverage for cracked fuel injectors. Details of the extension will be made available in June, but owners who experience the issue can get replacements.

Affected owners were notified by letter starting on April 1, according to The Associated Press

Other Ford recalls
The SUV recall, according to The Associated Press, extends from a 2022 Ford recall centered on the same issue.

That past SUV recall was much bigger, involving more than half a million Bronco Sport and Escape vehicles. The current recall was put in place when Ford realized the problem applied “to more vehicles than previously thought,” per Consumer Reports.

USA Today reported last week on a separate recall affecting Ford’s 2023 and 2024 Transit vehicles. The NHTSA report claimed on these cars said that tires “may contact the front wheel arch liner and body flange,” causing damage to them. As damaged tires may lose air pressure or tread separation, a driver could “lose control of the vehicle and increase the risk of a crash.”

Ford didn’t share a resolution for the recall by the time that NHTSA released its report. Interim letters were mailed out on March 27 highlighting the safety risk, and a second notice will be delivered when the remedy becomes available, reported USA Today.

What to do if your vehicle is recalled
According to Consumer Reports, the recalled models are:

Ford Bronco Sport SUVs manufactured from Oct. 17, 2022, to Jan. 13, 2023.

Ford Escape SUVs manufactured from Oct. 17, 2022, to Dec. 15, 2022.

You can check the NHTSA’s website to see if your vehicle is part of this recall or others.

Owners of the affected Ford models can call Ford at 866-436-7332 to arrange for dealers to repair the vehicles free of charge, per Consumer Reports.
'''


response = chain.invoke(input_text)

print(response.text)
