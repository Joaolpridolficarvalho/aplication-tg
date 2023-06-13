
from tkinter import Text
class Textboxes:
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.field = "text_field"
    # TODO: let it responsive

    def text_pitch(self):
        pitch_value = Text(self.root, height=1, width=7, font=("Arial", 11)).place(x=600, y=8)
        return pitch_value




# TODO: create method to alternate between fields
