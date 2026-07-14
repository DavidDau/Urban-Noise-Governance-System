import tempfile
import os

from fastapi import APIRouter, UploadFile, File, Form
from app.services.noise_service import estimate_db

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
        db = estimate_db(path)

    os.remove(path)

    return {
        "estimated_db": db
    }