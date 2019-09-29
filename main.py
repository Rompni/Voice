from Recognition import initRecognition
from Synthesizer import tts, media

enabled = initRecognition()

if enabled:
    tts("sample.txt", "ES", "sample.wav")
    media("sample.wav")
