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
        self.text = self.fk.get_text().strip()
        self.voice = ""
        
    def speak(self):
        if os.path.isfile(f'{self.text}.wav',):
            self.play
        else:
            subprocess.run(command, shell=False)
            command = ['aplay', f'./{self.text}.wav']
            subprocess.run(command, shell=False)
            self.play()

    def change_voice(self):
        subprocess.run(['espeak-ng', '-v', self.voice], shell=False)

    def list_voices(self):
        command = ['espeak-ng', '--voices']
        list_voice = subprocess.check_output(command)
        return list_voice

    def request_Watson(self):
        authenticator = IAMAuthenticator(apikey='YOUR_API_KEY')  # Replace with your API key
        self.text_to_speech = TextToSpeechV1(
            authenticator=authenticator,
            version='2019-07-12',  # Adjust the version as needed
        )
        text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/c10e6d85-723b-4b62-97f0-553e85561fb7')
 def save_file(self):
    reponse = send_requese()
     with open(f'{self.text}.wav', 'wb') as audio_file:
        audio_file.write(response.content)
        
 def send_request(self):
         return  self.text_to_speech.synthesize(self.text, voice=self.voice, accept='audio/wav').get_result()
         
    def play(self):
           subprocess.run(command, shell=False)
        command = ['aplay', f'./{self.text}.wav']
        subprocess.run(command, shell=False)
  def control(self):      
        try:
            self.request_Watson()
            self.save_file()
        finally:
            self.speak()
            
      
 
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            