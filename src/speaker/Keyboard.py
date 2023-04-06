import tkinter as tk
import Terminal


# import Editor
def __init__(self):
    self.amount_of_words = 0



root = tk.Tk()
terminal = Terminal.Terminal()
root.geometry("1024x600")
root.title("Keyboard")
text_field = tk.Text(root, height=16, width=50)
text_field.place(x=0, y=0)
buttonSpeake = tk.Button(root, text="Speak", height=20, width=10,
                         command=lambda: terminal.speake(get_text(text_field))).place(x=410, y=0)
sugestion1 = tk.Text(root, height=5, width=10).place(x=0, y=260)
sugestion2 = tk.Text(root, height=5, width=10).place(x=100, y=260)
sugestion3 = tk.Text(root, height=5, width=10).place(x=200, y=260)
sugestion4 = tk.Text(root, height=5, width=10).place(x=300, y=260)
sugestion5 = tk.Text(root, height=5, width=10).place(x=400, y=260)
sugestion6 = tk.Text(root, height=5, width=10).place(x=500, y=260)
sugestion7 = tk.Text(root, height=5, width=10).place(x=600, y=260)
sugestion8 = tk.Text(root, height=5, width=10).place(x=700, y=260)
sugestion9 = tk.Text(root, height=5, width=10).place(x=800, y=260)
ButtonQ = tk.Button(root, text="q", height=2, width=2, background="light blue",
                    command=lambda:control_button("q", text_field, 0,300)].place(x=0, y=300)
ButtonW = tk.Button(root, text="w", height=2, width=2, background="light blue",
                    command=lambda: print_value("w", text_field)).place(x=25, y=300)
ButtonE = tk.Button(root, text="e", height=2, width=2, background="light blue",
                    command=lambda: print_value("e", text_field)).place(x=50, y=300)
ButtonR = tk.Button(root, text="r", height=2, width=2, background="light blue",
                    command=lambda: print_value("r", text_field)).place(x=75, y=300)
ButtonT = tk.Button(root, text="t", height=2, width=2, background="light blue",
                    command=lambda: print_value("t", text_field)).place(x=100, y=300)
ButtonY = tk.Button(root, text="y", height=2, width=2, background="light blue",
                    command=lambda: print_value("y", text_field)).place(x=125, y=300)
ButtonU = tk.Button(root, text="u", height=2, width=2, background="light blue",
                    command=lambda: print_value("u", text_field)).place(x=150, y=300)
ButtonI = tk.Button(root, text="i", height=2, width=2, background="light blue",
                    command=lambda: print_value("i", text_field)).place(x=175, y=300)
ButtonO = tk.Button(root, text="o", height=2, width=2, background="light blue",
                    command=lambda: print_value("o", text_field)).place(x=200, y=300)
ButtonP = tk.Button(root, text="p", height=2, width=2, background="light blue",
                    command=lambda: print_value("p", text_field)).place(x=225, y=300)
ButtonBackspace = tk.Button(root, text="Backspace", height=2, width=10, background="light blue",
                            command=lambda: backspace(text_field)).place(x=250, y=300)
ButtonA = tk.Button(root, text="a", height=2, width=2, background="light blue",
                    command=lambda: print_value("a", text_field)).place(x=0, y=345)
ButtonS = tk.Button(root, text="s", height=2, width=2, background="light blue",
                    command=lambda: print_value("s", text_field)).place(x=25, y=345)
ButtonD = tk.Button(root, text="d", height=2, width=2, background="light blue",
                    command=lambda: print_value("d", text_field)).place(x=50, y=345)
ButtonF = tk.Button(root, text="f", height=2, width=2, background="light blue",
                    command=lambda: print_value("f", text_field)).place(x=75, y=345)
ButtonG = tk.Button(root, text="g", height=2, width=2, background="light blue",
                    command=lambda:control_button("g", text_field, 100,345)).place(x=100, y=345)
ButtonH = tk.Button(root, text="h", height=2, width=2, background="light blue",
                    command=lambda:[ print_value("h", text_field),syllable_bar(125,345)]).place(x=125, y=345)
ButtonJ = tk.Button(root, text="j", height=2, width=2, background="light blue",
                    command=lambda:control_button("j", text_field, 150,345)).place(x=150, y=345)
ButtonK = tk.Button(root, text="k", height=2, width=2, background="light blue",
                    command=lambda:control_button("k", text_field, 175,345)).place(x=175, y=345)
ButtonL = tk.Button(root, text="l", height=2, width=2, background="light blue",
                    command=lambda:control_button("l", text_field, 200,345)).place(x=200, y=345)
Buttonç = tk.Button(root, text="ç", height=2, width=2, background="light blue",
                    command=lambda:control_button("ç", text_field, 225,345)).place(x=225, y=345)
ButtonEnter = tk.Button(root, text="Enter", height=2, width=10, background="light blue",
                        command=lambda: print_value("\n", text_field)).place(x=250, y=345)
ButtonZ = tk.Button(root, text="z", height=2, width=2, background="light blue",
                    command=lambda:[ print_value("z", text_field) , syllable_bar(0,390)]).place(x=0, y=390)
