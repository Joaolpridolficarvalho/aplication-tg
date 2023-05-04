import File_manager
import Functions_keyboard as fk

class Favorite_section:
    def __init__(self, frame_favorite, path):
        self.frame_favorite = frame_favorite
        self.path = path
        self.fm = File_manager.File_manager(self.path)




    def add_favorite(self, text):

