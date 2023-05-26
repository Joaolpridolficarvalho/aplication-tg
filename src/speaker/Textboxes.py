
from tkinter import Text
class Textboxes:
    def __init__(self, root=None):
        super().__init__()
        self.root = root

    def text_field(self):
        text_field = Text(self.root, width=30, height=10, font=("Arial", 16), border=2)
        text_field.place(x=400, y=30)
        return text_field

    def text_pitch(self):
        pitch_value = Text(self.root, height=1, width=7, font=("Arial", 11)).place(x=600, y=8)
        return pitch_value




# TODO: create method to alternate between fields