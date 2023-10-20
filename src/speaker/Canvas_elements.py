from tkinter import Canvas, ttk, Label, Button, Tk, Frame, Text
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

        # Create a circular button (oval) with original dimensions
        button_favorite = self.toolbar.create_oval(100, 90, 5, 67, fill="#07C7F2", tags="button_favorite")
        self.toolbar.tag_bind("button_favorite", '<Button-1>', self.handle_button_favorite_click)
        button_place = self.toolbar.move("button_favorite", 275, -62)

        # Create the original text on the button
        text_favorite = self.toolbar.create_text(22, 22, text="Favoritar", fill="white", font=[style_font, font_size], tags="text_favorite")
        self.toolbar.tag_bind("button_favorite", '<Button-1>', self.handle_button_favorite_click)
        text_favorite = self.toolbar.move("text_favorite", 305, -5)
        menu_button = Button(self.toolbar, text="☰", background="black", foreground="white", command=lambda: menu(self.root, self.text_field).show_menu())
        menu_button.place(x=960, y=5)

        pitch = Label(self.root, text="Tom", font=[style_font, font_size], background="black", foreground="white")
        pitch.place(x=400, y=8)

        pitch_choose = ttk.Scale(self.frame_favorite, from_=0, to=100, orient="horizontal")
        pitch_choose.place(x=450, y=8)

    def handle_button_favorite_click(self, event):
        self.ffs.add_favorite()  
if __name__ == "__main__":
    root = Tk()
    frame_favorite = Frame(root)
    text_field = Text(root)
    toolbar = Canvas(root, width=1000, height=50)  # Adjust the canvas dimensions as needed

    canvas_elements = Canvas_elements(root, frame_favorite, text_field, toolbar)

    root.mainloop()
