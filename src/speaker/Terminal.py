import sys
from pathlib import Path
import subprocess


class Terminal:

    def __init__(self):
        self.folder = Path(r"D:\Downloads\balcon")

    def speak(self, text):
        subprocess.run(['cmd', '/c', 'start', '/D', self.folder, 'balcon.exe', '-t', text])

    def change_voice(self, voice):
        subprocess.run(['cmd', '/c', 'start', '/D', self.folder, 'balcon.exe', ' --voice1-name', voice])