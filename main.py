import pyaudio
import speech_recognition as sr
import pyttsx3

# Set up the PyAudio object
audio = pyaudio.PyAudio()

# Open the microphone
print("open microphone")
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Record audio for 5 seconds
frames = []
print("record audio")
for i in range(0, int(44100 / 1024 * 5)):
    data = stream.read(1024)
    frames.append(data)

print("convert audio")
# Convert the audio frames to a SpeechRecognition AudioData object
audio_data = sr.AudioData(b''.join(frames), sample_rate=44100, sample_width=2)

print("speech recognition")
# Set up the SpeechRecognition recognizer object
recognizer = sr.Recognizer()

# Use the recognizer to transcribe the audio
text = recognizer.recognize_google(audio_data)
print(text)

# Set up the pyttsx3 engine object
engine = pyttsx3.init()

# Speak the transcription
engine.say(text)
engine.runAndWait()
