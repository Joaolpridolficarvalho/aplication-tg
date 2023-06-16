from tkinter import Frame, Button, END, Text


class Functions_keyboard:
    def __init__(self, root=None):
        self.root = root
        self.uppercase = False

    def print_value(self, value, text_field):
        value = str(value)
        if self.uppercase:
            value = value.upper()
        text_field.insert("end", value)

    def get_text(self, text_field):
        setence = text_field.get("1.0", END)
        return setence

    def backspace(self, text_field):
        text_field.delete("end-2c")

    def change_position_cursor(self, text_field, event=None, new_position_cursor=1):
        position_cursor = text_field.index("insert")
        text_field.icursor(position_cursor + new_position_cursor)

    def clear_text(self, text_field):
        text_field.delete("1.0", END)

    def control_syllable_bar(self, syllable, text_field):
        self.print_value(syllable, text_field)
        self.hide_syllable_bar()

    def syllable_bar(self, x, y, text_field):

        global bar
        bar = Frame(self.root, width=70, height=20, background="red")
        bar.place(x=x - 5, y=y - 5)
        global letterA
        letterA = Button(bar, text="a", height=1, width=1, background="light blue",
                         command=lambda: self.control_syllable_bar("a", text_field)).grid(row=0, column=0)
        global letterE
        letterE = Button(bar, text="e", height=1, width=1, background="light blue",
                         command=lambda: self.control_syllable_bar("e", text_field)).grid(row=0, column=1)
        global letterI
        letterI = Button(bar, text="i", height=1, width=1, background="light blue",
                         command=lambda: self.control_syllable_bar("i", text_field)).grid(row=0, column=2)
        global letterO
        letterO = Button(bar, text="o", height=1, width=1, background="light blue",
                         command=lambda: self.control_syllable_bar("o", text_field)).grid(row=0, column=3)
        global letterU
        letterU = Button(bar, text="u", height=1, width=1, background="light blue",
                         command=lambda: self.control_syllable_bar("u", text_field)).grid(row=0, column=4)

        global letterAO
        letterAO = Button(bar, text="ão", height=1, width=1, background="light blue",
                          command=lambda: self.control_syllable_bar("ão", text_field)).grid(row=0, column=5)

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

    def control_button(self, value, x, y, text_field):
        self.print_value(value, text_field)
        try:
            self.hide_syllable_bar()
        except:
            if value == "q":
                self.buttonQ(x, y, text_field)
            else:
                self.syllable_bar(x, y, text_field)

    def buttonQ(self, x, y, text_field):

        global bar
        bar = Frame(self.root, width=70, height=20, background="red")
        bar.place(x=x - 5, y=y - 5)
        global letterUA
        letterUA = Button(bar, text="ua", height=1, width=1, background="light blue",
                          command=lambda: self.control_syllable_bar("ua", text_field)).grid(row=0, column=0)
        global letterUE
        letterUE = Button(bar, text="ue", height=1, width=1, background="light blue",
                          command=lambda: self.control_syllable_bar("ue", text_field)).grid(row=0, column=1)
        global letterUI
        letterUI = Button(bar, text="ui", height=1, width=1, background="light blue",
                          command=lambda: self.control_syllable_bar("ui", text_field)).grid(row=0, column=2)
        global letterUO
        letterUO = Button(bar, text="uo", height=1, width=1, background="light blue",
                          command=lambda: self.control_syllable_bar("uo", text_field)).grid(row=0, column=3)
        global letterU
        letterU = Button(bar, text="uu", height=1, width=1, background="light blue",
                         command=lambda: self.control_syllable_bar("u", text_field)).grid(row=0, column=4)

        global letterUAO
        letterUAO = Button(bar, text="uão", height=1, width=1, background="light blue",
                           command=lambda: self.control_syllable_bar("uão", text_field)).grid(row=0, column=5)

    def accents_bar(self, x, y, letter, text_field):
        global bar
        bar = Frame(self.root, width=70, height=20, background="red")
        bar.place(x=x - 5, y=y - 5)
        global agud
        agud = Button(bar, text="´", height=1, width=1, background="light blue",
                      command=lambda: self.set_accents("´", letter, text_field)).grid(row=0, column=0)
        global circumflex
        circumflex = Button(bar, text="^", height=1, width=1, background="light blue",
                            command=lambda: self.set_accents("^", letter, text_field)).grid(row=0, column=1)
        global tilde
        tilde = Button(bar, text="~", height=1, width=1, background="light blue",
                       command=lambda: self.set_accents("~", letter, text_field)).grid(row=0, column=2)
        global crasis
        crasis = Button(bar, text="`", height=1, width=1, background="light blue",
                        command=lambda: self.set_accents("`", letter, text_field)).grid(row=0, column=3)
        global trema
        trema = Button(bar, text="¨", height=1, width=1, background="light blue",
                       command=lambda: self.set_accents("¨", letter, text_field)).grid(row=0, column=4)

    def set_accents(self, accent, letter, text_field):
        if letter == "a" and accent == "´":
            self.print_value("á", text_field)
        elif letter == "a" and accent == "¨":
            self.print_value("â", text_field)
            self.hide_accents()
        elif letter == "a" and accent == "~":
            self.print_value("ã", text_field)
            self.hide_accents()
        elif letter == "a" and accent == "`":
            self.print_value("à", text_field)
            self.hide_accents()
        elif letter == "e" and accent == "´":
            self.print_value("é", text_field)
            self.hide_accents()
        elif letter == "e" and accent == "¨":
            self.print_value("ê", text_field)
            self.hide_accents()
        elif letter == "e" and accent == "~":
            self.print_value("ẽ", text_field)
            self.hide_accents()
        elif letter == "e" and accent == "`":
            self.print_value("è", text_field)
            self.hide_accents()
        elif letter == "i" and accent == "´":
            self.print_value("í", text_field)
            self.hide_accents()
        elif letter == "i" and accent == "^":
            self.print_value("î", text_field)
            self.hide_accents()
        elif letter == "i" and accent == "~":
            self.print_value("ĩ", text_field)
            self.hide_accents()
        elif letter == "i" and accent == "`":
            self.print_value("ì", text_field)
            self.hide_accents()
        elif letter == "o" and accent == "´":
            self.print_value("ó", text_field)
            self.hide_accents()
        elif letter == "o" and accent == "^":
            self.print_value("ô", text_field)
            self.hide_accents()
        elif letter == "o" and accent == "~":
            self.print_value("õ", text_field)
            self.hide_accents()
        elif letter == "o" and accent == "`":
            self.print_value("ò", text_field)
            self.hide_accents()
        elif letter == "u" and accent == "´":
            self.print_value("ú", text_field)
            self.hide_accents()
        elif letter == "u" and accent == "^":
            self.print_value("û", text_field)
            self.hide_accents()
        elif letter == "u" and accent == "~":
            self.print_value("ü", text_field)
            self.hide_accents()
        elif letter == "u" and accent == "`":
            self.print_value("ù", text_field)
            self.hide_accents()
        elif letter == "u" and accent == trema:
            self.print_value("ü", text_field)
            self.hide_accents()

    def control_accents(self, letter, x, y, text_field):
        try:
            self.hide_syllable_bar()
        finally:
            self.accents_bar(x, y, letter, text_field)

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
