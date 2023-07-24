from tkinter import Tk, Button, Frame, StringVar, ttk
from Instance_controller import Instance_controller as ic
from Textboxes import Textboxes as tb
from Terminal import Terminal
class Interface:
    root = Tk()
    root.geometry("1024x600")
    root.title("Fala ai")
    root.configure(background="white")



    #  To Solve
    text_field = tb(root).text_field()
    buttonSpeake = Button(root, text="Speak", height=20, width=10, command=Terminal(text_field).speak).place(x=780, y=35)
    frame_favorite = Frame(root, width=300, height=300, background="yellow", border=2).place(x=0, y=30)
    frame_keyboard = Frame(root, width=1024, height=600, background="#07C7F2").place(x=0, y=300)

    ic(root,frame_favorite, frame_keyboard, text_field)
    voices = ["test", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9"]
    voice = StringVar()

    voice_choose = ttk.Combobox(root, textvariable=voice, values=voices)
    voice_choose.place(x=700, y=8)
    voice_choose.set("Selecione uma voz")
    voice_choose.config(width=20, height=1, background="white", foreground="black")
    root.mainloop()



    def get_voice(self):
        voice = self.voice.get()
        return voice



if __name__ == '__main__':
    Interface()
