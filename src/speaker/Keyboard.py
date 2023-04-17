import tkinter as tk
import Terminal


# import Editor
def __init__(self):
    self.amount_of_words = 0



root = tk.Tk()
terminal = Terminal.Terminal()
root.geometry("500x500")
root.title("Keyboard")
text_field = tk.Text(root, height=10, width=30, font=("Arial", 18))
text_field.place(x=0, y=0)
buttonSpeake = tk.Button(root, text="Speak", height=20, width=10,
                         command=lambda: terminal.speake(get_text(text_field))).place(x=410, y=0)
ButtonQ = tk.Button(root, text="q", height=2, width=2, background="light blue",
                    command=lambda:control_button("q", text_field, 0,300)).place(x=0, y=300)
ButtonW = tk.Button(root, text="w", height=2, width=2, background="light blue",
                    command=lambda: control_button("w", text_field, 25,300)).place(x=25, y=300)
ButtonE = tk.Button(root, text="e", height=2, width=2, background="light blue",
                    command=lambda: control_button("e", text_field, 50, 300))
ButtonE.bind("<Button-3>", lambda event: control_accents("e", 50, 300))
ButtonE.place(x=50, y=300)
ButtonR = tk.Button(root, text="r", height=2, width=2, background="light blue",
                    command=lambda: control_button("r", text_field, 75, 300)).place(x=75, y=300)
ButtonT = tk.Button(root, text="t", height=2, width=2, background="light blue",
                    command=lambda: control_button("t", text_field, 100, 300)).place(x=100, y=300)
ButtonY = tk.Button(root, text="y", height=2, width=2, background="light blue",
                    command=lambda:control_button("y", text_field, 125, 300)).place(x=125, y=300)
ButtonU = tk.Button(root, text="u", height=2, width=2, background="light blue",
                    command=lambda: control_button("u", text_field, 150, 300)).place(x=150, y=300)
ButtonI = tk.Button(root, text="i", height=2, width=2, background="light blue",
                    command=lambda: control_button("i", text_field, 175, 300))
ButtonI.bind("<Button-3>", lambda event: control_accents("i", 175, 300))
ButtonI.place(x=175, y=300)
ButtonO = tk.Button(root, text="o", height=2, width=2, background="light blue",
                    command=lambda: control_button("o", text_field, 200, 300))
ButtonO.bind("<Button-3>", lambda event: control_accents("o", 200, 300))
ButtonO.place(x=200, y=300)
ButtonP = tk.Button(root, text="p", height=2, width=2, background="light blue",
                    command=lambda: control_button("p", text_field, 225, 300)).place(x=225, y=300)
ButtonBackspace = tk.Button(root, text="Backspace", height=2, width=10, background="light blue",
                            command=lambda: backspace(text_field)).place(x=250, y=300)
ButtonA = tk.Button(root, text="a", height=2, width=2, background="light blue",
                    command=lambda: control_button("a", text_field, 0, 345))
ButtonA.bind("<Button-3>", lambda event: control_accents("a", 0, 345))
ButtonA.place(x=0, y=345)
ButtonS = tk.Button(root, text="s", height=2, width=2, background="light blue",
                    command=lambda: control_button("s", text_field, 25, 345)).place(x=25, y=345)
ButtonD = tk.Button(root, text="d", height=2, width=2, background="light blue",
                    command=lambda: control_button("d", text_field, 50, 345)).place(x=50, y=345)
ButtonF = tk.Button(root, text="f", height=2, width=2, background="light blue",
                    command=lambda: control_button("f", text_field, 75, 345)).place(x=75, y=345)
ButtonG = tk.Button(root, text="g", height=2, width=2, background="light blue",
                    command=lambda:control_button("g", text_field, 100,345)).place(x=100, y=345)
ButtonH = tk.Button(root, text="h", height=2, width=2, background="light blue",
                    command=lambda: control_button("h", text_field, 125,345)).place(x=125, y=345)
ButtonJ = tk.Button(root, text="j", height=2, width=2, background="light blue",
                    command=lambda:control_button("j", text_field, 150,345)).place(x=150, y=345)
ButtonK = tk.Button(root, text="k", height=2, width=2, background="light blue",
                    command=lambda:control_button("k", text_field, 175,345)).place(x=175, y=345)
ButtonL = tk.Button(root, text="l", height=2, width=2, background="light blue",
                    command=lambda:control_button("l", text_field, 200,345)).place(x=200, y=345)
