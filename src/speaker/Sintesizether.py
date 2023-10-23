import tkinter as tk
from tkinter import ttk
from pathlib import Path
import subprocess
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
import requests
from Functions_keyboard import Functions_keyboard as fk
class Sintesizether:
    def __init__(self, text_field, root):
        self.text_field = text_field
        self.fk = fk(text_field=self.text_field)
        self.voice = ""
        self.path = Path("/home/joao/Documents/falaai/cod/src/speaker/audio.wav")
        load_dotenv('.env')

        self.root = root

        # Crie uma variável para armazenar a voz selecionada no Combobox
        self.selected_voice = tk.StringVar()

        # Crie o Combobox para escolher a voz
        self.voice_choose = ttk.Combobox(self.root, textvariable=self.selected_voice, values=["Carregando..."], height=5)
        self.voice_choose.place(x=750, y=5)
        self.voice_choose.set("Selecione uma voz")
        self.voice_choose.config(width=10, height=5, background="white", foreground="black")

        # Crie um botão de atualização
        self.update_button = tk.Button(self.root, text="Atualizar Vozes", command=self.update_voices)
        self.update_button.place(x=580, y=5)

        # Verifique a conectividade com a internet
        self.is_connected = self.check_internet_connection()

        # Carregue as vozes disponíveis no Combobox
        self.load_voices()

    def update_voices(self):
        # Verifique a conectividade com a internet
        self.is_connected = self.check_internet_connection()

        # Atualize a lista de vozes
        self.load_voices()

    def check_internet_connection(self):
        try:
            response = requests.get("https://www.google.com", timeout=5)
            return response.status_code == 200
        except requests.ConnectionError:
            return False

    def list_voices(self):
        command = ['espeak-ng', '--voices']
        list_voice = subprocess.check_output(command, text=True)
        return list_voice.split('\n')[1:-1]

    def get_watson_voices(self):
        if self.is_connected:
            apikey = os.getenv("WATSON")
            authenticator = IAMAuthenticator(apikey)
            text_to_speech = TextToSpeechV1(authenticator=authenticator)
            text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/c10e6d85-723b-4b62-97f0-553e85561fb7')
            voices_watson = text_to_speech.list_voices().get_result()
            return voices_watson
        else:
            return None

    def load_voices(self):
        # Carregar vozes do eSpeak
        voices_espeak = self.list_voices()

        # Carregar vozes do Watson Text-to-Speech somente se houver conectividade com a internet
        if self.is_connected:
            voices_watson = self.get_watson_voices()
        else:
            voices_watson = None

        # Preencher o Combobox com as vozes disponíveis
        voice_options = ["Selecione uma voz"] + voices_espeak
        if voices_watson:
            voice_options += [f"IBM Watson: {voice['name']}" for voice in voices_watson['voices']]
        self.voice_choose['values'] = voice_options

    # Restante do código (métodos speak, change_voice, save_file, request_Watson, play, run,
    def speak(self):
        try:
            self.save_file()
            self.play()
        except:
            text = self.fk.get_text().strip()
            command = ['espeak-ng', '-w', self.path, text]
            subprocess.run(command, shell=False)
            self.play()

    def change_voice(self):
        subprocess.run(['espeak-ng', '-v', self.voice], shell=False)

    def save_file(self):
        response = self.request_Watson()
        with open(self.path, 'wb') as audio_file:
            audio_file.write(response)

    def request_Watson(self):
        text = str(self.fk.get_text())
        apikey = os.getenv("WATSON")
        authenticator = IAMAuthenticator(apikey)
        text_to_speech = TextToSpeechV1(authenticator=authenticator)
        text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/c10e6d85-723b-4b62-97f0-553e85561fb7')
        response = text_to_speech.synthesize(text, voice="pt-BR_IsabelaV3Voice", accept='audio/wav').get_result().content
        return response

    def play(self):
        command = ["aplay", str(self.path)]
        subprocess.call(command)

