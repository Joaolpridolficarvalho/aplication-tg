import openai
from dotenv import load_dotenv
import os
class Word_prediction:
    def __init__(self):
        load_dotenv()
        text = input("Enter text: ")
        print(self.request(text))

    def request(self, text):
        openai.api_key = os.getenv("API_KEY")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0.5,
            stop=["\n"]
        )
        return response.choices[1].text

Word_prediction()