ButtonX = tk.Button(root, text="x", height=2, width=2, background="light blue",
                    command=lambda:control_button("x", text_field, 25,390)).place(x=25, y=390)
ButtonC = tk.Button(root, text="c", height=2, width=2, background="light blue",
                    command=lambda: control_button("c", text_field, 50,390)).place(x=50, y=390)
ButtonV = tk.Button(root, text="v", height=2, width=2, background="light blue",
                    command=lambda: control_button("v", text_field, 75,390)).place(x=75, y=390)
ButtonB = tk.Button(root, text="b", height=2, width=2, background="light blue",
                    command=lambda: control_button("b", text_field, 100,390]).place(x=100, y=390)
ButtonN = tk.Button(root, text="n", height=2, width=2, background="light blue",
                    command=lambda:control_button("n", text_field, 125, 390)).place(x=125, y=390)
ButtonM = tk.Button(root, text="m", height=2, width=2, background="light blue",
                    command=lambda:control_button("m", text_field,150,390)).place(x=150, y=390)
ButtonComma = tk.Button(root, text=",", height=2, width=2, background="light blue",
                        command=lambda: print_value(",", text_field)).place(x=175, y=390)
ButtonDot = tk.Button(root, text=".", height=2, width=2, background="light blue",
                      command=lambda: print_value(".", text_field)).place(x=200, y=390)
ButtonSpace = tk.Button(root, text=" ", height=2, width=10, background="light blue",
                        command=lambda: print_value(" ", text_field)).place(x=75, y=435)
ButtonSeven = tk.Button(root, text="7", height=2, width=2, background="light blue",
                        command=lambda: print_value(7, text_field)).place(x=300, y=300)
ButtonEight = tk.Button(root, text="8", height=2, width=2, background="light blue",
                        command=lambda: print_value(8, text_field)).place(x=325, y=300)
ButtonNine = tk.Button(root, text="9", height=2, width=2, background="light blue",
                       command=lambda: print_value(9, text_field)).place(x=350, y=300)
ButtonSix = tk.Button(root, text="6", height=2, width=2, background="light blue",
                      command=lambda: print_value(6, text_field)).place(x=350, y=345)
ButtonFive = tk.Button(root, text="5", height=2, width=2, background="light blue",
                       command=lambda: print_value(5, text_field)).place(x=325, y=345)
ButtonFour = tk.Button(root, text="4", height=2, width=2, background="light blue",
                       command=lambda: print_value(4, text_field)).place(x=300, y=345)
ButtonThree = tk.Button(root, text="3", height=2, width=2, background="light blue",
                        command=lambda: print_value(3, text_field)).place(x=350, y=390)
ButtonTwo = tk.Button(root, text="2", height=2, width=2, background="light blue",
                      command=lambda: print_value(2, text_field)).place(x=325, y=390)
ButtonOne = tk.Button(root, text="1", height=2, width=2, background="light blue",
                      command=lambda: print_value(1, text_field)).place(x=300, y=390)
ButtonZero = tk.Button(root, text="0", height=2, width=2, background="light blue",
                       command=lambda: print_value(0, text_field)).place(x=325, y=435)


def print_value(value, textarea):
    value = str(value)
    textarea.insert(tk.END, value)


def get_text(textarea):
    text = textarea.get("1.0", tk.END)
    return text


def get_amout_of_characters(self):
    text = get_text(text_field)
    return len(text)


# def get_sugestion(self):
#     sugestion = Editor.predict(get_text(text_field))
#     return sugestion
# def show_sugestion(self, textarea):
#     sugestion = get_sugestion()
#     textarea.insert(tk.END, sugestion)

def backspace(textarea):
    textarea.delete("end-2c")


def clear_text(textarea):
    textarea.delete("1.0", tk.END)


def control_syllable_bar(syllable):
    print_value(syllable, text_field)
    hide_syllable_bar()
def syllable_bar(x, y):

    global bar
    bar= tk.Frame(root, width=70, height=20, background="red")
    bar.place(x=x-5, y=y-5)
    global letterA
    letterA= tk.Button(bar, text="a", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("a")).grid(row=0, column=0)
    global letterE
    letterE= tk.Button(bar, text="e", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("e")).grid(row=0, column=1)
    global letterI
    letterI = tk.Button(bar, text="i", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("i")).grid(row=0, column=2)
    global letterO
    letterO= tk.Button(bar, text="o", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("o")).grid(row=0, column=3)
    global letterU
    letterU= tk.Button(bar, text="u", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("u")).grid(row=0, column=4)

    global letterAO
    letterAO= tk.Button(bar, text="ão", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("ão", )).grid(row=0, column=5)

def hide_syllable_bar():
    bar.destroy()
    letterA.destroy()
    letterE.destroy()
    letterI.destroy()
    letterO.destroy()
    letterU.destroy()
    letterAO.destroy()

def control_button(value, textarea, x, y):
    try:
        hide_syllable_bar()
    finally:
        print_value(value, textarea)
        syllable_bar(x, y)


root.mainloop()













