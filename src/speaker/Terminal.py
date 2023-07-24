import shlex
import subprocess
from Functions_keyboard import Functions_keyboard as fk


class Terminal:

    def __init__(self, text_field):
        self.text_field = text_field
        self.fk = fk(text_field=self.text_field)

    def speak(self):
        text = self.fk.get_text().strip()
        command = ['espeak-ng', '-w', f'./{text}.wav', text]

        subprocess.run(command, shell=False)
        command = ['aplay', f'./{text}.wav']
        subprocess.run(command, shell=False)

    def change_voice(self, voice):
        subprocess.run(['espeak-ng', '-v', voice], shell=False)

    def list_voices(self):
        command = ['espeak-ng', '--voices']
        list_voice = subprocess.check_output(command)
        return list_voice
