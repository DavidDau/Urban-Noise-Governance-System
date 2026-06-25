from fastapi import APIRouter

from app.database import SessionLocal
from app.models.report import AnalysisReport

router = APIRouter()


@router.get("/")
def get_history():

    db = SessionLocal()

    reports = db.query(
        AnalysisReport
    ).order_by(
        AnalysisReport.id.desc()
    ).all()

    db.close()

    return reports