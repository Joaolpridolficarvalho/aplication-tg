
from tkinter import Tk, Text
class Textboxes:
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.text_field = Text(master, width=50, height=10).place(x=0, y=0)