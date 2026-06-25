from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.database import Base


class AnalysisReport(Base):
    __tablename__ = "analysis_reports"

    id = Column(Integer, primary_key=True, index=True)

    source = Column(String)
    confidence = Column(Float)

    estimated_db = Column(Float)
    severity = Column(String)

    venue_type = Column(String)
    time_period = Column(String)

    legal_limit = Column(Float)
    status = Column(String)
    exceedance = Column(Float)

    recommendation = Column(String)

    risk_score = Column(Integer)
    risk_level = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )