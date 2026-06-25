from pathlib import Path
import os

import numpy as np
import librosa
import joblib

from tensorflow.keras.models import load_model

# Silence TensorFlow logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "ml_models"

MODEL_PATH = MODEL_DIR / "urban_noise_cnn.keras"
ENCODER_PATH = MODEL_DIR / "label_encoder.pkl"

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

if not ENCODER_PATH.exists():
    raise FileNotFoundError(f"Encoder not found: {ENCODER_PATH}")

MODEL = load_model(MODEL_PATH)
ENCODER = joblib.load(ENCODER_PATH)


def preprocess_audio(path: str):
    audio, sr = librosa.load(path, sr=22050)

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
        pad = 128 - mel_db.shape[1]
        mel_db = np.pad(
            mel_db,
            ((0, 0), (0, pad))
        )
    else:
        mel_db = mel_db[:, :128]

    mel_db = np.expand_dims(
        mel_db,
        axis=(0, -1)
    )

    return mel_db


def predict_source(audio_path: str):
    features = preprocess_audio(audio_path)

    predictions = MODEL.predict(
        features,
        verbose=0
    )

    predicted_index = int(
        np.argmax(predictions)
    )

    confidence = float(
        np.max(predictions)
    )

    label = ENCODER.inverse_transform(
        [predicted_index]
    )[0]

    return label, confidence