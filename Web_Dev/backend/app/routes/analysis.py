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

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        temp_path = tmp.name

    try:

        estimated_db = estimate_db(temp_path)

        ml_debug = predict_source(temp_path)

        source, confidence = predict_source(temp_path)

        return {
            "success": True,
            "estimated_db": estimated_db,
            "source": source,
            "confidence": round(confidence, 4),
            "venue_type": venue_type,
            "recording_time": recording_time
        }

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)