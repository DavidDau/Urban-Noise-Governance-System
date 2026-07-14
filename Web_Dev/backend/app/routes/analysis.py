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
        path = tmp.name

    try:
        estimated_db = estimate_db(path)

        source, confidence = predict_source(path)

        return {
            "estimated_db": estimated_db,
            "source": source,
            "confidence": confidence
        }

    finally:
        if os.path.exists(path):
            os.remove(path)