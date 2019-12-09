import pyaudio
import numpy as np

p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
f = 440        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
t = np.arange(fs*duration)*f/fs

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively)
samples = (volume*np.sin(2*np.pi*t)).astype(np.float32).tobytes()
stream.write(samples)
stream.stop_stream()
stream.close()

p.terminate()
