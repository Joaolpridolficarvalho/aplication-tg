import File_manager as fm

import tkinter as tk
import Images as img
import Functions_keyboard as fk


class Functions_favorite_section:
    def __init__(self, path, frame_favorite, text_field):
        self.text_field = text_field
        self.frame_favorite = frame_favorite
        self.path = path
        self.img = img.Images()
        self.fm = fm.File_manager(self.text_field)
        self.fk = fk.Functions_keyboard()
        self.favorite = []
        self.button_trash = []
        self.trash = r"D:\Documentos\estágio\Speaker\aplication-tg\Img\delete.png"
        self.pencil = r"D:\Documentos\estágio\Speaker\aplication-tg\Img\pencil.png"
      #  self.show_favorite()
        self.delimiter = ">/"
    #ok
    def add_favorite(self):

        text = self.fk.get_text(self.text_field)
        self.fm.edit_file(text, self.path)
        self.show_favorite()

    def delete_favorite(self):
        text = self.fk.get_text(self.text_field)
        self.fm.delete_sentence(text+"\n", self.path)
        self.show_favorite()

    def show_favorite(self):
        for item, line in enumerate(self.fm.get_sentence(self.path)):
            self.favorite.append(tk.Label(self.frame_favorite, text=item, background="black", font=("Arial", 18),
                                          border=2, width=20, height=2))
            self.favorite[item].grid(row=line, column=0)

    def show_trash(self):
        for item, line in enumerate(self.favorite):
            self.button_trash.append(tk.Button(self.frame_favorite, img=self.img.load_image(self.trash),
                                               command=lambda: self.delete_favorite(), background="red", border=2,
                                               height=2, width=2))
            self.button_trash[item].grid(row=line, column=1)

    def show_pencil(self):
        for item, line in enumerate(self.favorite):
            self.button_trash.append(tk.Button(self.frame_favorite, img=self.img.load_image(self.pencil),
                                               command=lambda: self.delete_favorite(), background="red", border=2,
                                               height=2, width=2))
            self.button_trash[item].grid(row=line, column=2)
