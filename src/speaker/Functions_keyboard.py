import tkinter as tk
import Frame_keyboard


class Functions_keyboard:
    def __init__(self):
        frame_key = Frame_keyboard.Frame_keyboard()
    def print_value(self, value, textarea):
        self.value = str(value)
        textarea.insert(tk.END, self.value)


    def get_text(self, textarea):
        text = textarea.get("1.0", tk.END)
        return text


    def get_amout_of_characters(self, text_field):
        text = self.get_text(text_field)
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


    def control_syllable_bar(self, syllable, text_field):
        self.print_value(syllable, text_field)
        self.hide_syllable_bar()
    def syllable_bar(self, x, y):

        global bar
        bar= tk.Frame(frame_key, width=70, height=20, background="red")
        bar.place(x=x-5, y=y-5)
        global letterA
        letterA= tk.Button(bar, text="a", height=1, width=1, background="light blue", command=lambda: self.control_syllable_bar("a")).grid(row=0, column=0)
        global letterE
        letterE= tk.Button(bar, text="e", height=1, width=1, background="light blue", command=lambda: self.control_syllable_bar("e")).grid(row=0, column=1)
        global letterI
        letterI = tk.Button(bar, text="i", height=1, width=1, background="light blue", command=lambda: self.control_syllable_bar("i")).grid(row=0, column=2)
        global letterO
        letterO= tk.Button(bar, text="o", height=1, width=1, background="light blue", command=lambda: self.control_syllable_bar("o")).grid(row=0, column=3)
        global letterU
        letterU= tk.Button(bar, text="u", height=1, width=1, background="light blue", command=lambda: self.control_syllable_bar("u")).grid(row=0, column=4)

        global letterAO
        letterAO= tk.Button(bar, text="ão", height=1, width=1, background="light blue", command=lambda: self.control_syllable_bar("ão")).grid(row=0, column=5)

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

    def control_button(self, value, textarea, x, y):
        self.print_value(value, textarea)
        if value == "q":
            self.buttonQ(x, y)
        else:
            self.syllable_bar(x, y)
        self.hide_syllable_bar()
    def buttonQ(self, x, y):

        global bar
        bar= tk.Frame(root, width=70, height=20, background="red")
        bar.place(x=x-5, y=y-5)
        global letterUA
        letterUA= tk.Button(bar, text="a", height=1, width=1, background="light blue", command=lambda: self.control_syllable_bar("ua")).grid(row=0, column=0)
        global letterUE
        letterUE= tk.Button(bar, text="e", height=1, width=1, background="light blue", command=lambda: self.control_syllable_bar("ue")).grid(row=0, column=1)
        global letterUI
        letterUI = tk.Button(bar, text="i", height=1, width=1, background="light blue", command=lambda: self.control_syllable_bar("ui")).grid(row=0, column=2)
        global letterUO
        letterUO= tk.Button(bar, text="o", height=1, width=1, background="light blue", command=lambda: self.control_syllable_bar("uo")).grid(row=0, column=3)
        global letterU
        letterU= tk.Button(bar, text="u", height=1, width=1, background="light blue", command=lambda: self.control_syllable_bar("u")).grid(row=0, column=4)

        global letterUAO
        letterUAO= tk.Button(bar, text="uão", height=1, width=1, background="light blue", command=lambda: self.control_syllable_bar("uão")).grid(row=0, column=5)

    def accents_bar(self, x, y, letter):
        global bar
        bar= tk.Frame(root, width=70, height=20, background="red")
        bar.place(x=x-5, y=y-5)
        global agud
        agud= tk.Button(bar, text="´", height=1, width=1, background="light blue", command=lambda: self.set_accents("´", letter)).grid(row=0, column=0)
        global circumflex
        circumflex= tk.Button(bar, text="^", height=1, width=1, background="light blue", command=lambda: self.set_accents("^", letter)).grid(row=0, column=1)
        global tilde
        tilde= tk.Button(bar, text="~", height=1, width=1, background="light blue", command=lambda: self.set_accents("~", letter)).grid(row=0, column=2)
        global crasis
        crasis= tk.Button(bar, text="`", height=1, width=1, background="light blue", command=lambda: self.set_accents("`", letter)).grid(row=0, column=3)
        global trema
        trema= tk.Button(bar, text="¨", height=1, width=1, background="light blue", command=lambda: self.set_accents("¨", letter)).grid(row=0, column=4)
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

    def control_accents(self, letter, x, y):
       self.accents_bar(x, y, letter)


    def hide_accents(self):
        bar.destroy()
        agud.destroy()
        circumflex.destroy()
        tilde.destroy()
        crasis.destroy()
        trema.destroy()

