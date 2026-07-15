import os
import tempfile

from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.report import AnalysisReport

from app.services.noise_service import (
    estimate_db,
    get_time_period,
)

from app.services.ml_service import predict_source

from app.services.compliance_service import (
    check_compliance,
    get_recommendation,
)

from app.services.severity_service import get_severity
from app.services.risk_service import calculate_risk_score

router = APIRouter()


@router.post("/predict")
async def analyze_audio(
    file: UploadFile = File(...),
    venue_type: str = Form(...),
    recording_time: str = Form(...),
    db: Session = Depends(get_db)
):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        temp_path = tmp.name

    try:

        # ML prediction
        estimated_db = estimate_db(temp_path)
        source, confidence = predict_source(temp_path)

        # Time period
        time_period = get_time_period(recording_time)

        # Compliance
        compliance = check_compliance(
            estimated_db,
            venue_type,
            time_period
        )

        # Severity
        severity = get_severity(estimated_db)

        # Risk
        risk = calculate_risk_score(
            severity,
            compliance["status"]
        )

        # Recommendation
        recommendation = get_recommendation(
            source,
            compliance["status"]
        )

        # Save analysis to database
        report = AnalysisReport(
            user_id=None,

            source=source,
            confidence=round(confidence, 4),

            estimated_db=round(estimated_db, 2),
            severity=severity,

            venue_type=venue_type,
            time_period=time_period,

            legal_limit=compliance["legal_limit"],
            status=compliance["status"],
            exceedance=compliance["exceedance"],

            risk_score=risk["risk_score"],
            risk_level=risk["risk_level"],

            recommendation=recommendation,
        )

        db.add(report)
        db.commit()
        db.refresh(report)

        return {
            "success": True,
            "report_id": report.id,

            "source": source,
            "confidence": round(confidence, 4),

            "estimated_db": round(estimated_db, 2),
            "severity": severity,

            "venue_type": venue_type,
            "recording_time": recording_time,
            "time_period": time_period,

            "legal_limit": compliance["legal_limit"],
            "status": compliance["status"],
            "exceedance": compliance["exceedance"],

            "risk_score": risk["risk_score"],
            "risk_level": risk["risk_level"],

            "recommendation": recommendation
        }

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)