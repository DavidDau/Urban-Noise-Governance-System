import os
import tempfile

from fastapi import APIRouter, UploadFile, File, Form

router = APIRouter()


@router.post("/predict")
async def analyze_audio(
    file: UploadFile = File(...),
    venue_type: str = Form(...),
    recording_time: str = Form(...)
):

    temp_path = None

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as tmp:

            tmp.write(await file.read())
            temp_path = tmp.name

        print("TEMP FILE:", temp_path)

        return {
            "saved": True,
            "filename": file.filename,
            "venue": venue_type,
            "time": recording_time
        }

    finally:

        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)