import sys
from pathlib import Path
import os
import tempfile

import joblib
import librosa
import numpy as np

from enum import Enum

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model

# =====================================================
# Project Root
# =====================================================

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

# =====================================================
# Noise Analysis Imports
# =====================================================

from noise_analysis.loudness import estimate_db
from noise_analysis.compliance import check_compliance
from noise_analysis.recommendations import get_recommendation
from noise_analysis.time_utils import get_time_period

# =====================================================
# Venue Enum (IMPORTANT: keep values simple for frontend)
# =====================================================

class VenueType(str, Enum):
    residential = "Residential Zone"
    commercial = "Commercial Zone"
    industrial = "Industrial Zone"
    quiet = "Quiet Zone"
    special_quiet = "Special Quiet Zone"
    soundproof = "Soundproof Venue"
    non_soundproof = "Non-Soundproof Venue"

# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(
    title="Urban Noise Governance API",
    description="Acoustic classification + compliance + recommendations",
    version="2.0"
)

# =====================================================
# CORS (MUST be declared immediately after app creation)
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # better than "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# Paths
# =====================================================

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

MODEL_PATH = MODEL_DIR / "urban_noise_cnn.keras"
ENCODER_PATH = MODEL_DIR / "label_encoder.pkl"

# =====================================================
# Load Model + Encoder
# =====================================================

try:
    model = load_model(str(MODEL_PATH))
    label_encoder = joblib.load(str(ENCODER_PATH))
    print("Model loaded successfully.")

except Exception as e:
    print(f"Error loading model: {e}")
    raise e

# =====================================================
# Audio Preprocessing
# =====================================================

def preprocess_audio(audio_path):
    signal, sample_rate = librosa.load(audio_path, sr=22050)

    mel_spec = librosa.feature.melspectrogram(
        y=signal,
        sr=sample_rate,
        n_mels=128
    )

    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

    # pad / trim
    if mel_spec_db.shape[1] < 128:
        pad = 128 - mel_spec_db.shape[1]
        mel_spec_db = np.pad(mel_spec_db, ((0, 0), (0, pad)), mode="constant")
    else:
        mel_spec_db = mel_spec_db[:, :128]

    mel_spec_db = np.expand_dims(mel_spec_db, axis=-1)
    mel_spec_db = np.expand_dims(mel_spec_db, axis=0)

    return mel_spec_db

# =====================================================
# Health Check
# =====================================================

@app.get("/")
def home():
    return {"message": "Urban Noise Governance API is running."}

# =====================================================
# Prediction Endpoint
# =====================================================

@app.post("/predict")
async def predict_audio(
    file: UploadFile = File(...),
    venue_type: VenueType = Form(...),
    recording_time: str = Form(...)
):

    if not file.filename.lower().endswith(".wav"):
        raise HTTPException(
            status_code=400,
            detail="Only WAV files are supported."
        )

    temp_path = None

    try:
        # Save temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(await file.read())
            temp_path = tmp.name

        # ---------------- CNN ----------------
        features = preprocess_audio(temp_path)
        predictions = model.predict(features)

        predicted_index = int(np.argmax(predictions))
        confidence = float(np.max(predictions))

        predicted_label = label_encoder.inverse_transform([predicted_index])[0]

        # ---------------- Noise Analysis ----------------
        estimated_db = estimate_db(temp_path)
        time_period = get_time_period(recording_time)

        compliance = check_compliance(
            estimated_db,
            venue_type.value,   # IMPORTANT FIX
            time_period
        )

        recommendation = get_recommendation(
            predicted_label,
            compliance["status"]
        )

        # ---------------- Response ----------------
        return {
            "source": predicted_label,
            "confidence": round(confidence, 4),
            "estimated_db": estimated_db,
            "venue_type": venue_type.value,
            "recording_time": recording_time,
            "time_period": time_period,
            "legal_limit": compliance["legal_limit"],
            "status": compliance["status"],
            "exceedance": compliance["exceedance"],
            "recommendation": recommendation
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)