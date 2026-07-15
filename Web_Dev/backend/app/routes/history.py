from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.report import AnalysisReport

router = APIRouter()


@router.get("/")
def get_history(db: Session = Depends(get_db)):

    reports = (
        db.query(AnalysisReport)
        .order_by(AnalysisReport.created_at.desc())
        .all()
    )

    return [
        {
            "id": report.id,
            "created_at": report.created_at,

            "source": report.source,
            "confidence": report.confidence,

            "estimated_db": report.estimated_db,
            "severity": report.severity,

            "venue_type": report.venue_type,
            "time_period": report.time_period,

            "legal_limit": report.legal_limit,
            "status": report.status,
            "exceedance": report.exceedance,

            "risk_score": report.risk_score,
            "risk_level": report.risk_level,

            "recommendation": report.recommendation
        }
        for report in reports
    ]