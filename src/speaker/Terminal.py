import sys
from pathlib import Path
import subprocess
class Terminal:


# Open a new command prompt window in the C:\Windows\System32 directory
#subprocess.run(['cmd', '/c', 'start', '/D', 'C:\\Windows\\System32'])

    def __init__(self):
        #self.test()
        self.folder = Path(r"C:\Users\Joao\Downloads\balcon")

        self.speake("Hello World")



    def speake(self, text):
       subprocess.run(['cmd', '/c', 'start', '/D', self.folder, 'balcon.exe', '-t', text])

    def change_voice(self, voice):
        subprocess.run(['cmd', '/c', 'start', '/D', self.folder, 'balcon.exe', ' --voice1-name', voice])

if __name__ == "__main__":
    Terminal()