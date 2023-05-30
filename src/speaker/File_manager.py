from tkinter import filedialog
from Functions_keyboard import Functions_keyboard as fk

class File_manager:
    def __init__(self):
        self.words = 0
    def edit_file(self, text, file_name, mode='w' ):
        with open(file_name, mode) as f:
            text = str(text)
            f.write(text)



    def read_file(self, file_name):
        with open(file_name, "r") as f:
            content = f.read()
            return content
    def get_sentence(self, file_name):
        content = self.read_file(file_name)
        sentence = content.split()
        return sentence

    def seach_sentence(self, sentence, file_name):
        content = self.read_file(file_name)
        result = content.index(sentence)
        return result

    def delete_sentence(self, sentence, file_name):
        content = self.read_file(file_name)
        text = content.replace(sentence, "")
        self.edit_file(text, "w")

    def select_file(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Abrir", filetypes=[("Arquivos de texto", "*.txt")] )
        fk().control_button(self.read_file(filename), 0, 0)
    def save_file(self):
        filename = filedialog.asksaveasfilename(initialdir="/", title="Salvar", filetypes=[("Arquivos de texto", "*.txt")])
        return filename




if __name__ == '__main__':
    file_manager = File_manager(path)
    file_manager.edit_file("Olá, tudo bem?")

    file_manager.delete_sentence("?")
    content = file_manager.read_file()
    print(content)