import sounddevice as sd
import numpy as np

fs = 16000
phase = 0

def callback(indata, outdata, frames, time, status):
    global phase
    
    # Generate a very low-frequency 50Hz rumble
    t = (phase + np.arange(frames)) / fs
    carrier = np.cos(2 * np.pi * 50 * t).reshape(-1, 1)
    
    # Apply modulation and boost the volume by 1.5x
    vader_voice = indata * carrier * 1.5
    
    outdata[:] = vader_voice
    phase += frames

print("Darth Vader Voice Active.Speak")
print("Press Enter to stop.")

with sd.Stream(channels=1, samplerate=fs, callback=callback):
    input()