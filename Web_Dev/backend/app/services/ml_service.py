import os
import time
from pathlib import Path

import joblib
import librosa
import numpy as np
from tensorflow.keras.models import load_model

# Silence TensorFlow logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from app.config import MODEL_PATH, ENCODER_PATH

# ------------------------------------------------------------------
# Validate model files
# ------------------------------------------------------------------

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

if not ENCODER_PATH.exists():
    raise FileNotFoundError(f"Encoder not found: {ENCODER_PATH}")

print("Loading CNN model...")
load_start = time.perf_counter()
MODEL = load_model(MODEL_PATH)
print(f"CNN model loaded in {time.perf_counter() - load_start:.2f}s")

print("Loading label encoder...")
encoder_start = time.perf_counter()
ENCODER = joblib.load(ENCODER_PATH)
print(f"Label encoder loaded in {time.perf_counter() - encoder_start:.2f}s")


# ------------------------------------------------------------------
# Audio preprocessing
# ------------------------------------------------------------------

def preprocess_audio(path: str):

    start = time.perf_counter()

    # Load only the first 4 seconds to speed up inference
    audio, sr = librosa.load(
        path,
        sr=22050,
        duration=4
    )

    print(f"      Audio loaded: {time.perf_counter() - start:.2f}s")

    mel_start = time.perf_counter()

    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_mels=128
    )

    mel_db = librosa.power_to_db(
        mel,
        ref=np.max
    )

    print(f"      Mel spectrogram: {time.perf_counter() - mel_start:.2f}s")

    resize_start = time.perf_counter()

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

    print(f"      Resize/expand: {time.perf_counter() - resize_start:.2f}s")
    print(f"      Total preprocessing: {time.perf_counter() - start:.2f}s")

    return mel_db


# ------------------------------------------------------------------
# Prediction
# ------------------------------------------------------------------

def predict_source(audio_path: str):

    total_start = time.perf_counter()

    features = preprocess_audio(audio_path)

    predict_start = time.perf_counter()

    predictions = MODEL.predict(
        features,
        verbose=0
    )

    print(f"      MODEL.predict(): {time.perf_counter() - predict_start:.2f}s")

    decode_start = time.perf_counter()

    predicted_index = int(np.argmax(predictions))
    confidence = float(np.max(predictions))

    label = ENCODER.inverse_transform(
        [predicted_index]
    )[0]

    label_normalized = label.strip().lower()

    capitalization_map = {
        "traffic": "Traffic",
        "construction": "Construction",
        "entertainment": "Entertainment",
        "worship": "Worship",
        "ambience": "Ambience",
        "normal_ambience": "Ambience"
    }

    label = capitalization_map.get(
        label_normalized,
        label.capitalize()
    )

    print(f"      Label decoding: {time.perf_counter() - decode_start:.2f}s")
    print(f"      Total ML prediction: {time.perf_counter() - total_start:.2f}s")

    return label, confidence