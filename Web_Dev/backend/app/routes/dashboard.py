from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.report import AnalysisReport

router = APIRouter()


@router.get("/")
def dashboard(db: Session = Depends(get_db)):

    # ---------------------------------------------------------
    # Basic statistics
    # ---------------------------------------------------------

    total_reports = db.query(AnalysisReport).count()

    compliant_reports = (
        db.query(AnalysisReport)
        .filter(AnalysisReport.status == "Compliant")
        .count()
    )

    non_compliant_reports = (
        db.query(AnalysisReport)
        .filter(AnalysisReport.status == "Non-Compliant")
        .count()
    )

    average_noise = (
        db.query(func.avg(AnalysisReport.estimated_db))
        .scalar()
        or 0
    )

    average_risk = (
        db.query(func.avg(AnalysisReport.risk_score))
        .scalar()
        or 0
    )

    compliance_rate = (
        round((compliant_reports / total_reports) * 100, 2)
        if total_reports > 0
        else 0
    )

    # ---------------------------------------------------------
    # Most common source
    # ---------------------------------------------------------

    common_source = (
        db.query(
            AnalysisReport.source,
            func.count(AnalysisReport.id).label("count")
        )
        .group_by(AnalysisReport.source)
        .order_by(func.count(AnalysisReport.id).desc())
        .first()
    )

    most_common_source = (
        common_source.source
        if common_source
        else "N/A"
    )

    # ---------------------------------------------------------
    # Source distribution
    # ---------------------------------------------------------

    sources = (
        db.query(
            AnalysisReport.source,
            func.count(AnalysisReport.id)
        )
        .group_by(AnalysisReport.source)
        .order_by(func.count(AnalysisReport.id).desc())
        .all()
    )

    source_distribution = [
        {
            "source": source,
            "count": count
        }
        for source, count in sources
    ]

    # ---------------------------------------------------------
    # Severity distribution
    # ---------------------------------------------------------

    severities = (
        db.query(
            AnalysisReport.severity,
            func.count(AnalysisReport.id)
        )
        .group_by(AnalysisReport.severity)
        .order_by(func.count(AnalysisReport.id).desc())
        .all()
    )

    severity_distribution = [
        {
            "severity": severity,
            "count": count
        }
        for severity, count in severities
    ]

    # ---------------------------------------------------------
    # Recent reports
    # ---------------------------------------------------------

    recent = (
        db.query(AnalysisReport)
        .order_by(AnalysisReport.created_at.desc())
        .limit(10)
        .all()
    )

    recent_reports = [
        {
            "id": report.id,
            "source": report.source,
            "estimated_db": round(report.estimated_db, 2),
            "severity": report.severity,
            "status": report.status,
            "venue_type": report.venue_type,
            "created_at": report.created_at.isoformat(),
        }
        for report in recent
    ]

    # ---------------------------------------------------------
    # Response
    # ---------------------------------------------------------

    return {
        "total_reports": total_reports,
        "compliant_reports": compliant_reports,
        "non_compliant_reports": non_compliant_reports,
        "average_noise_db": round(average_noise, 2),
        "average_risk_score": round(average_risk, 2),
        "compliance_rate": compliance_rate,
        "most_common_source": most_common_source,
        "sources": source_distribution,
        "severity": severity_distribution,
        "recent_reports": recent_reports,
    }