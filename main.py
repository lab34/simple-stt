import pyaudio
import speech_recognition as sr
import wave
from pydub import AudioSegment
import pyttsx3

p = pyaudio.PyAudio()

chunk = 1024
sample_format = pyaudio.paInt16
channels = 1
fs = 44100
seconds = 5

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []

print("reading")
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

wave_file = wave.open("audio.wav", "wb")
wave_file.setnchannels(channels)
wave_file.setsampwidth(p.get_sample_size(sample_format))
wave_file.setframerate(fs)
wave_file.writeframes(b''.join(frames))
wave_file.close()

r = sr.Recognizer()
print("exporting")
with sr.AudioFile('audio.wav') as source:
    audio = r.record(source)

print("recognizing")
text = r.recognize_google(audio)

print(text)

# Set up the pyttsx3 engine object
engine = pyttsx3.init()

# Speak the transcription
engine.say(text)
engine.runAndWait()
