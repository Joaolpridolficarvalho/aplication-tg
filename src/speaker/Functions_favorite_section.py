import File_manager as fm

import tkinter as tk
import Images as img



class Functions_favorite_section:
    def __init__(self, path, frame_favorite, fk):
        self.frame_favorite = frame_favorite
        self.path = path
        self.img = img.Images()
        self.fk = fk
        self.fm = fm.File_manager()
        self.favorite = []
        self.button_trash = []
        self.button_pencil = []
        self.trash = r"/Documentos/Speaker/aplication-tg/Img\delete.png"
        self.pencil = r"/Documentos/Speaker/aplication-tg/Img\Img\pencil.png"
        self.delimiter = ">/"
        self.x = 20
        self.y = 45

    #ok
    def add_favorite(self):

        text = self.fk.get_text()
        self.fm.edit_file(text+self.delimiter, self.path, 'a')
        self.control_favorite()


    def edit_favorite(self, text):
        self.fk.print_value(text)



    def delete_favorite(self, text):
        
        self.fm.delete_sentence(text, self.path)
        self.control_favorite()

    def show_favorite(self):
        for index, favorite in enumerate(self.fm.get_sentence(self.path)):
            if favorite !='':
                label = tk.Label(self.frame_favorite, text=favorite, font=("Arial", 18), highlightbackground="yellow", background="yellow")
                label.place(x=self.x, y=self.y + 5)
                label.bind("label", '<Button-1>', lambda event: self.fk.print_value(label))
                self.favorite.append(label)
                self.y += 30
                print(index)
        self.y = 30
        print(len(self.favorite))
    def show_trash(self):
        for index, favorite in enumerate(self.favorite):
            if favorite !='': 
               self.button_trash.append(tk.Button(self.frame_favorite, text="exclui",
                                               command=lambda: self.delete_favorite(self.favorite[index].cget("text")), background="red",                                border=2,
                                               height=5, width=5)) 
               self.button_trash[index].place(x=self.x+200, y=self.y)
               self.y += 30
        self.y = 30

    def show_pencil(self):
        for index, favorite in enumerate(self.favorite):
            if favorite !='':
               self.button_pencil.append(tk.Button(self.frame_favorite, text="edita",
                                               command=lambda: self.edit_favorite(self.favorite[index].cget("text")), background="#07C7F2", border=2, height=5, width=5))
               self.button_pencil[index].place(x=self.x + 230, y=self.y)
               self.y += 30
        self.y = 30

#image=self.img.load_image(self.pencil)
    def hide_trash(self):
        for item in self.button_trash:
            item.place_forget()

    def hide_pencil(self):
        for item in self.button_pencil:
            item.place_forget()

    def hide_favorite(self):
        for item in self.favorite:
            item.place_forget()
        self.favorite.clear()

    def hide_all(self):
        self.hide_favorite()
        self.hide_trash()
        self.hide_pencil()

    def control_favorite(self):
        try:
            self.hide_all()
        finally:
            self.show_favorite()
            self.show_trash()
            self.show_pencil()
