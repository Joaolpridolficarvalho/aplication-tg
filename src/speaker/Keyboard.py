import tkinter as tk

from Word_predictor import Word_predictor as wp

from Functions_keyboard import Functions_keyboard as fk

from Symbol_keyboard import Symbol_keyboard as sk


class Keyboard:
    def __init__(self, frame_keyboard, text_field):
        self.text_field = text_field
        self.is_activated_sk = False
        position_first_line = [320, 30]
        position_first_line_numeric = [820, 30]
        distance_between_lines = 40
        self.frame_keyboard = frame_keyboard
        self.distance_between_buttons = 40
        self.sk = sk(frame_keyboard, self.text_field)
        first_line = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        second_line = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ç"]
        third_line = ["z", "x", "c", "v", "b", "n", "m", ",", ".", "?"]
        first_line_numeric = ["7", "8", "9"]
        second_line_numeric = ["4", "5", "6"]
        third_line_numeric = ["1", "2", "3"]
        fourth_line_numeric = ["0"]
        global ButtonSymbols
        ButtonSymbols = tk.Button(frame_keyboard, text="?123", height=2, width=10, background="light blue",
                                  command=lambda: self.control_buttonSymbols())
        ButtonSymbols.place(x=position_first_line[0] - 100,
                            y=position_first_line_numeric[1] + distance_between_lines * 2)

        spaceButton = tk.Button(frame_keyboard, text=" ", height=2, width=10, background="light blue",
                                command=lambda: fk(root=frame_keyboard, text_field=text_field).print_value(" ")).place(x=position_first_line[0] + 120,
                           y=position_first_line_numeric[1] + distance_between_lines * 3 + 10)
        enterButton = tk.Button(frame_keyboard, text="Enter", height=2, width=10, background="light blue", command=lambda: fk(text_field=text_field).print_value("\n")).place(x=position_first_line[0] + 405, y=position_first_line[1]*2+15)

        global ButtonCapsLock
        ButtonCapsLock = tk.Button(frame_keyboard, text="caps", height=2, width=10, background="light blue",
                                   command=self.change_color)
        ButtonCapsLock.place(x=position_first_line[0] - 100, y=position_first_line[1] + self.distance_between_buttons)

        self.backspace_button = tk.Button(frame_keyboard, text="Backspace", height=2, width=10, background="light blue",
                                          command=lambda: fk(text_field=text_field).backspace())
        self.backspace_button.place(x=position_first_line[0] + 405, y=position_first_line[1])
        self.buttons = []
        self.build_keyboard(first_line, position_first_line[0], position_first_line[1])
        self.build_keyboard(second_line, position_first_line[0], (position_first_line[1] + distance_between_lines))
        self.build_keyboard(third_line, position_first_line[0], (position_first_line[1] + distance_between_lines * 2))
        self.build_keyboard(first_line_numeric, position_first_line_numeric[0], position_first_line_numeric[1])
        self.build_keyboard(second_line_numeric, position_first_line_numeric[0],
                            (position_first_line_numeric[1] + distance_between_lines))
        self.build_keyboard(third_line_numeric, position_first_line_numeric[0],
                            (position_first_line_numeric[1] + distance_between_lines * 2))
        self.build_keyboard(fourth_line_numeric, position_first_line_numeric[0] + self.distance_between_buttons,
                            (position_first_line_numeric[1] + distance_between_lines * 3 + 10))

    def build_keyboard(self, line, position_x, position_y):
        for letter in line:
            button = tk.Button(self.frame_keyboard, text=letter, height=2, width=2, background="light blue",
                               command=lambda position_x=position_x, position_y=position_y, letter=letter: [
                                   wp(self.frame_keyboard, self.text_field).control_prediction(letter),
                                   fk(root=self.frame_keyboard, text_field=self.text_field).control_button(letter,                                                                             position_x,
                                                                                                           position_y)])

            if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
                button.bind("<Button-3>", lambda event, position_x=position_x, position_y=position_y: fk(
                    root=self.frame_keyboard, text_field=self.text_field).syllable_bar(position_x, position_y))
            button.place(x=position_x, y=position_y)
            self.buttons.append(button)
            position_x += self.distance_between_buttons
            print(letter)

    def hilde_keyboard(self):
        for button in self.buttons:
            button.destroy()

    def change_color(self):
        if ButtonCapsLock["background"] == "light blue":
            ButtonCapsLock.configure(background="#0752F2")
        else:
            ButtonCapsLock.configure(background="light blue")

    def control_buttonSymbols(self):
        if self.is_activated_sk is False:
            self.sk.build_keyboard()
            self.is_activated_sk = True
        else:
            self.sk.destroy_keyboard()
            self.is_activated_sk = False


