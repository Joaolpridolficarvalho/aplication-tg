from tkinter import Canvas, ttk, Label
from Functions_favorite_section import Functions_favorite_section as ffs


class Canvas_elements:
    def __init__(self, root, fk, frame_favorite):
        self.root = root
        self.fk = fk
        self.frame_favorite = frame_favorite
        self.path = r"D:\favorite.txt"
        self.ffs = ffs(self.path, self.frame_favorite, self.fk)
        style_font = "Arial"
        font_size = 11
        toolbar = Canvas(root, width=1024, height=30, background="black", border=2)
        toolbar.place(x=0, y=0)
        try:
            self.ffs.show_favorite()
            self.ffs.show_trash()
            self.ffs.show_pencil()
        except:
            pass

        button_favorite = toolbar.create_oval(100, 90, 5, 67, fill="#07C7F2", tags="button_favorite")
        button_place = toolbar.move("button_favorite", 275, -62)
        text_favorite = toolbar.create_text(325, 15, text="Favoritar", fill="white", font=[style_font, font_size],
                                            tags="text_favorite")
        toolbar.tag_bind("button_favorite", '<Button-1>',
                         lambda event: self.ffs.add_favorite())
        toolbar.tag_bind("text_favorite", '<Button-1>', lambda event: self.ffs.add_favorite())

        pitch = Label(self.root, text="Tom", font=[style_font, font_size], background="black",
                      foreground="white").place(x=400, y=8)
        pitch_choose = ttk.Scale(self.root, from_=0, to=100, orient="horizontal").place(x=450, y=8)
