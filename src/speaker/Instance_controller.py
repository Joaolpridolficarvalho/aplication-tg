from Keyboard import Keyboard as kb
from Menu import Menu as menu
from tkinter import Button
from File_manager import File_manager
from Canvas_elements import Canvas_elements as ce
from Functions_keyboard import Functions_keyboard as fk
class Instance_controller:
    def __init__(self, root, frame_favorite, frame_keyboard, text_field):
        self.fk = fk(frame_keyboard, text_field)
        self.text_field = text_field
        kb(frame_keyboard, self.fk)
        menu(frame_favorite, text_field)
        ce(root,  self.fk)
        menu_button = Button(frame_keyboard, text="☰", background="black", foreground="white", command=menu(root, File_manager).show_menu).place(x=960, y=5)