import librosa
import numpy as np


def generate_mel_spectrogram(
    audio,
    sample_rate=22050
):
    """
    Generate Mel Spectrogram.
    """

    spectrogram = librosa.feature.melspectrogram(
        y=audio,
        sr=sample_rate
    )

    spectrogram_db = librosa.power_to_db(
        spectrogram,
        ref=np.max
    )

    return spectrogram_db