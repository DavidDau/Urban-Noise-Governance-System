import librosa
import numpy as np


def normalize_audio(audio):
    """
    Normalize audio between -1 and 1.
    """

    max_value = np.max(np.abs(audio))

    if max_value == 0:
        return audio

    return audio / max_value


def remove_silence(audio, top_db=20):
    """
    Remove silent sections.
    """

    intervals = librosa.effects.split(
        audio,
        top_db=top_db
    )

    non_silent_audio = []

    for start, end in intervals:
        non_silent_audio.extend(audio[start:end])

    return np.array(non_silent_audio)