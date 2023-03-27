from tkinter import *
import Terminal
import Editor
import string

class Interface:
    def __init__(self):
        mensage = ""
    methods_terminal = Terminal.Terminal()
    window = Tk()
    methods_editor = Editor.Editor()
    window.geometry("500x500")
    text_field = Entry(window)

    #inteface = Interface()
    def print_value(value, textarea):
        textarea.insert(tk.END, value + "\n")

    window.title("Speak")
    letter="a"

    text_field = Text(window, height=16, width=50)
    Text.pack(text_field)
    text_field.place(x=0, y=0)

    buttonSpeake = window.button = Button(window, text="Speak", height=20, width=10).place(x=410, y=0)
    ButtonQ = Button(window, text="q", relief=FLAT, height=2, width=2, background="light blue",  command= lambda: print_value("q", text_field)).place(x=0, y=300)
    ButtonW = Button(window, text="w", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("w", text_field)).place(x=25, y=300)
    ButtonE = Button(window, text="e", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("e", text_field)).place(x=50, y=300)
    ButtonR = Button(window, text="r", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("r", text_field)).place(x=75, y=300)
    ButtonT = Button(window, text="t", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("t", text_field)).place(x=100, y=300)
    ButtonY = Button(window, text="y", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("y", text_field)).place(x=125, y=300)
    ButtonU = Button(window, text="u", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("u", text_field)).place(x=150, y=300)
    ButtonI = Button(window, text="i", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("i", text_field)).place(x=175, y=300)
    ButtonO = Button(window, text="o", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("o", text_field)).place(x=200, y=300)
    ButtonP = Button(window, text="p", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("p", text_field)).place(x=225, y=300)
    ButtonA = Button(window, text="a", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("a", text_field)).place(x=0, y=345)
    ButtonS = Button(window, text="s", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("s", text_field)).place(x=25, y=345)
    ButtonD = Button(window, text="d", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("d", text_field)).place(x=50, y=345)
    ButtonF = Button(window, text="f", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("f", text_field)).place(x=75, y=345)
    ButtonG = Button(window, text="g", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("g", text_field)).place(x=100, y=345)
    ButtonH = Button(window, text="h", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("h", text_field)).place(x=125, y=345)
    ButtonJ = Button(window, text="j", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("j", text_field)).place(x=150, y=345)
    ButtonK = Button(window, text="k", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("k", text_field)).place(x=175, y=345)
    ButtonL = Button(window, text="l", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("l", text_field)).place(x=200, y=345)
    Buttonç = Button(window, text="ç", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("ç", text_field)).place(x=225, y=345)
    ButtonZ = Button(window, text="z", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("z", text_field)).place(x=0, y=390)
    ButtonX = Button(window, text="x", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("x", text_field)).place(x=25, y=390)
    ButtonC = Button(window, text="c", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("c", text_field)).place(x=50, y=390)
    ButtonV = Button(window, text="v", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("v", text_field)).place(x=75, y=390)
    ButtonB = Button(window, text="b", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("b", text_field)).place(x=100, y=390)
    ButtonN = Button(window, text="n", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("n", text_field)).place(x=125, y=390)
    ButtonM = Button(window, text="m", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value("m", text_field)).place(x=150, y=390)
    ButtonSpace = Button(window, text=" ", relief=FLAT, height=2, width=10, background="light blue", command=  lambda: print_value("", text_field)).place(x=75, y=435)
    ButtonSeven = Button(window, text="7", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value(7, text_field)).place(x=300, y=345)
    ButtonEight = Button(window, text="8", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value(8, text_field)).place(x=325, y=345)
    ButtonNine = Button(window, text="9", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value(9, text_field)).place(x=350, y=345)
    ButtonSix = Button(window, text="6", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value(6, text_field)).place(x=350, y=390)
    ButtonFive = Button(window, text="5", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value(5, text_field)).place(x=325, y=390)
    ButtonFour = Button(window, text="4", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value(4, text_field)).place(x=300, y=390)
    ButtonThree = Button(window, text="3", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value(3, text_field)).place(x=350, y=435)
    ButtonTwo = Button(window, text="2", relief=FLAT, height=2, width=2, background="light blue", command=  lambda: print_value(2, text_field)).place(x=325, y=435)
    ButtonOne = Button(window, text="1", relief=FLAT, height=2, width=2, background="light blue", command= lambda: print_value(1, text_field)).place(x=300, y=435)

    window.mainloop()
if __name__ == "__main__":
    Interface()
