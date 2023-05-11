from tkinter import *
import tkinter as tk

from Keyboard import Keyboard
import Terminal

import Functions_keyboard
import Functions_favorite_section as ffs

class Interface:
    root = tk.Tk()
    root.geometry("1024x600")
    root.title("Fala ai")
    root.configure(background="white")
    text_field = tk.Text(root, height=10, width=20, border=5, font=("Arial", 18)).place(x=350, y=35)
  #  To Solve
    buttonSpeake = tk.Button(root, text="Speak", height=20, width=10).place(x=780, y=30)
    frame_favorite = tk.Frame(root, width=300, height=300, background="yellow", border=2).place(x=0, y=30)
    frame_keyboard = tk.Frame(root, width=1024, height=600, background="#07C7F2").place(x=0, y=300)
    keyboard = Keyboard(frame_keyboard, text_field)
    toolbar = Canvas(root, width=1024, height=30, background="black", border=2)
    toolbar.place(x=0, y=0)

    button_favorite = toolbar.create_oval(100, 90, 5, 70, fill="#07C7F2", tags="button_favorite")
    button_place = toolbar.move("button_favorite", 275, -65)
    text_favorite = toolbar.create_text(320, 15, text="Favoritar", fill="white", font=11, tags="text_favorite")
  #  toolbar.tag_bind("button_favorite", "<Button-1>", ffs.Functions_favorite_section(frame_favorite, r"D:\Documentos\teste.txt").add_favorite(Functions_keyboard.Functions_keyboard().get_text(text_field)))

    root.mainloop()
