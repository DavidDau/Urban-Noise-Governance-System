import logging
import traceback
import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.database import Base, engine
from app.config import CORS_ORIGINS

from app.routes import (
    analysis,
    history,
    dashboard,
    report,
    auth,
)

# ------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("noisegov")

# ------------------------------------------------------------------
# Database
# ------------------------------------------------------------------

Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------------
# FastAPI
# ------------------------------------------------------------------

app = FastAPI(
    title="Urban Noise Governance API",
    description="ML-based urban acoustic event classification",
    version="2.0"
)

# ------------------------------------------------------------------
# Startup
# ------------------------------------------------------------------

@app.on_event("startup")
async def startup():

    logger.info("=" * 70)
    logger.info("APPLICATION STARTED")
    logger.info("Registered routes:")

    for route in app.routes:
        methods = ",".join(route.methods)
        logger.info(f"{methods:15} {route.path}")

    logger.info("=" * 70)

# ------------------------------------------------------------------
# Middleware
# ------------------------------------------------------------------

@app.middleware("http")
async def request_logger(request: Request, call_next):

    start = time.perf_counter()

    logger.info("")
    logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    logger.info(f"Incoming request")
    logger.info(f"{request.method} {request.url.path}")
    logger.info(f"Client: {request.client}")
    logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    try:

        response = await call_next(request)

        elapsed = time.perf_counter() - start

        logger.info(
            f"Completed {request.method} {request.url.path}"
        )
        logger.info(
            f"Status: {response.status_code}"
        )
        logger.info(
            f"Time: {elapsed:.2f}s"
        )

        return response

    except Exception as e:

        logger.exception("Unhandled exception")

        return JSONResponse(
            status_code=500,
            content={
                "error": str(e),
                "traceback": traceback.format_exc(),
            },
        )

# ------------------------------------------------------------------
# CORS
# ------------------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------------
# Routers
# ------------------------------------------------------------------

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    analysis.router,
    prefix="/analysis",
    tags=["Analysis"],
)

app.include_router(
    history.router,
    prefix="/history",
    tags=["History"],
)

app.include_router(
    dashboard.router,
    prefix="/dashboard",
    tags=["Dashboard"],
)

app.include_router(
    report.router,
    prefix="/report",
    tags=["Report"],
)

# ------------------------------------------------------------------
# Health
# ------------------------------------------------------------------

@app.get("/")
def root():

    return {
        "status": "running",
        "service": "Urban Noise Governance API",
        "version": "2.0",
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }