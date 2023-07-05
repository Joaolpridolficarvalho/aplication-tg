from tkinter import filedialog

class File_manager:
    def __init__(self, fk):
        self.fk = fk
        self.delimiter = ">/"

    def edit_file(self, text, file_name, mode='w'):

        with open(file_name, mode) as f:
            text = str(text)
            print(text)
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
        print(sentence)
        return sentence

    def search_sentence(self, sentence, file_name):
        content = self.read_file(file_name)
        result = content.find(sentence)
        return result

    def delete_sentence(self, sentence, file_name):
        sentence = str(sentence+ '\n>/')
        content = self.read_file(file_name)
        text = content.replace(sentence, "") 
        self.edit_file(text, file_name)
        
    def proccess_sentence(self, file_name):
        sentences = self.get_sentence(file_name)
        sentences = ''.join(sentences)
        sentences = sentences.strip()
        sentences = self.strtolist(sentences)
        print (sentences)
        return sentences
        
    def strtolist(self, sentence):
        li = list(sentence.split("\n")) 
       
        return li 
     
    def select_file(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Abrir",
                                              filetypes=[("Arquivos de texto", "*.txt")])
        if filename:
            content = self.read_file(filename)
            self.fk.print_value(content)

    def save_file(self):
        filename = filedialog.asksaveasfilename(initialdir="/", defaultextension=".txt",
                                                title="Salvar", filetypes=[("Arquivos de texto", "*.txt")])
        if filename:
            content = self.fk.get_text()
            self.edit_file(content, filename)


if __name__ == '__main__':
    file_manager = File_manager()
    file_manager.edit_file("Olá, tudo bem?", "./arquivo.txt")

    file_manager.delete_sentence("?", "arquivo.txt")
    content = file_manager.read_file("arquivo.txt")
    print(content)
