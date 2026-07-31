import os
from pathlib import Path

# ==========================================================
# Environment
# ==========================================================

ENV = os.getenv("ENVIRONMENT", "development")
DEBUG = ENV.lower() == "development"

# ==========================================================
# Database
# ==========================================================

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL environment variable is not set."
    )

# ==========================================================
# API
# ==========================================================

API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))

# ==========================================================
# CORS
# ==========================================================

CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS",
        "http://localhost:5173"
    ).split(",")
    if origin.strip()
]

# ==========================================================
# Project Paths
# ==========================================================

# app/config.py
#       ↓
# backend/
BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================================
# Reports
# ==========================================================

REPORTS_DIR = Path(
    os.getenv(
        "REPORTS_DIR",
        BASE_DIR / "reports"
    )
).resolve()

REPORTS_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# ==========================================================
# ML Models
# ==========================================================

DEFAULT_MODEL_DIR = BASE_DIR / "ml_models"

MODEL_DIR = Path(
    os.getenv(
        "MODEL_DIR",
        str(DEFAULT_MODEL_DIR)
    )
).resolve()

MODEL_PATH = Path(
    os.getenv(
        "MODEL_PATH",
        str(MODEL_DIR / "urban_noise_kigali.keras")
    )
).resolve()

ENCODER_PATH = Path(
    os.getenv(
        "ENCODER_PATH",
        str(MODEL_DIR / "label_encoder_kigali.pkl")
    )
).resolve()

# ==========================================================
# Validate Paths
# ==========================================================

if not MODEL_DIR.exists():
    raise FileNotFoundError(
        f"Model directory not found: {MODEL_DIR}"
    )

print(f"Backend directory : {BASE_DIR}")
print(f"Model directory   : {MODEL_DIR}")
print(f"Model path        : {MODEL_PATH}")
print(f"Encoder path      : {ENCODER_PATH}")
