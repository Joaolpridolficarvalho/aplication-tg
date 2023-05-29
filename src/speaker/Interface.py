from tkinter import Tk, Text, Button, Frame, Canvas, StringVar, ttk, Label, Entry
from Menu import Menu as menu
from Keyboard import Keyboard as kb
from Textboxes import Textboxes as tb

class Interface:
    root = Tk()
    root.geometry("1024x600")
    root.title("Fala ai")
    root.configure(background="white")

    style_font = "Arial"
    font_size = 11

    #  To Solve
    buttonSpeake = Button(root, text="Speak", height=20, width=10).place(x=780, y=30)
    frame_favorite = Frame(root, width=300, height=300, background="yellow", border=2).place(x=0, y=30)
    frame_keyboard = Frame(root, width=1024, height=600, background="#07C7F2").place(x=0, y=300)
    keyboard = kb(frame_keyboard)
    tb(root)
    toolbar = Canvas(root, width=1024, height=30, background="black", border=2)
    toolbar.place(x=0, y=0)

    button_favorite = toolbar.create_oval(100, 90, 5, 67, fill="#07C7F2", tags="button_favorite")
    button_place = toolbar.move("button_favorite", 275, -62)
    text_favorite = toolbar.create_text(325, 15, text="Favoritar", fill="white", font=[style_font, font_size], tags="text_favorite")
    #toolbar.tag_bind("button_favorite", "<Button-1>", ffs(frame_favorite, r"D:\Documentos\teste.txt").add_favorite(Functions_keyboard().get_text()))
    voices = ["test", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9"]
    voice = StringVar()
    voice.set("Selecione uma voz")
    voice_choose = ttk.Combobox(frame_favorite, textvariable=voice, values=voices)
    voice_choose.place(x=700, y=8)
    pitch = Label(frame_favorite, text="Tom", font=[style_font, font_size], background="black", foreground="white").place(x=400,
                                                                                                                y=8)
    pitch_choose = ttk.Scale(frame_favorite, from_=0, to=100, orient="horizontal").place(x=450, y=8)
    voice_choose.config(width=20, height=1, background="white")
    menu_button = Button(frame_keyboard, text="☰", command=menu(root).show_menu).place(x=960, y=8)

    root.mainloop()



    def get_voice(self):
        voice = self.voice.get()
        return voice

    def get_pitch(self):
        pitch = self.pitch_choose.get()
        return pitch
