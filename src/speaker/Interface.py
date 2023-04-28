from tkinter import *
import tkinter as tk
import Terminal
import Keyboard
#import Editor
import string

class Interface:
    root = tk.Tk()
    terminal = Terminal.Terminal()
    root.geometry("1024x600")
    root.title("Fala ai")
   # root.configure(background='#07C7F2')

    text_field = tk.Text(root, height=10, width=20, font=("Arial", 18))
    text_field.place(x=0, y=0)
    buttonSpeake = tk.Button(root, text="Speak", height=20, width=10,
                             command=lambda:Terminal.speake(Keyboard.get_text())).place(x=410, y=0)
    frame_keyboard = tk.Frame(root, width=600, height=600, background="#07C7F2").place(x=0, y=300)

    keyboard = Keyboard.Keyboard(frame_keyboard)


    root.mainloop()