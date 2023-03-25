from tkinter import *
import Terminal
import Editor
import string
import TestKeyboard
class Interface:
    kb = TestKeyboard.On_screen_keyboard()
    methods_terminal = Terminal.Terminal()
    window = Tk()
    methods_editor = Editor.Editor()
    window.geometry("500x500")
    window.title("Speak")
    window.textArea = Text(window, height=16, width=50).grid(row=0, column=0)
    kb.keyboard()

    button = window.button = Button(window, text="Speak", height=20, width=10).grid(row=0, column=10)
    window.mainloop()
if __name__ == "__main__":
    Interface()
