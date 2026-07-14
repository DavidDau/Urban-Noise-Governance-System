import os
import tempfile

from fastapi import APIRouter, UploadFile, File, Form

from app.services.noise_service import estimate_db
from app.services.ml_service import predict_source

router = APIRouter()


@router.post("/predict")
async def analyze_audio(
    file: UploadFile = File(...),
    venue_type: str = Form(...),
    recording_time: str = Form(...)
):

    # Save uploaded audio temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        temp_path = tmp.name

    try:

        # Estimate noise level
        estimated_db = estimate_db(temp_path)

        # Predict sound source using CNN
        source, confidence = predict_source(temp_path)

        # Return prediction
        return {
            "success": True,
            "source": source,
            "confidence": round(confidence, 4),
            "estimated_db": round(estimated_db, 2),
            "venue_type": venue_type,
            "recording_time": recording_time
        }

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)