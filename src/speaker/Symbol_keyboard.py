class Symbol_keyboard:
    def __init__(self, root, fk):
        self.root = root
        self.fk = fk

        position_last_line = 130

        symbols_row1 = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        symbols_row2 = ['_', '-', '+', '=', '{', '}', '[', ']', '|', '\\']
        symbols_row3 = [':', ';', '<', '>', ',', '.', '?', '/', '`', '~']
        
        self.create_symbol_buttons(root, symbols_row1, 400, position_last_line - 90)
        self.create_symbol_buttons(root, symbols_row2, 400, position_last_line - 45)
        self.create_symbol_buttons(root, symbols_row3, 400, position_last_line)

        ButtonBackspace = tk.Button(root, text="Backspace", height=2, width=10, background="light blue",
                                    command=lambda: fk.backspace()).place(x=650, y=position_last_line - 90)

        ButtonCapsLock = tk.Button(root, text="Caps", height=2, width=10, background="light blue",
                                   command=lambda: [fk.set_uppercase(), self.change_color()])
        ButtonCapsLock.place(x=320, y=position_last_line - 45)

        # Adicione mais botões de símbolos conforme necessário

    def create_symbol_buttons(self, root, symbols, x_start, y_start):
        x, y = x_start, y_start
        for symbol in symbols:
            button = tk.Button(root, text=symbol, height=2, width=2, background="light blue",
                               command=lambda s=symbol: fk.print_value(s))
            button.place(x=x, y=y)
            x += 25  # Espaçamento horizontal entre os botões

    
