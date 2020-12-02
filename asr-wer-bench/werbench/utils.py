# Copyright (c) 2020 Slang Labs Private Limited. All rights reserved.

import numpy as np
from scipy import signal
import wave


def read_wav(audio_file_path):
    w = wave.open(audio_file_path, 'r')
    rate = w.getframerate()
    frames = w.getnframes()
    buffer = w.readframes(frames)
    return buffer, rate

def bytes2int16(buffer, input_rate, desired_rate):
    data16 = np.frombuffer(buffer, dtype=np.int16)

    if input_rate != desired_rate:
        resample_size = int(len(data16) / input_rate * desired_rate)
        resample = signal.resample(data16, resample_size)
        data16 = np.array(resample, dtype=np.int16)

    return data16
