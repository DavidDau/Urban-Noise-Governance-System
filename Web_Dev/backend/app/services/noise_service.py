import numpy as np
import librosa

def estimate_db(path: str):
    print("estimate_db() called")
    return 75.0


def get_time_period(recording_time: str):
    hour = int(recording_time.split(":")[0])

    if 6 <= hour < 21:
        return "Day"

    return "Night"