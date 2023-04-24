import tkinter as tk
class Frame_keyboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master = tk.Frame(self.master, height=300, width=1024, bg="light blue")
        self.master.grid_location(0, 300)



