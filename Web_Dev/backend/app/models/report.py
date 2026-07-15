from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from app.database import Base


class AnalysisReport(Base):
    __tablename__ = "analysis_reports"

    id = Column(Integer, primary_key=True, index=True)

    # Future authentication support
    user_id = Column(Integer, nullable=True)

    # ML prediction
    source = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)

    # Noise analysis
    estimated_db = Column(Float, nullable=False)
    severity = Column(String, nullable=False)

    # Context
    venue_type = Column(String, nullable=False)
    time_period = Column(String, nullable=False)

    # Compliance
    legal_limit = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    exceedance = Column(Float, nullable=False)

    # Risk assessment
    risk_score = Column(Integer, nullable=False)
    risk_level = Column(String, nullable=False)

    # Recommendation
    recommendation = Column(String, nullable=False)

    # Timestamp
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )