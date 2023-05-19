from tkinter import Tk, Text, Button, Frame, Canvas, OptionMenu, StringVar, ttk

from Keyboard import Keyboard as kb


class Interface:
    root = Tk()
    root.geometry("1024x600")
    root.title("Fala ai")
    root.configure(background="white")
    text_field = Text(root, height=10, width=25, border=5, font=("Arial", 18)).place(x=350, y=35)

    #  To Solve
    buttonSpeake = Button(root, text="Speak", height=20, width=10).place(x=780, y=30)
    frame_favorite = Frame(root, width=300, height=300, background="yellow", border=2).place(x=0, y=30)
    frame_keyboard = Frame(root, width=1024, height=600, background="#07C7F2").place(x=60, y=300)
    keyboard = kb(frame_keyboard, text_field)
    toolbar = Canvas(root, width=1024, height=30, background="black", border=2)
    toolbar.place(x=0, y=0)

    button_favorite = toolbar.create_oval(100, 90, 5, 67, fill="#07C7F2", tags="button_favorite")
    button_place = toolbar.move("button_favorite", 275, -62)
    text_favorite = toolbar.create_text(325, 15, text="Favoritar", fill="white", font=11, tags="text_favorite")
    #  toolbar.tag_bind("button_favorite", "<Button-1>", ffs.Functions_favorite_section(frame_favorite, r"D:\Documentos\teste.txt").add_favorite(Functions_keyboard.Functions_keyboard().get_text(text_field)))
    voices = ["test", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9"]
    voice = StringVar()
    voice.set("Selecione uma voz")
    voice_choose = ttk.Combobox(frame_favorite, textvariable=voice, values=voices)
    voice_choose.place(x=500, y=8)

    voice_choose.config(width=20, height=1, background="white")
    menu_button = Button(frame_keyboard, text="☰").place(x=1000, y=8)

    root.mainloop()

    def get_text_field(self):
        return self.text_field

    def get_voice(self):
        voice = self.voice.get()
        return voice
