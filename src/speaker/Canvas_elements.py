from tkinter import Canvas, ttk, Label, Button
from Functions_favorite_section import Functions_favorite_section as ffs
from Menu import Menu as menu

class Canvas_elements:
    def __init__(self, root, frame_favorite, text_field, toolbar):
        self.root = root
        self.frame_favorite = frame_favorite
        self.text_field = text_field
        self.path = r"D:\favorite.txt"
        self.ffs = ffs(self.path, self.frame_favorite, self.text_field)
        style_font = "Arial"
        font_size = 11
        self.toolbar = toolbar

        try:
            self.ffs.show_favorite()
            self.ffs.show_trash()
            self.ffs.show_pencil()
        except:
            pass

        button_favorite = self.toolbar.create_oval(100, 90, 5, 67, fill="#07C7F2", tags="button_favorite")
        button_place = self.toolbar.move("button_favorite", 275, -62)
        text_favorite = self.toolbar.create_text(325, 15, text="Favoritar", fill="white", font=[style_font, font_size],
                                            tags="text_favorite")
        toolbar.tag_bind("button_favorite", '<Button-1>',
                         lambda event: self.ffs.add_favorite)
        toolbar.tag_bind("text_favorite", '<Button-1>', lambda event: self.ffs.add_favorite)
        menu_button = Button(toolbar, text="☰", background="black", foreground="white", command= menu(root, text_field).show_menu).place(x=960, y=5)

        pitch = Label(self.root, text="Tom", font=[style_font, font_size], background="black",
                      foreground="white").place(x=400, y=8)
        pitch_choose = ttk.Scale(self.frame_favorite, from_=0, to=100, orient="horizontal").place(x=450, y=8)
