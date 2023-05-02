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
    root.configure(background='white')

    text_field = tk.Text(root, height=10, width=35, font=("Arial", 18), border=2, background="white", relief="solid")
    text_field.place(x=285, y=30)
    buttonSpeake = tk.Button(root, text="Speak", height=20, width=10,
                             command=lambda:Terminal.speake(Keyboard.get_text())).place(x=780, y=30)
    frame_toolbar = tk.Frame(root, width=1024, height=30, background="black").place(x=0, y=0)
    frame_favorite = tk.Frame(root, width=275, height=30, background="white", border=2).place(x=0, y=30)
    frame_keyboard = tk.Frame(root, width=1024, height=600, background="#07C7F2").place(x=0, y=300)
    keyboard = Keyboard.Keyboard(frame_keyboard, text_field)


    root.mainloop()