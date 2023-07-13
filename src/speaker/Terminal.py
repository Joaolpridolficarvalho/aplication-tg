import sys
import subprocess
from Functions_keyboard import Functions_keyboard as fk


class Terminal:

    def __init__(self, text_field):
        self.text_field = text_field
        self.fk = fk(text_field=self.text_field)

    def speak(self):
    	text = self.fk.get_text()
    	command = ['nohup espeak-ng '+ text]
    	subprocess.Popen(command, shell=True)

    def change_voice(self, voice):
        subprocess.run(['cmd', '/c', 'start', '/D', self.folder, 'balcon.exe', ' --voice1-name', voice])
