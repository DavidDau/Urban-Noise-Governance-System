from fastapi import APIRouter, UploadFile, File, Form

router = APIRouter()

@router.post("/predict")
async def analyze_audio(
    file: UploadFile = File(...),
    venue_type: str = Form(...),
    recording_time: str = Form(...)
):
    return {
        "success": True
    }