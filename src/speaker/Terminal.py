import sys
from pathlib import Path
import subprocess
class Terminal:
    def __init__(self):
        #self.test()
        self.folder = Path(r"C:Users\Joao\Downloads\balcon")
        self.speake("Hello World")
    def test(self):
        try:
            subprocess.check_output("dir {}", shell=True, stderr=subprocess.STDOUT)(format = self.folder)
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    def speake(self, text):
       cmd = {r"C:Users\Joao\Downloads\balcon.exe"}
       cmd.onecmd(cmd, "-l", "oi", shell=True )

if __name__ == "__main__":
    Terminal()