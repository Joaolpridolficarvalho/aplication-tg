
import Functions_keyboard

class Adapter_interface:

    def __init__(self, root):
        self.root = root
        self.functions_keyboard = Functions_keyboard.Functions_keyboard(root)