from tkinter import Button
from Functions_keyboard import Functions_keyboard as fk

class Symbol_keyboard:
    def __init__(self, frame_keyboard, text_field):
        self.text_field = text_field
        self.fk = fk(text_field=text_field)
        self.frame_keyboard = frame_keyboard
        self.symbol_buttons = []

    def build_keyboard(self):
        position_last_line = 0

        symbols_row1 = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        symbols_row2 = ['_', '-', '+', '=', '{', '}', '[', ']', '|', '\\']
        symbols_row3 = [':', ';', '<', '>', ',', '.', '?', '/', '`', '~']

        position_last_line = self.create_symbol_buttons(symbols_row1, 360, position_last_line - 90)
        position_last_line = self.create_symbol_buttons(symbols_row2, 360, position_last_line - 45)
        self.create_symbol_buttons(symbols_row3, 360, position_last_line)

    def destroy_keyboard(self):
        for button in self.symbol_buttons:
            button.destroy()
        self.symbol_buttons.clear()

    def create_symbol_buttons(self, symbols, x_start, y_start):
        x, y = x_start, y_start
        spacing_x = 40  # Adjust the horizontal spacing between buttons
        spacing_y = 50  # Adjust the vertical spacing between rows
        for symbol in symbols:
            button = Button(self.frame_keyboard, text=symbol, height=2, width=2, background="light blue",
                            command=lambda s=symbol: [self.fk.print_value(s), self.destroy_keyboard()])
            button.place(x=x, y=y)
            self.symbol_buttons.append(button)
            x += spacing_x  # Move horizontally to the next button position
        y += spacing_y  # Move vertically to the next row
        return y  # Return the updated y position

# Example usage:
# frame_keyboard = ...  # replace with your actual frame
# text_field = ...  # replace with your actual text field
# symbol_keyboard = Symbol_keyboard(frame_keyboard, text_field)
# symbol_keyboard.build_keyboard()

