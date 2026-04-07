# DSP Voice Transformer

A Python project applying Digital Signal Processing (DSP) to modify recorded and live audio.

## Project Structure

**1. `Question1_Offline_processing/`**
* **`recorder.py`**: Captures a 5-second voice sample.
* **`mercy_voice.wav`**: My original audio recording.
* **`VoiceTransformer.ipynb`**: Applies Pitch Shift, Echo, and Robot Voice effects offline.

**2. `Question2_Realtime_processing/`**
* **`realtime_robotic.py`**: applies a 400Hz robot voice effect to live microphone input in real-time.
* **`realtime_vader.py` (Darth Vader):** Uses a very low-frequency (50Hz) carrier wave to create a deep, rumbling tremolo effect, along with a slight volume boost for an intimidating voice.
* **`realtime_chipmunk.py` (Chipmunk):** Uses `scipy.signal.resample` to speed up the pitch. Because real-time pitch shifting is mathematically difficult with strict hardware chunk sizes, you will hear a bit of digital "stuttering" as the script repeats data to keep the stream from crashing, but it successfully demonstrates the DSP concept!
---
