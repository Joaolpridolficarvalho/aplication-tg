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
    root.title("Keyboard")
    text_field = tk.Text(root, height=10, width=20, font=("Arial", 18))
    text_field.place(x=0, y=0)
    keyboard = Keyboard.Keyboard(root)
    #Keyboard.place( 0, 300)

    root.mainloop()