import librosa
import numpy as np


def extract_mfcc(
    audio,
    sample_rate=22050,
    n_mfcc=40
):
    """
    Extract MFCC features.
    """

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sample_rate,
        n_mfcc=n_mfcc
    )

    mfcc_mean = np.mean(
        mfcc.T,
        axis=0
    )

    return mfcc_mean