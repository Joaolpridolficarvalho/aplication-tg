from tkinter import Tk, Button, Frame, Canvas
from Instance_controller import Instance_controller as ic
from Textboxes import Textboxes as tb
from Sintesizether import Sintesizether
class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1024x600")
        self.root.title("Fala ai")
        self.root.configure(background="white")

        self.text_field = tb(self.root).text_field()
        
        self.frame_favorite = Frame(self.root, width=500, height=270, background="yellow", border=2)
        self.frame_favorite.place(x=0, y=35)
        self.toolbar = Canvas(self.root, width=1024, height=30, background="black", border=2)
        self.toolbar.place(x=0, y=0)
        self.sintesizether = Sintesizether(self.text_field, self.toolbar)
        self.buttonSpeake = Button(self.root, text="Speak", height=15, width=10, command=self.sintesizether.speak).place(x=780, y=35)
        self.frame_keyboard = Frame(self.root, width=1024, height=550, background="#07C7F2")
        self.frame_keyboard.place(x=0, y=300)
        
        ic(self.root, self.frame_favorite, self.frame_keyboard, self.text_field, self.toolbar)

        
        self.root.mainloop()

  
if __name__ == '__main__':
    Interface()

