from pathlib import Path
import shlex
import subprocess
from Functions_keyboard import Functions_keyboard as fk
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
import os

class Terminal:

    def __init__(self, text_field):
        self.text_field = text_field
        self.fk = fk(text_field=self.text_field)
        
        self.voice = ""
        self.path = Path("/home/joao/Documents/falaai/cod/src/speaker/audio.wav")
        load_dotenv('.env')

    def speak(self):
        if os.path.isfile(self.path):
            self.play()
        else:
            text = self.fk.get_text().strip()
            command = ['espeak-ng', '-w', self.path, text]
            subprocess.run(command, shell=False)
            self.play()

    def change_voice(self):
        subprocess.run(['espeak-ng', '-v', self.voice], shell=False)

    def list_voices(self):
        command = ['espeak-ng', '--voices']
        list_voice = subprocess.check_output(command)
        return list_voice
        
    def request_Watson(self):
        text = str(self.fk.get_text())
        apikey = os.getenv("WATSON")  
        authenticator = IAMAuthenticator(apikey)
        text_to_speech = TextToSpeechV1( authenticator=authenticator )
        text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/c10e6d85-723b-4b62-97f0-553e85561fb7')
        response = text_to_speech.synthesize(text, voice="pt-BR_IsabelaV3Voice", accept='audio/wav').get_result().content
        return response

    def save_file(self):
        response = self.request_Watson()
        with open(self.path, 'wb') as audio_file:
            audio_file.write(response)
       
    def play(self):
        command = ['aplay', str(self.path)]  # Converta o caminho para uma string
        subprocess.call(command)

    def control(self):
        try:
            self.save_file()
        except Exception as e:
            print(e)
            self.speak()












