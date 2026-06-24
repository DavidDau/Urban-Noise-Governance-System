from pathlib import Path
import numpy as np
import librosa
import joblib
from tensorflow.keras.models import load_model

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "ml_models"

MODEL = load_model(MODEL_DIR / "urban_noise_cnn.keras")
ENCODER = joblib.load(MODEL_DIR / "label_encoder.pkl")


def preprocess_audio(path: str):
    audio, sr = librosa.load(path, sr=22050)

    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_mels=128
    )

    mel_db = librosa.power_to_db(mel, ref=np.max)

    if mel_db.shape[1] < 128:
        pad = 128 - mel_db.shape[1]
        mel_db = np.pad(mel_db, ((0, 0), (0, pad)))
    else:
        mel_db = mel_db[:, :128]

    mel_db = np.expand_dims(mel_db, axis=(0, -1))
    return mel_db


def predict_source(audio_path: str):
    features = preprocess_audio(audio_path)

    preds = MODEL.predict(features)

    idx = int(np.argmax(preds))
    confidence = float(np.max(preds))

    label = ENCODER.inverse_transform([idx])[0]

    return label, confidence