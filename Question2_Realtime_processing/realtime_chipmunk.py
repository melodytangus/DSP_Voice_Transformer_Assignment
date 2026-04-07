import sounddevice as sd
import numpy as np
from scipy import signal

fs = 16000
speed_factor = 1.5  # higher pitch

def callback(indata, outdata, frames, time, status):
    # get microphone data
    x = indata[:, 0]
    
    # resampling it to a smaller number of samples
    short_chunk = signal.resample(x, int(frames / speed_factor))
    
    y = np.resize(short_chunk, frames)
    
    outdata[:, 0] = y

print("Chipmunk Voice Active.Speak")
print("Press Enter to stop")

with sd.Stream(channels=1, samplerate=fs, callback=callback):
    input()