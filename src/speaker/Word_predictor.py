import openai
from dotenv import load_dotenv
import os
from tkinter import Label
from Functions_keyboard import Functions_keyboard as fk

class Word_predictor:
    def __init__(self, root=None):
        load_dotenv()
        self.prompt = "give me the most probability words in Portuguese based on prompt:  "
        self.root = root
        self.text = ""
        self. predictions = []
        self.x = 340
        self.fk = fk

    def request(self, text):
    	
        openai.api_key = os.getenv("API_KEY")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.prompt + text,
            max_tokens=100,
            temperature=0
        )
       # print(self.prompt + text)
       # print(response)
        return response.choices[0].text

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = self.text + text


    def get_prediction(self, prediction):
        #print("see"+prediction)
        return prediction.split("\n")



    def show_prediction(self, prediction):
        for i in range(len(prediction)):
            self.predictions.append(Label(self.root, text=prediction[i], height=2, width=len(prediction[i]), background="white"))
            self.predictions[i].place(x=self.x, y=300)
            self.predictions[i].bind("<Button-1>", lambda event, text=prediction[i]: self.select_prediction(text))
          #  print(prediction[i])
            self.x += 90
        self.x = 400
        print("test")
    def select_prediction(self, text):
        self.fk.print_value(text)

    def clear_predictions(self):
        for i in range(len(self.predictions)):
            self.predictions[i].destroy()
        self.predictions = []
        self.x = 400
    def control_prediction(self, text):
        print("ok")
#        try:
 #           self.predictions.clear()
  #      finally:
   #         pass
           # self.set_text(text)
            #text = self.get_text()
            #prediction = self.request(text)
            #prediction = self.get_prediction(prediction)
            #self.show_prediction(prediction)


if __name__ == "__main__":
    wp = Word_predictor()
    sentence = input()
    print(wp.request(sentence))
