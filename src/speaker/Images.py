from PIL import Image, ImageTk


class Images:
    def __init__(self):
        pass

    def open_image(self, path):
        image = Image.open(path)
        return image

    def load_image(self, path):
        image = ImageTk.PhotoImage(self.open_image(path))
        return image