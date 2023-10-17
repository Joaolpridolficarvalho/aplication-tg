class SymbolKeyboard:
    def __init__(self, frame_keyboard, fk):
        self.amount_of_words = 0
        self.fk = fk
        self.frame_keyboard = frame_keyboard
        self.symbol_buttons = []

    def build_keyboard(self):
        position_last_line = 130

        symbols_row1 = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        symbols_row2 = ['_', '-', '+', '=', '{', '}', '[', ']', '|', '\\']
        symbols_row3 = [':', ';', '<', '>', ',', '.', '?', '/', '`', '~']

        self.create_symbol_buttons(symbols_row1, 400, position_last_line - 90)
        self.create_symbol_buttons(symbols_row2, 400, position_last_line - 45)
        self.create_symbol_buttons(symbols_row3, 400, position_last_line)

        ButtonBackspace = tk.Button(self.frame_keyboard, text="Backspace", height=2, width=10, background="light blue",
                                    command=lambda: self.fk.backspace())
        ButtonBackspace.place(x=650, y=position_last_line - 90)

        ButtonCapsLock = tk.Button(self.frame_keyboard, text="Caps", height=2, width=10, background="light blue",
                                   command=lambda: [self.fk.set_uppercase(), self.change_color()])
        ButtonCapsLock.place(x=320, y=position_last_line - 45)

    def destroy_keyboard(self):
        for button in self.symbol_buttons:
            button.destroy()
        self.symbol_buttons.clear()

    def create_symbol_buttons(self, symbols, x_start, y_start):
        x, y = x_start, y_start
        for symbol in symbols:
            button = tk.Button(self.frame_keyboard, text=symbol, height=2, width=2, background="light blue",
                               command=lambda s=symbol: self.fk.print_value(s))
            button.place(x=x, y=y)
            self.symbol_buttons.append(button)
            x += 25  # Espaçamento horizontal entre os botões

    def change_color(self):
        pass
