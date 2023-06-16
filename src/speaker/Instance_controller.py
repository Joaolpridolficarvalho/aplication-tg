from Keyboard import Keyboard as kb
from Menu import Menu as menu
from tkinter import Button
from File_manager import File_manager
from Canvas_elements import Canvas_elements as ce

class Instance_controller:
    def __init__(self, root, frame_favorite, frame_keyboard, text_field):

        self.text_field = text_field
        kb(frame_keyboard, self.text_field)
        menu(frame_favorite, self.text_field)
        ce(root,  self.text_field)
        menu_button = Button(frame_keyboard, text="☰", command=menu(root, File_manager).show_menu).place(x=960, y=8)