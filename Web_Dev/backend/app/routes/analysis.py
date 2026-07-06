import os
import tempfile
import time
import logging

from fastapi import APIRouter, UploadFile, File, Form

from app.services.pdf_service import generate_pdf
from app.database import SessionLocal
from app.models.report import AnalysisReport
from app.schemas.venue import VenueType
from app.services.ml_service import predict_source
from app.services.noise_service import estimate_db, get_time_period
from app.services.severity_service import get_severity
from app.services.compliance_service import (
    check_compliance,
    get_recommendation
)
from app.services.risk_service import calculate_risk_score
from app.config import REPORTS_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/predict")
async def analyze_audio(
    file: UploadFile = File(...),
    venue_type: VenueType = Form(...),
    recording_time: str = Form(...)
):

    start = time.perf_counter()
    print("\n========== NEW ANALYSIS REQUEST ==========")

    temp_path = None

    try:

        # Save uploaded file
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as tmp:

            tmp.write(await file.read())
            temp_path = tmp.name

        print(f"1. File saved: {time.perf_counter() - start:.2f}s")

        # ML prediction
        source, confidence = predict_source(temp_path)

        print(f"2. ML prediction complete: {time.perf_counter() - start:.2f}s")

        # Noise analysis
        estimated_db = estimate_db(temp_path)

        print(f"3. dB estimation complete: {time.perf_counter() - start:.2f}s")

        severity = get_severity(
            estimated_db
        )

        period = get_time_period(
            recording_time
        )

        compliance = check_compliance(
            estimated_db,
            venue_type.value,
            period
        )

        recommendation = get_recommendation(
            source,
            compliance["status"]
        )

        risk = calculate_risk_score(
            severity,
            compliance["status"]
        )

        print(f"4. Governance analysis complete: {time.perf_counter() - start:.2f}s")

        # Save to database
        db_session = SessionLocal()

        report = AnalysisReport(
            source=source,
            confidence=confidence,
            estimated_db=estimated_db,
            severity=severity,
            venue_type=venue_type.value,
            time_period=period,
            legal_limit=compliance["legal_limit"],
            status=compliance["status"],
            exceedance=compliance["exceedance"],
            recommendation=recommendation,
            risk_score=risk["score"],
            risk_level=risk["level"]
        )

        db_session.add(report)
        db_session.commit()
        db_session.refresh(report)
        db_session.close()

        print(f"5. Database saved: {time.perf_counter() - start:.2f}s")

        # Generate PDF report
        pdf_path = REPORTS_DIR / f"report_{report.id}.pdf"

        generate_pdf(report, str(pdf_path))

        print(f"6. PDF generated: {time.perf_counter() - start:.2f}s")
        print(f"========== TOTAL TIME: {time.perf_counter() - start:.2f}s ==========\n")

        # API response
        return {
            "report_id": report.id,
            "source": source,
            "confidence": round(confidence, 4),
            "estimated_db": estimated_db,
            "severity": severity,
            "venue_type": venue_type.value,
            "time_period": period,
            "legal_limit": compliance["legal_limit"],
            "status": compliance["status"],
            "exceedance": compliance["exceedance"],
            "recommendation": recommendation,
            "risk_score": risk["score"],
            "risk_level": risk["level"]
        }

    except Exception as e:
        print(f"\nERROR during analysis: {e}")
        raise

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)