import tempfile
import os

from fastapi import APIRouter, UploadFile, File, Form

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

    os.remove(path)

    return {
        "saved": True
    }