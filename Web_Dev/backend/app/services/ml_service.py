import os
import time

import joblib
import librosa
import numpy as np
from tensorflow.keras.models import load_model

# Silence TensorFlow logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from app.config import MODEL_PATH, ENCODER_PATH

# ------------------------------------------------------------------
# Load model once when the API starts
# ------------------------------------------------------------------

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

if not ENCODER_PATH.exists():
    raise FileNotFoundError(f"Encoder not found: {ENCODER_PATH}")

print("Loading CNN model...")
start = time.perf_counter()
MODEL = load_model(MODEL_PATH)
print(f"CNN model loaded in {time.perf_counter() - start:.2f}s")

print("Loading label encoder...")
start = time.perf_counter()
ENCODER = joblib.load(ENCODER_PATH)
print(f"Label encoder loaded in {time.perf_counter() - start:.2f}s")


# ------------------------------------------------------------------
# Audio preprocessing
# ------------------------------------------------------------------

def preprocess_audio(audio_path: str):

    start = time.perf_counter()
    print("Loading audio...")

    # Load only first 4 seconds
    audio, sr = librosa.load(
        audio_path,
        sr=22050,
        duration=4
    )

    print(f"Audio loaded in {time.perf_counter() - start:.2f}s")

    start = time.perf_counter()

    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_mels=128
    )

    mel_db = librosa.power_to_db(
        mel,
        ref=np.max
    )

    print(f"Mel spectrogram in {time.perf_counter() - start:.2f}s")

    # Resize to 128x128
    if mel_db.shape[1] < 128:
        pad = 128 - mel_db.shape[1]
        mel_db = np.pad(
            mel_db,
            ((0, 0), (0, pad))
        )
    else:
        mel_db = mel_db[:, :128]

    # Model expects (1,128,128,1)
    mel_db = np.expand_dims(
        mel_db,
        axis=(0, -1)
    ).astype(np.float32)

    print("Feature shape:", mel_db.shape)

    return mel_db


# ------------------------------------------------------------------
# Prediction
# ------------------------------------------------------------------

def predict_source(audio_path: str):

    total = time.perf_counter()

    print("========== ML START ==========")

    features = preprocess_audio(audio_path)

    print("Calling MODEL.predict()...")

    start = time.perf_counter()

    predictions = MODEL.predict(
        features,
        verbose=0
    )

    print(f"Prediction completed in {time.perf_counter() - start:.2f}s")

    predicted_index = int(np.argmax(predictions))
    confidence = float(np.max(predictions))

    label = ENCODER.inverse_transform(
        [predicted_index]
    )[0]

    label = label.strip().lower()

    mapping = {
        "traffic": "Traffic",
        "construction": "Construction",
        "entertainment": "Entertainment",
        "worship": "Worship",
        "ambience": "Ambience",
        "normal_ambience": "Ambience",
    }

    label = mapping.get(
        label,
        label.capitalize()
    )

    print(f"Total ML time: {time.perf_counter() - total:.2f}s")
    print("========== ML END ==========")

    return label, confidence