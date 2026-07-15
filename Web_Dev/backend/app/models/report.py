from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from app.database import Base


class AnalysisReport(Base):
    __tablename__ = "analysis_reports"

    id = Column(Integer, primary_key=True, index=True)

    source = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)

    estimated_db = Column(Float, nullable=False)
    severity = Column(String, nullable=False)

    venue_type = Column(String, nullable=False)
    recording_time = Column(String, nullable=False)
    time_period = Column(String, nullable=False)

    legal_limit = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    exceedance = Column(Float, nullable=False)

    recommendation = Column(String, nullable=False)

    risk_score = Column(Integer, nullable=False)
    risk_level = Column(String, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )