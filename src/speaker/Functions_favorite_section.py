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
        self.button_pencil = []
        self.trash = r"D:\Documentos\estágio\Speaker\aplication-tg\Img\delete.png"
        self.pencil = r"D:\Documentos\estágio\Speaker\aplication-tg\Img\pencil.png"
        self.delimiter = ">/"
        self.x = 15
        self.y = 30

    #ok
    def add_favorite(self):

        text = self.fk.get_text()
        self.fm.edit_file(text+self.delimiter, self.path, 'a')
        try:
            self.hide_favorite()
        finally:
            self.show_favorite()
            self.show_trash()
            self.show_pencil()

    def edit_favorite(self,  old_text):
        self.fk.print_value(old_text)
        new_text = self.fk.get_text()
        self.fm.replace_sentence(old_text, new_text, self.path)
        self.show_favorite()



    def delete_favorite(self, text):
        self.fm.delete_sentence(text, self.path)
        self.show_favorite()

    def show_favorite(self):
        for index, favorite in enumerate(self.fm.get_sentence(self.path)):
            label = tk.Label(self.frame_favorite, text=favorite, font=("Arial", 18), highlightbackground="yellow")
            label.place(x=self.x, y=self.y)
            self.favorite.append(label)
            self.y += 30
        self.y = 30
    def show_trash(self):
        for index, trash in enumerate(self.favorite):
            self.button_trash.append(tk.Button(self.frame_favorite, image=self.img.load_image(self.trash),
                                               command=lambda: self.delete_favorite(self.favorite[index]), background="red", border=2,
                                               height=5, width=5))
            self.button_trash[index].place(x=self.x+200, y=self.y)
            self.y += 30
        self.y = 30

    def show_pencil(self):
        for index, pencil in enumerate(self.favorite):
            self.button_pencil.append(tk.Button(self.frame_favorite, image=self.img.load_image(self.pencil),
                                               command=lambda: self.edit_favorite(self.favorite[index]), background="#07C7F2", border=2,
                                               height=22, width=2))
            self.button_pencil[index].place(x=self.x + 230, y=self.y)
            self.y += 30
        self.y = 30


    def hide_trash(self):
        for item in self.button_trash:
            item.grid_forget()

    def hide_pencil(self):
        for item in self.button_trash:
            item.grid_forget()

    def hide_favorite(self):
        for item in self.favorite:
            item.place_forget()

    def hide_all(self):
        self.hide_favorite()
        self.hide_trash()
        self.hide_pencil()

    def control_favorite(self):
        try:
            self.hide_all()
        except:
            self.show_favorite()
            self.show_trash()
            self.show_pencil()