import numpy as np
import librosa


def estimate_db(path: str):
    audio, sr = librosa.load(path, sr=None)

    rms = np.sqrt(np.mean(audio ** 2))

    db = 20 * np.log10(rms + 1e-10)

    # calibration offset (MVP approximation)
    return round(float(db + 100), 2)


def get_time_period(recording_time: str):
    hour = int(recording_time.split(":")[0])

    if 6 <= hour < 21:
        return "Day"
    return "Night"