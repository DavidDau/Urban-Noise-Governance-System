import os
import tempfile
from fastapi import APIRouter, UploadFile, File, Form

from app.services.ml_service import predict_source
from app.schemas.venue import VenueType
from app.services.severity_service import get_severity
from app.services.noise_service import estimate_db, get_time_period
from app.services.compliance_service import (
    check_compliance,
    get_recommendation
)

router = APIRouter()


@router.post("/predict")
async def analyze_audio(
    file: UploadFile = File(...),
    venue_type: VenueType = Form(...),
    recording_time: str = Form(...)
):

    temp_path = None

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        temp_path = tmp.name

    # ML prediction
    source, confidence = predict_source(temp_path)

    # noise analysis
    db = estimate_db(temp_path)
    severity = get_severity(db)
    period = get_time_period(recording_time)

    compliance = check_compliance(db, venue_type.value, period)
    recommendation = get_recommendation(source, compliance["status"])

    return {
        "source": source,
        "confidence": round(confidence, 4),
        "estimated_db": db,
        "venue_type": venue_type.value,
        "severity": severity,
        "time_period": period,
        "legal_limit": compliance["legal_limit"],
        "status": compliance["status"],
        "exceedance": compliance["exceedance"],
        "recommendation": recommendation
    }