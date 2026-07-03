from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import analysis, history, auth, dashboard, report
from app.database import Base, engine
from app.models.report import AnalysisReport
from app.config import CORS_ORIGINS

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Urban Noise Governance API",
    description="ML-based urban acoustic event classification for smart noise governance",
    version="2.0"
)

# CORS middleware - configurable via environment
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(analysis.router, prefix="/analysis", tags=["Analysis"])
app.include_router(history.router, prefix="/history", tags=["History"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(report.router, prefix="/report", tags=["Reports"])


@app.get("/")
def health():
    return {
        "status": "running",
        "service": "Urban Noise Governance API",
        "version": "2.0"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
