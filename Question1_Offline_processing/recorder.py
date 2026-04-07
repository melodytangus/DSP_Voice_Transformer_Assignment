import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000
duration = 5  # seconds

print("Speak")

recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait() 

write('mercy_voice.wav', fs, recording)
print("Saved 'mercy_voice.wav'")