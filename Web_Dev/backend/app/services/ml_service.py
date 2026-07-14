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

    print("STEP 1")
    print("Input shape:", features.shape)

    print("STEP 2")
    output = MODEL(features, training=False)

    print("STEP 3")

    predictions = output.numpy()

    print("STEP 4")

    predicted_index = int(np.argmax(predictions))
    confidence = float(np.max(predictions))

    label = ENCODER.inverse_transform([predicted_index])[0]

    return label, confidence