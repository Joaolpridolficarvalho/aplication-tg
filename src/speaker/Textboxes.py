from  Instance_controller import Instance_controller
from tkinter import Text, Menu
class Textboxes:
    def __init__(self, root=None):
        super().__init__()
        self.root = root
        self.field = "text_field"
    
    # TODO: let it responsive

    def text_pitch(self):
        pitch_value = Text(self.root, height=1, width=7, font=("Arial", 11)).place(x=600, y=8)
        return pitch_value

    def text_field(self):
        text_field = Text(self.root, width=30, height=10, font=("Arial", 16), border=2)
        text_field.place(x=400, y=35)
        text_field.bind("<Button-3>", self.display_popup)
        return text_field

    def show_menu(self):
        self.menu = Menu(self.root, tearoff=False)
        self.menu.add_command(label="Copy", command=self.popup_copy)
        self.menu.add_command(label="Cut", command=self.popup_cut)
        self.menu.add_separator()
        self.menu.add_command(label="Paste", command=self.popup_paste)
            


    def display_popup(self, event):
        try:
            self.menu.post(event.x_root, event.y_root)
        finally:
        	pass

    def popup_copy(self):
        self.event_generate("<<Copy>>")

    def popup_cut(self):
        self.event_generate("<<Cut>>")

    def popup_paste(self):
        self.event_generate("<<Paste>>")


# TODO: create method to alternate between fields
