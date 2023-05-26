from tkinter import Button, Frame
class Menu:
    def __init__(self, root):
        self.root = root


    def open(self):
        #self.frame_menu = Frame(self.root, width=1200, height=50, background="white").place(x=1000, y=10)
        open_file = Button(self.root, text="Abrir", width=10, height=2, font=("Arial", 12), border=2, background="black").place(x=1000, y=11)
