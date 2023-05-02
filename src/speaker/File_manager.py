

class File_manager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.words = 0

    def write_text(self):
        try:
            self.edit_file()
        except FileNotFoundError:
            self.create_file()
    def create_file(self):
        with open(self.file_name, "w") as f:
            text = input()
            text = str(text)
            f.write(text)

    def edit_file(self):
        with open(self.file_name, "a") as f:
            text = input()
            f.write(text)


    def read_file(self):
        with open(self.file_name, "r") as f:
            content = f.readline()
            return content
    def get_sentence(self):
        content = self.read_file()
        sentence = content.split()
        return sentence
    def write_file(self, text):
        try:
          self.edit_file()
        except FileNotFoundError:
            self.create_file()

    def seach_sentence(self, sentence):
        content = self.read_file()
        result = content.index(sentence)
        return result

    def delete_sentence(self, sentence):
        with open(self.file_name, "r+") as f:
            for line in f:
                if line.strip('\n') != sentence:
                    f.write(line)



path = r"D:\Documentos\teste.txt"


if __name__ == '__main__':
    file_manager = File_manager(path)
    file_manager.write_text()
    file_manager.read_file()
    file_manager.delete_sentence("teste")
