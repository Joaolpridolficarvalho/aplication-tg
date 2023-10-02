from Keyboard import Keyboard as kb
from tkinter import Button
from File_manager import File_manager
from Canvas_elements import Canvas_elements as ce
from Functions_keyboard import Functions_keyboard as fk
class Instance_controller:
    def __init__(self, root, frame_favorite, frame_keyboard, text_field):
        self.fk = fk(frame_keyboard, text_field)
        self.text_field = text_field
        print(type(self.text_field))
        kb(frame_keyboard, self.fk)
        ce(root,  self.fk, frame_favorite, text_field)


