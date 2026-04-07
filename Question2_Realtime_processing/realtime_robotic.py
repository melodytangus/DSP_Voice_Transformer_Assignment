import sounddevice as sd
import numpy as np

fs = 16000
phase = 0

def callback(indata, outdata, frames, time, status):
    global phase
    
    # Generate continuous 400Hz sine wave (Robot effect)
    t = (phase + np.arange(frames)) / fs
    carrier = np.cos(2 * np.pi * 400 * t).reshape(-1, 1)
    
    # Apply modulation and send directly to speakers
    outdata[:] = indata * carrier
    phase += frames

print("Real-time Robot Voice Active.You can speak")
print("Press Enter in the terminal to stop.")

# Run the continuous stream
with sd.Stream(channels=1, samplerate=fs, callback=callback):
    input()
    