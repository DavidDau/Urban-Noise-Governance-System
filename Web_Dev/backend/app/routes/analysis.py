import os
import tempfile
import traceback

from fastapi import APIRouter, UploadFile, File, Form

from app.services.ml_service import predict_source

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

        print("STEP 1 - File saved")

        source, confidence = predict_source(temp_path)

        print("STEP 2 - Prediction completed")

        return {
            "success": True,
            "source": source,
            "confidence": confidence
        }

    except Exception as e:
        print("===================================")
        print(type(e).__name__)
        print(e)
        print(traceback.format_exc())
        raise

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)