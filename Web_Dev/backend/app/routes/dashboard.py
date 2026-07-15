from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.dependencies import get_db
from app.models.report import AnalysisReport

router = APIRouter()


@router.get("/")
def dashboard(db: Session = Depends(get_db)):

    total_reports = db.query(AnalysisReport).count()

    compliant = (
        db.query(AnalysisReport)
        .filter(AnalysisReport.status == "Compliant")
        .count()
    )

    non_compliant = (
        db.query(AnalysisReport)
        .filter(AnalysisReport.status == "Non-Compliant")
        .count()
    )

    average_db = (
        db.query(func.avg(AnalysisReport.estimated_db))
        .scalar()
    )

    average_risk = (
        db.query(func.avg(AnalysisReport.risk_score))
        .scalar()
    )

    source_distribution = (
        db.query(
            AnalysisReport.source,
            func.count(AnalysisReport.id)
        )
        .group_by(AnalysisReport.source)
        .all()
    )

    severity_distribution = (
        db.query(
            AnalysisReport.severity,
            func.count(AnalysisReport.id)
        )
        .group_by(AnalysisReport.severity)
        .all()
    )

    return {

        "total_reports": total_reports,

        "compliant_reports": compliant,

        "non_compliant_reports": non_compliant,

        "average_noise_db": round(average_db or 0, 2),

        "average_risk_score": round(average_risk or 0, 2),

        "sources": [
            {
                "source": s,
                "count": c
            }
            for s, c in source_distribution
        ],

        "severity": [
            {
                "severity": s,
                "count": c
            }
            for s, c in severity_distribution
        ]
    }