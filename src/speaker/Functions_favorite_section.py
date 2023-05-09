import File_manager as fm
import Functions_keyboard as fk
import tkinter as tk

class Functions_favorite_section:
    def __init__(self, frame_favorite, path):
        self.frame_favorite = frame_favorite
        self.path = path
        self.fm = fm.File_manager(self.path)
        self.fk = fk.Functions_keyboard()
        self.favorite = []

    def add_favorite(self, text_field):
        text = self.fk.get_text(text_field)
        self.fm.edit_file(text)
        self.show_favorite()

    def delete_favorite(self, text_field):
        text = self.fk.get_text(text_field)
        self.fm.delete_sentence(text)
        self.show_favorite()
    def show_favorite(self):
        for item, h in self.fm.get_sentence():
            self.favorite[item] = tk.Button(self.frame_favorite, text=item, height=5, width=10, background="white", font=("Arial", 18)).place(x=0, y=h)



    