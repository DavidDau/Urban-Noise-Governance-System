import librosa
import numpy as np


def estimate_db(path: str):

    print("STEP 1 - loading audio")

    audio, sr = librosa.load(
        path,
        sr=None,
        mono=True,
        duration=10,
        backend="soundfile"
    )

    print("STEP 2 - audio loaded")

    rms = np.sqrt(np.mean(audio ** 2))

    print("STEP 3 - rms computed")

    db = 20 * np.log10(rms + 1e-10)

    print("STEP 4 - returning")

    return round(float(db + 100), 2)


def get_time_period(recording_time: str):

    hour = int(recording_time.split(":")[0])

    if 6 <= hour < 21:
        return "Day"

    return "Night"