from pydantic import BaseModel


class AudioPredictionRequest(BaseModel):
    """Request schema for audio prediction endpoint"""
    pass


class AudioPredictionResponse(BaseModel):
    """Response schema for audio prediction endpoint"""
    report_id: int
    source: str
    confidence: float
    estimated_db: float
    severity: str
    venue_type: str
    time_period: str
    legal_limit: int
    status: str
    exceedance: float
    recommendation: str
    risk_score: int
    risk_level: str

    class Config:
        from_attributes = True
