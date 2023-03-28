import tkinter
from tkinter import *
import string
class On_screen_keyboard:

    window = Tk()
    window.geometry("500x500")
    window.title("Keyboard")
    window.configure(background="black")
    lbl = Label(window, text="Keyboard", font=("Arial Bold", 50, "bold"), bg="black", padx=12)
    lbl.grid(column=0, row=0)
    frame = Frame(window, bd=10, width=500, height=500, relief=RIDGE).grid(column=1, row=0, padx=10, pady=30)
    keys =[["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
                [string.ascii_letters]]
    for i, key_row in enumerate(keys):
        for j, key in enumerate(key_row):
            button = Button(frame, text=key,  height=2, width=5).grid(row=i, column=10)
    display = tkinter.Entry(frame, width=50, bg="white", fg="black", font=("Arial Bold", 20, "bold"))
    display=display.grid(row=0, column=0).grid(row=len(keys), column=0, columnspan=len(keys[0]), padx=10, pady=30)
    def button_click(self, key):
        current_key = display.get()
        display.delete(0, tk.END)
        display.insert(0, str(current_key) + str(key))
    for i, key_row in enumerate(keys):
        for j, key in enumerate(key_row):
            button = Button(frame, text=key, font=("Arial Bold", 20, "bold"), height=2, width=5, command=lambda key=key: button_click(key)).grid(row=i, column=j)

    window.mainloop()
if __name__ == "__main__":
    On_screen_keyboard()