import librosa
from pathlib import Path


def load_audio(file_path, sample_rate=22050):
    """
    Load an audio file.

    Args:
        file_path (str | Path): Path to audio file.
        sample_rate (int): Target sample rate.

    Returns:
        tuple:
            audio (numpy.ndarray)
            sample_rate (int)
    """

    audio, sr = librosa.load(
        file_path,
        sr=sample_rate,
        mono=True
    )

    return audio, sr