Buttonç = tk.Button(root, text="ç", height=2, width=2, background="light blue",
                    command=lambda:control_button("ç", text_field, 225,345)).place(x=225, y=345)
ButtonEnter = tk.Button(root, text="Enter", height=2, width=10, background="light blue",
                        command=lambda: special_char("\n")).place(x=250, y=345)
ButtonZ = tk.Button(root, text="z", height=2, width=2, background="light blue",
                    command=lambda: control_button("z", text_field, 0,390)).place(x=0, y=390)
ButtonX = tk.Button(root, text="x", height=2, width=2, background="light blue",
                    command=lambda:control_button("x", text_field, 25,390)).place(x=25, y=390)
ButtonC = tk.Button(root, text="c", height=2, width=2, background="light blue",
                    command=lambda: control_button("c", text_field, 50,390)).place(x=50, y=390)
ButtonV = tk.Button(root, text="v", height=2, width=2, background="light blue",
                    command=lambda: control_button("v", text_field, 75,390)).place(x=75, y=390)
ButtonB = tk.Button(root, text="b", height=2, width=2, background="light blue",
                    command=lambda: control_button("b", text_field, 100,390)).place(x=100, y=390)
ButtonN = tk.Button(root, text="n", height=2, width=2, background="light blue",
                    command=lambda:control_button("n", text_field, 125, 390)).place(x=125, y=390)
ButtonM = tk.Button(root, text="m", height=2, width=2, background="light blue",
                    command=lambda:control_button("m", text_field,150,390)).place(x=150, y=390)
ButtonComma = tk.Button(root, text=",", height=2, width=2, background="light blue",
                        command=lambda: print_value(",", text_field)).place(x=175, y=390)
ButtonDot = tk.Button(root, text=".", height=2, width=2, background="light blue",
                      command=lambda: print_value(".", text_field)).place(x=200, y=390)
ButtonSpace = tk.Button(root, text=" ", height=2, width=10, background="light blue",
                        command=lambda: special_char(" ")).place(x=75, y=435)
ButtonSeven = tk.Button(root, text="7", height=2, width=2, background="light blue",
                        command=lambda: print_value(7, text_field)).place(x=325, y=300)
ButtonEight = tk.Button(root, text="8", height=2, width=2, background="light blue",
                        command=lambda: print_value(8, text_field)).place(x=350, y=300)
ButtonNine = tk.Button(root, text="9", height=2, width=2, background="light blue",
                       command=lambda: print_value(9, text_field)).place(x=375, y=300)
ButtonSix = tk.Button(root, text="6", height=2, width=2, background="light blue",
                      command=lambda: print_value(6, text_field)).place(x=375, y=345)
ButtonFive = tk.Button(root, text="5", height=2, width=2, background="light blue",
                       command=lambda: print_value(5, text_field)).place(x=350, y=345)
ButtonFour = tk.Button(root, text="4", height=2, width=2, background="light blue",
                       command=lambda: print_value(4, text_field)).place(x=325, y=345)
ButtonThree = tk.Button(root, text="3", height=2, width=2, background="light blue",
                        command=lambda: print_value(3, text_field)).place(x=375, y=390)
ButtonTwo = tk.Button(root, text="2", height=2, width=2, background="light blue",
                      command=lambda: print_value(2, text_field)).place(x=350, y=390)
ButtonOne = tk.Button(root, text="1", height=2, width=2, background="light blue",
                      command=lambda: print_value(1, text_field)).place(x=325, y=390)
ButtonZero = tk.Button(root, text="0", height=2, width=2, background="light blue",
                       command=lambda: print_value(0, text_field)).place(x=350, y=435)


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
    try:
        hide_syllable_bar()
        hide_accents()
    finally:
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
    letterAO= tk.Button(bar, text="ão", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("ão")).grid(row=0, column=5)

def hide_syllable_bar():
    bar.destroy()
    try:
        letterUA.destroy()
        letterUE.destroy()
        letterUI.destroy()
        letterUO.destroy()
        letterUAO.destroy()
    except:
        letterA.destroy()
        letterE.destroy()
        letterI.destroy()
        letterO.destroy()
        letterU.destroy()
        letterAO.destroy()

def control_button(value, textarea, x, y):
    print_value(value, textarea)
    try:
        hide_syllable_bar()
    finally:
        if value == "q":
            buttonQ(x, y)
        else:
            syllable_bar(x, y)
      #  hide_syllable_bar()
