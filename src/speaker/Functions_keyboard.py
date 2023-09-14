from tkinter import Frame, Button, END


class Functions_keyboard:
    def __init__(self, root=None, text_field=None):
        self.root = root
        self.uppercase = False
        self.text_field = text_field

    def print_value(self, value):
        value = str(value)
        if self.uppercase:
            value = value.upper()
        print(value)
        
        self.text_field.insert("end", value)

    def get_text(self):
        setence = self.text_field.get("1.0", END)
        return setence

    def backspace(self):
        self.text_field.delete("end-2c")

    def change_position_cursor(self, event=None, new_position_cursor=1):
        position_cursor = self.text_field.index("insert")
        self.text_field.icursor(position_cursor + new_position_cursor)

    def clear_text(self):
        self.text_field.delete("1.0", END)

    def control_syllable_bar(self, syllable):
        self.print_value(syllable)
        self.hide_syllable_bar()

    def syllable_bar(self, x, y):

        global bar
        bar = Frame(self.root, width=70, height=20, background="red")
        bar.place(x=x - 5, y=y - 5)
        global letterA
        letterA = Button(bar, text="a", height=1, width=1, background="light blue",
                         command=lambda: self.control_syllable_bar("a")).grid(row=0, column=0)
        global letterE
        letterE = Button(bar, text="e", height=1, width=1, background="light blue",
                         command=lambda: self.control_syllable_bar("e")).grid(row=0, column=1)
        global letterI
        letterI = Button(bar, text="i", height=1, width=1, background="light blue",
                         command=lambda: self.control_syllable_bar("i")).grid(row=0, column=2)
        global letterO
        letterO = Button(bar, text="o", height=1, width=1, background="light blue",
                         command=lambda: self.control_syllable_bar("o")).grid(row=0, column=3)
        global letterU
        letterU = Button(bar, text="u", height=1, width=1, background="light blue",
                         command=lambda: self.control_syllable_bar("u")).grid(row=0, column=4)

        global letterAO
        letterAO = Button(bar, text="ão", height=1, width=1, background="light blue",
                          command=lambda: self.control_syllable_bar("ão")).grid(row=0, column=5)

    def hide_syllable_bar(self):
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

    def control_button(self, value, x, y):
        self.print_value(value)
        try:
            self.hide_syllable_bar()
        except:
            if value == "q":
                self.buttonQ(x, y)
            else:
                self.syllable_bar(x, y)

    def buttonQ(self, x, y):

        global bar
        bar = Frame(self.root, width=70, height=20, background="red")
        bar.place(x=x - 5, y=y - 5)
        global letterUA
        letterUA = Button(bar, text="ua", height=1, width=1, background="light blue",
                          command=lambda: self.control_syllable_bar("ua")).grid(row=0, column=0)
        global letterUE
        letterUE = Button(bar, text="ue", height=1, width=1, background="light blue",
                          command=lambda: self.control_syllable_bar("ue")).grid(row=0, column=1)
        global letterUI
        letterUI = Button(bar, text="ui", height=1, width=1, background="light blue",
                          command=lambda: self.control_syllable_bar("ui")).grid(row=0, column=2)
        global letterUO
        letterUO = Button(bar, text="uo", height=1, width=1, background="light blue",
                          command=lambda: self.control_syllable_bar("uo")).grid(row=0, column=3)
        global letterU
        letterU = Button(bar, text="uu", height=1, width=1, background="light blue",
                         command=lambda: self.control_syllable_bar("u")).grid(row=0, column=4)

        global letterUAO
        letterUAO = Button(bar, text="uão", height=1, width=1, background="light blue",
                           command=lambda: self.control_syllable_bar("uão")).grid(row=0, column=5)

    def accents_bar(self, x, y, letter):
        global bar
        bar = Frame(self.root, width=70, height=20, background="red")
        bar.place(x=x - 5, y=y - 5)
        global agud
        agud = Button(bar, text="´", height=1, width=1, background="light blue",
                      command=lambda: self.set_accents("´", letter)).grid(row=0, column=0)
        global circumflex
        circumflex = Button(bar, text="^", height=1, width=1, background="light blue",
                            command=lambda: self.set_accents("^", letter)).grid(row=0, column=1)
        global tilde
        tilde = Button(bar, text="~", height=1, width=1, background="light blue",
                       command=lambda: self.set_accents("~", letter)).grid(row=0, column=2)
        global crasis
        crasis = Button(bar, text="`", height=1, width=1, background="light blue",
                        command=lambda: self.set_accents("`", letter)).grid(row=0, column=3)
        global trema
        trema = Button(bar, text="¨", height=1, width=1, background="light blue",
                       command=lambda: self.set_accents("¨", letter)).grid(row=0, column=4)

    def set_accents(self, accent, letter):
        if letter == "a" and accent == "´":
            self.print_value("á")
        elif letter == "a" and accent == "¨":
            self.print_value("â")
            self.hide_accents()
        elif letter == "a" and accent == "~":
            self.print_value("ã")
            self.hide_accents()
        elif letter == "a" and accent == "`":
            self.print_value("à")
            self.hide_accents()
        elif letter == "e" and accent == "´":
            self.print_value("é")
            self.hide_accents()
        elif letter == "e" and accent == "¨":
            self.print_value("ê")
            self.hide_accents()
        elif letter == "e" and accent == "~":
            self.print_value("ẽ")
            self.hide_accents()
        elif letter == "e" and accent == "`":
            self.print_value("è")
            self.hide_accents()
        elif letter == "i" and accent == "´":
            self.print_value("í")
            self.hide_accents()
        elif letter == "i" and accent == "^":
            self.print_value("î")
            self.hide_accents()
        elif letter == "i" and accent == "~":
            self.print_value("ĩ")
            self.hide_accents()
        elif letter == "i" and accent == "`":
            self.print_value("ì")
            self.hide_accents()
        elif letter == "o" and accent == "´":
            self.print_value("ó")
            self.hide_accents()
        elif letter == "o" and accent == "^":
            self.print_value("ô")
            self.hide_accents()
        elif letter == "o" and accent == "~":
            self.print_value("õ")
            self.hide_accents()
        elif letter == "o" and accent == "`":
            self.print_value("ò")
            self.hide_accents()
        elif letter == "u" and accent == "´":
            self.print_value("ú")
            self.hide_accents()
        elif letter == "u" and accent == "^":
            self.print_value("û")
            self.hide_accents()
        elif letter == "u" and accent == "~":
            self.print_value("ü")
            self.hide_accents()
        elif letter == "u" and accent == "`":
            self.print_value("ù")
            self.hide_accents()
        elif letter == "u" and accent == trema:
            self.print_value("ü")
            self.hide_accents()

    def control_accents(self, letter, x, y):
        try:
            self.hide_syllable_bar()
        finally:
            self.accents_bar(x, y, letter)

    def hide_accents(self):
        bar.destroy()
        agud.destroy()
        circumflex.destroy()
        tilde.destroy()
        crasis.destroy()
        trema.destroy()

    def set_uppercase(self):
        if self.uppercase:
            self.uppercase = False
        else:
            self.uppercase = True
