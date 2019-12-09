
import numpy as np


def gen_samples(f, duration, fs=44100):
    """
    Function that generates sinusional samples at a frequency f, with a sampling frequency of fs for duration in seconds

    Parameters
    f (float): Frequency to generate
    duration (float): Time in seconds
    fs (float): Sampling frequency - defaults ot 441000 Hz
    """

    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

    return samples
