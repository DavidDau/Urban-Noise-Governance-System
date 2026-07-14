import os
import time

# Disable TensorFlow optimizations that cause long startup compilation
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_XLA_FLAGS"] = "--tf_xla_auto_jit=0"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import joblib
import librosa
import numpy as np
from tensorflow.keras.models import load_model

from app.config import MODEL_PATH, ENCODER_PATH

# ------------------------------------------------------------------
# Load model
# ------------------------------------------------------------------

print("Loading model...")

MODEL = load_model(
    MODEL_PATH,
    compile=False
)

print("Model loaded.")

print("Loading encoder...")

ENCODER = joblib.load(ENCODER_PATH)

print("Encoder loaded.")

# ------------------------------------------------------------------
# Warm up the model
# ------------------------------------------------------------------

print("Warming up model...")

dummy = np.zeros((1, 128, 128, 1), dtype=np.float32)

MODEL.predict(dummy, verbose=0)

print("Warmup complete.")

# ------------------------------------------------------------------
# Audio preprocessing
# ------------------------------------------------------------------

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

    mel = librosa.power_to_db(
        mel,
        ref=np.max
    )

    if mel.shape[1] < 128:

        mel = np.pad(
            mel,
            ((0, 0), (0, 128 - mel.shape[1]))
        )

    else:

        mel = mel[:, :128]

    mel = mel.astype(np.float32)

    mel = np.expand_dims(mel, axis=-1)

    mel = np.expand_dims(mel, axis=0)

    return mel

# ------------------------------------------------------------------
# Prediction
# ------------------------------------------------------------------

def predict_source(audio_path: str):

    start = time.perf_counter()

    features = preprocess_audio(audio_path)

    predictions = MODEL.predict(
        features,
        verbose=0
    )

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
        "normal_ambience": "Ambience"
    }

    label = mapping.get(
        label,
        label.capitalize()
    )

    print(f"Inference completed in {time.perf_counter() - start:.2f}s")

    return label, confidence