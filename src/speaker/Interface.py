from tkinter import *
import Terminal
import Editor
import string
class Interface:
    methods_terminal = Terminal.Terminal()
    window = Tk()
    methods_editor = Editor.Editor()
    window.geometry("500x500")
    window.title("Speak")
    window.textArea = Text(window, height=16, width=50).grid(row=0, column=0)


    def get_text(self):
        Terminal.Terminal.speake(self.text)

    button = window.button = Button(window, text="Speak", command=get_text, height=20, width=10).grid(row=0, column=10)
    window.mainloop()
if __name__ == "__main__":
    Interface()
