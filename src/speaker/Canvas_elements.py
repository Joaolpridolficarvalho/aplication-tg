from tkinter import Canvas, StringVar, ttk, Label
from Functions_favorite_section import Functions_favorite_section as ffs

class Canvas_elements:
    def __init__(self, root=None, text_field=None):
        self.root = root
        self.text_field = text_field
        self.path = r"D:\Documentos\favorite.txt"
        style_font = "Arial"
        font_size = 11
        toolbar = Canvas(root, width=1024, height=30, background="black", border=2)
        toolbar.place(x=0, y=0)

        button_favorite = toolbar.create_oval(100, 90, 5, 67, fill="#07C7F2", tags="button_favorite")
        button_place = toolbar.move("button_favorite", 275, -62)
        text_favorite = toolbar.create_text(325, 15, text="Favoritar", fill="white", font=[style_font, font_size],
                                            tags="text_favorite")
        toolbar.tag_bind("button_favorite", '<Button-1>',
                         lambda event: ffs(self.path, self.root, self.text_field).add_favorite())
        toolbar.tag_bind("text_favorite", '<Button-1>', lambda event: ffs(self.path,self.root, text_field).add_favorite())

        pitch = Label(self.root, text="Tom", font=[style_font, font_size], background="black",
                      foreground="white").place(x=400, y=8)
        pitch_choose = ttk.Scale(self.root, from_=0, to=100, orient="horizontal").place(x=450, y=8)

