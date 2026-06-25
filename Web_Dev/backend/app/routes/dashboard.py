from fastapi import APIRouter
from sqlalchemy import func

from app.database import SessionLocal
from app.models.report import AnalysisReport

router = APIRouter()


@router.get("/")
def get_dashboard():

    db = SessionLocal()

    total_reports = db.query(
        AnalysisReport
    ).count()

    average_db = db.query(
        func.avg(
            AnalysisReport.estimated_db
        )
    ).scalar()

    most_common_source = db.query(
        AnalysisReport.source,
        func.count(
            AnalysisReport.source
        ).label("count")
    ).group_by(
        AnalysisReport.source
    ).order_by(
        func.count(
            AnalysisReport.source
        ).desc()
    ).first()

    compliant_count = db.query(
        AnalysisReport
    ).filter(
        AnalysisReport.status == "Compliant"
    ).count()

    compliance_rate = 0

    if total_reports > 0:
        compliance_rate = round(
            (compliant_count / total_reports) * 100,
            2
        )

    recent_reports = db.query(
        AnalysisReport
    ).order_by(
        AnalysisReport.id.desc()
    ).limit(5).all()

    db.close()

    return {
        "total_reports": total_reports,
        "average_db": round(average_db or 0, 2),
        "most_common_source":
            most_common_source[0]
            if most_common_source
            else "N/A",
        "compliance_rate": compliance_rate,
        "recent_reports": recent_reports
    }