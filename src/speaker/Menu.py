from tkinter import Button, Frame
from File_manager import File_manager

class Menu:
    def __init__(self, root, text_field):
        self.root = root
        self.text_field = text_field
        self.file_manager = File_manager(self.text_field)


    def open_menu(self):
        self.show_menu()

    def show_menu(self):
        global frame_menu
        frame_menu = Frame(self.root, width=55, height=60, background="#07C7F2")
        frame_menu.place(x=950, y=24)

        global open_file
        open_file = Button(self.root, text="Abrir", width=5, height=1, font=("Arial", 12),
                           border=0, background="#07C7F2", foreground="white",
                           command=self.file_manager.select_file)
        open_file.place(x=950, y=30)
        open_file.bind("<Enter>", func=lambda e: open_file.config(background="gray"))
        open_file.bind("<Leave>", func=lambda e: open_file.config(background="#07C7F2"))

        global save_file
        save_file = Button(self.root, text="Salvar", width=5, height=1, font=("Arial", 12),
                           border=0, background="#07C7F2", foreground="white",
                           command=self.file_manager.save_file)
        save_file.place(x=950, y=54)
        save_file.bind("<Enter>", func=lambda e: save_file.config(background="gray"))
        save_file.bind("<Leave>", func=lambda e: save_file.config(background="#07C7F2"))

    def close(self):
        frame_menu.destroy()
        open_file.destroy()
        save_file.destroy()
