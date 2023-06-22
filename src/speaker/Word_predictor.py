import openai
from dotenv import load_dotenv
import os
from tkinter import Label
class Word_prediction:
    def __init__(self, text_field, root=None):
        load_dotenv()
        self.text_field = text_field
        self.prompt = "Quais são todas as próximas palavras mais provaveis dado o seguinte prompt? "
        self.root = root
        self. predictions = []

    def request(self, text):
        openai.api_key = os.getenv("API_KEY")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.prompt + text,
            max_tokens=100,
            temperature=0
        )
        return response.choices[0].text

    def get_text(self):
        pass


    def get_prediction(self, prediction):
        return prediction.split("\n")

    def show_prediction(self, prediction):
        for i in range(len(prediction)):
            self.predictions.append(Label(self.root, text=prediction[i]))
            self.predictions[i].place(x=0, y=0)
            self.predictions[i].bind("<Button-1>", lambda event, text=prediction[i]: self.select_prediction(text))

    def select_prediction(self, text):
        pass

    def control_prediction(self):
        text = self.get_text()
        prediction = self.request(text)
        prediction = self.get_prediction(prediction)
        self.show_prediction(prediction)