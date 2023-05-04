

class File_manager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.words = 0
    def edit_file(self, text):
        with open(self.file_name, "a", encoding="utf-8") as f:
            text = str(text)
            f.write(text)



    def read_file(self):
        with open(self.file_name, "r", encoding="utf-8") as f:
            content = f.readline()
            return content
    def get_sentence(self):
        content = self.read_file()
        sentence = content.split("//")
        return sentence

    def seach_sentence(self, sentence):
        content = self.read_file()
        result = content.index(sentence)
        return result

    def delete_sentence(self, sentence):
        content = self.read_file()
        text = content.replace(sentence, "")
        self.edit_file(text)



path = r"D:\Documentos\teste.txt"


if __name__ == '__main__':
    file_manager = File_manager(path)
    file_manager.edit_file("Olá, tudo bem?")

    file_manager.delete_sentence("?")
