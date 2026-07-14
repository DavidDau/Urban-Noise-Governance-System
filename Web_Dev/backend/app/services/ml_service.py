import os
import time

import joblib
import librosa
import numpy as np
from tensorflow.keras.models import load_model

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from app.config import MODEL_PATH, ENCODER_PATH


if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

if not ENCODER_PATH.exists():
    raise FileNotFoundError(f"Encoder not found: {ENCODER_PATH}")

print("Loading model...")
MODEL = load_model(MODEL_PATH)
print("Model loaded.")

print("Loading encoder...")
ENCODER = joblib.load(ENCODER_PATH)
print("Encoder loaded.")


def preprocess_audio(audio_path: str):

    audio, sr = librosa.load(
        audio_path,
        sr=22050,
        duration=4,
        mono=True
    )

    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_mels=128
    )

    mel_db = librosa.power_to_db(
        mel,
        ref=np.max
    )

    if mel_db.shape[1] < 128:
        mel_db = np.pad(
            mel_db,
            ((0, 0), (0, 128 - mel_db.shape[1]))
        )
    else:
        mel_db = mel_db[:, :128]

    mel_db = mel_db.astype(np.float32)

    mel_db = np.expand_dims(
        mel_db,
        axis=-1
    )

    mel_db = np.expand_dims(
        mel_db,
        axis=0
    )

    return mel_db


def predict_source(audio_path: str):

    features = preprocess_audio(audio_path)

    return {
        "shape": list(features.shape),
        "dtype": str(features.dtype),
        "minimum": float(np.min(features)),
        "maximum": float(np.max(features)),
        "mean": float(np.mean(features))
    }
