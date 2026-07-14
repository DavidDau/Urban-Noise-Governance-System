import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from tensorflow.keras.models import load_model
import joblib

from app.config import MODEL_PATH, ENCODER_PATH

print("Loading model...")
MODEL = load_model(MODEL_PATH)
print("Model loaded.")

print("Loading encoder...")
ENCODER = joblib.load(ENCODER_PATH)
print("Encoder loaded.")


def predict_source(audio_path: str):
    return "Traffic", 0.99