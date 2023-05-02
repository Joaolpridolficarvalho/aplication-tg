class Favorite_section:
    def __init__(self, frame_favorite, path):
        self.frame_favorite = frame_favorite
        self.path = path



    def get_favorite(self):
        with open("favorite.txt", "r") as file:
            return file.read()