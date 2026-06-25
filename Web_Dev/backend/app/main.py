from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import analysis, history, auth, dashboard, report

from app.database import Base, engine
from app.models.report import AnalysisReport

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Urban Noise Governance API",
    version="2.0"
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
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
    return {"status": "running"}