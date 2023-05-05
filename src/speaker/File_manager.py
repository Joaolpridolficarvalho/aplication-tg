

class File_manager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.words = 0
    def edit_file(self, text, mode="a"):
        with open(self.file_name, mode) as f:
            text = str(text)
            f.write(text)



    def read_file(self):
        with open(self.file_name, "r") as f:
            content = f.readline()
            return content
    def get_sentence(self):
        content = self.read_file()
        sentence = content.split()
        return sentence

    def seach_sentence(self, sentence):
        content = self.read_file()
        result = content.index(sentence)
        return result

    def delete_sentence(self, sentence):
        content = self.read_file()
        text = content.replace(sentence, "")
        self.edit_file(text, "w")



path = r"D:\Documentos\teste.txt"


if __name__ == '__main__':
    file_manager = File_manager(path)
    file_manager.edit_file("Olá, tudo bem?")

    file_manager.delete_sentence("?")
    content = file_manager.read_file()
    print(content)