def buttonQ(x, y):

    global bar
    bar= tk.Frame(root, width=70, height=20, background="red")
    bar.place(x=x-5, y=y-5)
    global letterUA
    letterUA= tk.Button(bar, text="a", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("ua")).grid(row=0, column=0)
    global letterUE
    letterUE= tk.Button(bar, text="e", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("ue")).grid(row=0, column=1)
    global letterUI
    letterUI = tk.Button(bar, text="i", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("ui")).grid(row=0, column=2)
    global letterUO
    letterUO= tk.Button(bar, text="o", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("uo")).grid(row=0, column=3)
    global letterU
    letterU= tk.Button(bar, text="u", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("u")).grid(row=0, column=4)

    global letterUAO
    letterUAO= tk.Button(bar, text="uão", height=1, width=1, background="light blue", command=lambda: control_syllable_bar("uão")).grid(row=0, column=5)

def accents_bar(x, y, letter):
    global bar
    bar= tk.Frame(root, width=70, height=20, background="red")
    bar.place(x=x-5, y=y-5)
    global agud
    agud= tk.Button(bar, text="´", height=1, width=1, background="light blue", command=lambda: set_accents("´", letter)).grid(row=0, column=0)
    global circumflex
    circumflex= tk.Button(bar, text="^", height=1, width=1, background="light blue", command=lambda: set_accents("^", letter)).grid(row=0, column=1)
    global tilde
    tilde= tk.Button(bar, text="~", height=1, width=1, background="light blue", command=lambda: set_accents("~", letter)).grid(row=0, column=2)
    global crasis
    crasis= tk.Button(bar, text="`", height=1, width=1, background="light blue", command=lambda: set_accents("`", letter)).grid(row=0, column=3)
    global trema
    trema= tk.Button(bar, text="¨", height=1, width=1, background="light blue", command=lambda: set_accents("¨", letter)).grid(row=0, column=4)
def set_accents(accent, letter):
    if letter == "a" and accent == "´":
        print_value("á", text_field)
        hide_accents()
    elif letter == "a" and accent == "¨":
        print_value("â", text_field)
        hide_accents()
    elif letter == "a" and accent == "~":
        print_value("ã", text_field)
        hide_accents()
    elif letter == "a" and accent == "`":
        print_value("à", text_field)
        hide_accents()
    elif letter == "a" and accent == "^":
        print_value("â", text_field)
        hide_accents()
    elif letter == "e" and accent == "´":
        print_value("é", text_field)
        hide_accents()
    elif letter == "e" and accent == "¨":
        print_value("ê", text_field)
        hide_accents()
    elif letter == "e" and accent == "^":
        print_value("ê", text_field)
        hide_accents()
    elif letter == "e" and accent == "~":
        print_value("ẽ", text_field)
        hide_accents()
    elif letter == "e" and accent == "`":
        print_value("è", text_field)
        hide_accents()
    elif letter == "i" and accent == "´":
        print_value("í", text_field)
        hide_accents()
    elif letter == "i" and accent == "^":
        print_value("î", text_field)
        hide_accents()
    elif letter == "i" and accent == "~":
        print_value("ĩ", text_field)
        hide_accents()
    elif letter == "i" and accent == "`":
        print_value("ì", text_field)
        hide_accents()
    elif letter == "o" and accent == "´":
        print_value("ó", text_field)
        hide_accents()
    elif letter == "o" and accent == "^":
        print_value("ô", text_field)
        hide_accents()
    elif letter == "o" and accent == "~":
        print_value("õ", text_field)
        hide_accents()
    elif letter == "o" and accent == "`":
        print_value("ò", text_field)
        hide_accents()

    elif letter == "u" and accent == "´":
        print_value("ú", text_field)
        hide_accents()
    elif letter == "u" and accent == "^":
        print_value("û", text_field)
        hide_accents()
    elif letter == "u" and accent == "~":
        print_value("ü", text_field)
        hide_accents()
    elif letter == "u" and accent == "`":
        print_value("ù", text_field)
        hide_accents()
    elif letter == "u" and accent == trema:
        print_value("ü", text_field)
        hide_accents()

def special_char(char):
    try:
        hide_syllable_bar()
        hide_accents()
    finally:
        print_value(char, text_field)

def control_accents(letter, x, y):
   accents_bar(x, y, letter)


def hide_accents():
    bar.destroy()
    agud.destroy()
    circumflex.destroy()
    tilde.destroy()
    crasis.destroy()
    trema.destroy()


root.mainloop()












