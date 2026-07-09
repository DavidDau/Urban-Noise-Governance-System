import os
import tempfile

from fastapi import APIRouter, UploadFile, File, Form

from app.services.noise_service import estimate_db

router = APIRouter()


@router.post("/predict")
async def analyze_audio(
    file: UploadFile = File(...),
    venue_type: str = Form(...),
    recording_time: str = Form(...)
):
    temp_path = None

    try:
        # Save uploaded file
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as tmp:

            tmp.write(await file.read())
            temp_path = tmp.name

        print("===================================")
        print("STEP 1: File uploaded successfully")
        print("Temp file:", temp_path)

        # Test librosa/audio processing only
        estimated_db = estimate_db(temp_path)

        print("STEP 2: estimate_db() completed")
        print("Estimated dB:", estimated_db)

        return {
            "success": True,
            "filename": file.filename,
            "venue": venue_type,
            "recording_time": recording_time,
            "estimated_db": estimated_db
        }

    except Exception as e:
        print("===================================")
        print("ERROR INSIDE analysis.py")
        print(type(e).__name__)
        print(str(e))
        raise

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)