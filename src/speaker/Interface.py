from tkinter import Tk, Button, Frame, StringVar, ttk
from Instance_controller import Instance_controller as ic
from Textboxes import Textboxes as tb
from Terminal import Terminal
class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1024x600")
        self.root.title("Fala ai")
        self.root.configure(background="white")

        self.text_field = tb(self.root).text_field()
        self.buttonSpeake = Button(self.root, text="Speak", height=15, width=10, command=Terminal(self.text_field).control).place(x=780, y=35)
        self.frame_favorite = Frame(self.root, width=350, height=270, background="yellow", border=2)
        self.frame_favorite.place(x=0, y=35)
        
        self.frame_keyboard = Frame(self.root, width=1024, height=550, background="#07C7F2")
        self.frame_keyboard.place(x=0, y=300)
        
        ic(self.root, self.frame_favorite, self.frame_keyboard, self.text_field)

        self.voices = ["test", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9"]
        self.voice = StringVar()

        self.voice_choose = ttk.Combobox(self.root, textvariable=self.voice, values=self.voices)
        self.voice_choose.place(x=700, y=8)
        self.voice_choose.set("Selecione uma voz")
        self.voice_choose.config(width=20, height=1, background="white", foreground="black")
        
        self.root.mainloop()

    def get_voice(self):
        voice = self.voice.get()
        return voice

if __name__ == '__main__':
    Interface()

