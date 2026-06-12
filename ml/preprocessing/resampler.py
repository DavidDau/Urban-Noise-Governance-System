import librosa
import numpy as np


TARGET_DURATION = 4
TARGET_SR = 22050


def standardize_length(audio):
    """
    Force all audio clips to 4 seconds.
    """

    target_length = TARGET_DURATION * TARGET_SR

    if len(audio) > target_length:
        audio = audio[:target_length]

    elif len(audio) < target_length:
        padding = target_length - len(audio)

        audio = np.pad(
            audio,
            (0, padding),
            mode="constant"
        )

    return audio