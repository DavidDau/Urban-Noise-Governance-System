from fastapi import FastAPI, File, UploadFile, HTTPException
from tensorflow.keras.models import load_model
import numpy as np
import librosa
import joblib
import tempfile
import os

# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(
    title="Urban Acoustic Event Classification API",
    description="CNN-based API for classifying urban environmental sounds.",
    version="1.0"
)

# =====================================================
# Paths (FIXED: absolute paths based on file location)
# =====================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

MODEL_PATH = os.path.join(MODEL_DIR, "urban_noise_cnn.keras")
ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.pkl")

# =====================================================
# Load Model + Label Encoder
# =====================================================

try:
    model = load_model(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)

    print("Model and label encoder loaded successfully.")

except Exception as e:
    print(f"Error loading model files: {e}")
    raise e


# =====================================================
# Audio Preprocessing
# =====================================================

def preprocess_audio(audio_path):
    """
    Convert audio file into a 128x128 Mel Spectrogram.
    """

    signal, sample_rate = librosa.load(audio_path, sr=22050)

    mel_spec = librosa.feature.melspectrogram(
        y=signal,
        sr=sample_rate,
        n_mels=128
    )

    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

    # Pad or trim to 128 time frames
    if mel_spec_db.shape[1] < 128:
        padding = 128 - mel_spec_db.shape[1]
        mel_spec_db = np.pad(
            mel_spec_db,
            pad_width=((0, 0), (0, padding)),
            mode="constant"
        )
    else:
        mel_spec_db = mel_spec_db[:, :128]

    # Add channel + batch dimensions
    mel_spec_db = np.expand_dims(mel_spec_db, axis=-1)
    mel_spec_db = np.expand_dims(mel_spec_db, axis=0)

    return mel_spec_db


# =====================================================
# Health Check
# =====================================================

@app.get("/")
def home():
    return {"message": "Urban Noise Classification API is running."}


# =====================================================
# Prediction Endpoint
# =====================================================

@app.post("/predict")
async def predict_audio(file: UploadFile = File(...)):

    if not file.filename.endswith(".wav"):
        raise HTTPException(
            status_code=400,
            detail="Only WAV audio files are supported."
        )

    temp_path = None

    try:
        # Save temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(await file.read())
            temp_path = temp_file.name

        # Preprocess
        features = preprocess_audio(temp_path)

        # Predict
        predictions = model.predict(features)

        predicted_index = int(np.argmax(predictions))
        confidence = float(np.max(predictions) * 100)

        # Decode label
        predicted_label = label_encoder.inverse_transform([predicted_index])[0]

        return {
            "prediction": predicted_label,
            "confidence": round(confidence, 2)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)