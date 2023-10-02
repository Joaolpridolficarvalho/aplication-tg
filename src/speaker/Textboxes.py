from tkinter.scrolledtext import ScrolledText

class Textboxes:
    def __init__(self, root=None):
        self.root = root

    def text_field(self):
        text_field = ScrolledText(self.root, width=30, height=10, font=("Arial", 16), bd=2)
        text_field.place(x=400, y=35)
      
        return text_field
