import os
import time
from pathlib import Path

# ------------------------------------------------------------------
# TensorFlow startup settings
# ------------------------------------------------------------------

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_XLA_FLAGS"] = "--tf_xla_auto_jit=0"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import joblib
import librosa
import numpy as np
from tensorflow.keras.models import load_model

from app.config import MODEL_PATH, ENCODER_PATH

# ------------------------------------------------------------------
# Validate paths
# ------------------------------------------------------------------

MODEL_PATH = Path(MODEL_PATH).resolve()
ENCODER_PATH = Path(ENCODER_PATH).resolve()

print(f"Model path   : {MODEL_PATH}")
print(f"Encoder path : {ENCODER_PATH}")

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model file not found:\n{MODEL_PATH}"
    )

if not ENCODER_PATH.exists():
    raise FileNotFoundError(
        f"Label encoder not found:\n{ENCODER_PATH}"
    )

# ------------------------------------------------------------------
# Load model
# ------------------------------------------------------------------

print("Loading model...")

MODEL = load_model(
    MODEL_PATH,
    compile=False
)

print("✓ Model loaded successfully.")

# ------------------------------------------------------------------
# Load encoder
# ------------------------------------------------------------------

print("Loading label encoder...")

ENCODER = joblib.load(ENCODER_PATH)

print("✓ Label encoder loaded successfully.")

# ------------------------------------------------------------------
# Warm up model
# ------------------------------------------------------------------

print("Warming up model...")

dummy_input = np.zeros((1, 128, 128, 1), dtype=np.float32)

MODEL.predict(dummy_input, verbose=0)

print("✓ Warm-up complete.")

# ------------------------------------------------------------------
# Audio preprocessing
# ------------------------------------------------------------------

SAMPLE_RATE = 22050
DURATION = 4
N_MELS = 128
TARGET_WIDTH = 128


def preprocess_audio(audio_path: str) -> np.ndarray:
    """
    Convert an audio file into a Mel spectrogram suitable
    for CNN inference.
    """

    audio, sr = librosa.load(
        audio_path,
        sr=SAMPLE_RATE,
        duration=DURATION,
        mono=True
    )

    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_mels=N_MELS
    )

    mel = librosa.power_to_db(
        mel,
        ref=np.max
    )

    if mel.shape[1] < TARGET_WIDTH:
        mel = np.pad(
            mel,
            ((0, 0), (0, TARGET_WIDTH - mel.shape[1])),
            mode="constant"
        )
    else:
        mel = mel[:, :TARGET_WIDTH]

    mel = mel.astype(np.float32)
    mel = np.expand_dims(mel, axis=-1)
    mel = np.expand_dims(mel, axis=0)

    return mel


# ------------------------------------------------------------------
# Prediction
# ------------------------------------------------------------------

LABEL_MAPPING = {
    "traffic": "Traffic",
    "construction": "Construction",
    "entertainment": "Entertainment",
    "worship": "Worship",
    "ambience": "Ambience",
    "normal_ambience": "Ambience",
}


def predict_source(audio_path: str):
    """
    Predict the dominant noise source from an audio recording.

    Returns:
        tuple[str, float]
            (predicted_label, confidence)
    """

    start_time = time.perf_counter()

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

    label = LABEL_MAPPING.get(
        label.strip().lower(),
        label.strip().capitalize()
    )

    elapsed = time.perf_counter() - start_time

    print(
        f"Prediction: {label} "
        f"(confidence={confidence:.4f}) "
        f"in {elapsed:.2f}s"
    )

    return label, confidence
