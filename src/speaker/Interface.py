from tkinter import Tk, Text, Button, Frame, Canvas, StringVar, ttk, Label, Entry
from Menu import Menu as menu
from Keyboard import Keyboard as kb
from Textboxes import Textboxes as tb
from File_manager import File_manager
from Functions_favorite_section import Functions_favorite_section as ffs
from Canvas_elements import Canvas_elements as ce
class Interface:
    root = Tk()
    root.geometry("1024x600")
    root.title("Fala ai")
    root.configure(background="white")



    #  To Solve
    buttonSpeake = Button(root, text="Speak", height=20, width=10).place(x=780, y=30)
    frame_favorite = Frame(root, width=300, height=300, background="white", border=2).place(x=0, y=30)
    frame_keyboard = Frame(root, width=1024, height=600, background="#07C7F2").place(x=0, y=300)
    keyboard = kb(frame_keyboard)
    tb(root)
    ce(root)

    menu_button = Button(frame_keyboard, text="☰", command=menu(root, File_manager).show_menu).place(x=960, y=8)

    root.mainloop()



    def get_voice(self):
        voice = self.voice.get()
        return voice

    def get_pitch(self):
        pitch = self.pitch_choose.get()
        return pitch

if __name__ == '__main__':
    Interface()