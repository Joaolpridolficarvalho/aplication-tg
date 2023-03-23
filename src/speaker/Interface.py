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
    button = window.button = Button(window, text="Speak", command=methods_terminal.speake, height=20, width=10).grid(row=0, column=10)
    def keyboad(self):
        for char in string.ascii_letters:
            button_char = window.button = Button(window, text=char, command=methods_editor.write_char , height=2, width=5).grid(row=9, column=10)

    window.mainloop()
if __name__ == "__main__":
    Interface()
