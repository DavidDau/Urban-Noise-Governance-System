import librosa
import numpy as np


def estimate_db(audio_path):
    """
    Estimate loudness from audio signal.
    Returns estimated dBA.
    """

    audio, sr = librosa.load(audio_path, sr=None)

    rms = np.sqrt(np.mean(audio ** 2))

    estimated_db = 20 * np.log10(rms + 1e-10)

    estimated_db += 100

    return round(float(estimated_db), 2)
