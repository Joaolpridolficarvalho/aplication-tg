import tkinter as tk
from tkinter import ttk

class Functions_favorite_section:
    def __init__(self, path, frame_favorite, fk):
        self.frame_favorite = frame_favorite
        self.path = path
        self.fk = fk
        self.favorite = []
        self.delimiter = ">/"
        self.x = 20
        self.y = 45
        self.scrollbar = ttk.Scrollbar(self.frame_favorite, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")
        self.frame = tk.Canvas(self.frame_favorite, background="green")
        self.frame.pack(side="left", fill="both", expand=True)
        self.scrollbar.config(command=self.frame.yview)
        self.frame.config(yscrollcommand=self.scrollbar.set)  # Link scrollbar to canvas
        self.update_scroll_region()

    def update_scroll_region(self):
        self.frame.update_idletasks()
        self.frame.config(scrollregion=self.frame.bbox("all"))

    def add_favorite(self):
        text = self.fk.get_text()
        # Simulating file modification
        self.favorite.append(text)  # Add to the list for demonstration purposes
        self.display_favorite()
        self.update_scroll_region()

    def delete_favorite(self, text):
        if text in self.favorite:
            self.favorite.remove(text)
            self.display_favorite()
            self.update_scroll_region()

    def display_favorite(self):
        self.frame.delete("all")  # Clear the canvas
        self.y = 45
        for favorite in self.favorite:
            label = tk.Label(self.frame, text=favorite, font=("Arial", 18), anchor="w")
            label.place(x=self.x, y=self.y + 5)
            self.y += 30

if __name__ == "__main__":
    root = tk.Tk()
    frame_favorite = tk.Frame(root)
    frame_favorite.pack(fill="both", expand=True)

    fk = FakeFK()  # You should replace this with your own implementation of `fk`

    functions = Functions_favorite_section("sample_path", frame_favorite, fk)

    add_button = tk.Button(root, text="Add Favorite", command=functions.add_favorite)
    add_button.pack()

    delete_button = tk.Button(root, text="Delete Favorite", command=lambda: functions.delete_favorite("Item 1"))
    delete_button.pack()

    root.mainloop()
