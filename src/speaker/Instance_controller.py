from Keyboard import Keyboard as kb
from tkinter import Button
from File_manager import File_manager
from Canvas_elements import Canvas_elements as ce
from Functions_keyboard import Functions_keyboard as fk
class Instance_controller:
    def __init__(self, root, frame_favorite, frame_keyboard, text_field, toolbar):
        self.text_field = text_field
        print(type(self.text_field))
        kb(frame_keyboard, self.text_field)
        ce(root, frame_favorite, self.text_field, toolbar)


