from vosk import Model, KaldiRecognizer
import pyaudio
import wave
import os
import json

model_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "vosk-model-small-cn-0.22")
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        text = result.get("text","")
        print(text)