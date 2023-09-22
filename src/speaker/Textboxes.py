from tkinter import Text, Menu
from Functions_keyboard import Functions_keyboard as fk

class Textboxes:
    def __init__(self, root=None):
        self.root = root
        self.text = ""

    def text_pitch(self):
        pitch_value = Text(self.root, height=1, width=7, font=("Arial", 11))
        pitch_value.place(x=600, y=8)
        return pitch_value

    def text_field(self):
        text_field = Text(self.root, width=30, height=10, font=("Arial", 16), bd=2)
        text_field.place(x=400, y=35)
      
        return text_field
