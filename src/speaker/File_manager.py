from tkinter import filedialog
from Functions_keyboard import Functions_keyboard as fk

class File_manager:
    def __init__(self, text_field=None):
        self.text_field = text_field
        self.delimiter = ">/"

    def edit_file(self, text, file_name, mode='w'):

        with open(file_name, mode) as f:
            text = str(text)
            f.write(text)

    def read_file(self, file_name):
        with open(file_name, "r") as f:
            content = f.read()
            return content

    def replace_sentence(self, old_sentence, new_sentence, file_name):
        content = self.read_file(file_name)
        new_sentence = str(new_sentence)
        content = content.replace(old_sentence, new_sentence)
        self.edit_file(content, file_name)
    def get_sentence(self, file_name):
        content = self.read_file(file_name)
        sentence = content.split(self.delimiter)
        return sentence

    def search_sentence(self, sentence, file_name):
        content = self.read_file(file_name)
        result = content.find(sentence)
        return result

    def delete_sentence(self, sentence, file_name):
        content = self.read_file(file_name)
        text = content.replace(sentence, "")
        self.edit_file(text, file_name)

    def select_file(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Abrir",
                                              filetypes=[("Arquivos de texto", "*.txt")])
        if filename:
            content = self.read_file(filename)
            fk().print_value(content, self.text_field)

    def save_file(self):
        filename = filedialog.asksaveasfilename(initialdir="/", defaultextension=".txt",
                                                title="Salvar", filetypes=[("Arquivos de texto", "*.txt")])
        if filename:
            content = fk().get_text(self.text_field)
            self.edit_file(content, filename)


if __name__ == '__main__':
    file_manager = File_manager()
    file_manager.edit_file("Olá, tudo bem?", "./arquivo.txt")

    file_manager.delete_sentence("?", "arquivo.txt")
    content = file_manager.read_file("arquivo.txt")
    print(content)
