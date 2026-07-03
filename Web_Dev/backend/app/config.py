import os
from pathlib import Path

# Environment
ENV = os.getenv("ENVIRONMENT", "development")
DEBUG = ENV == "development"

# Database
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://noisegov_user:lcRlcuWIOAYVaqJPS2LwUCa5ZiA5O5rE@dpg-d93l9lcvikkc73ahe4sg-a/noisegov"
)

# API
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))

# CORS
CORS_ORIGINS = os.getenv(
    "CORS_ORIGINS",
    "http://localhost:5173"
).split(",")

# Reports
REPORTS_DIR = Path(os.getenv("REPORTS_DIR", "./reports"))
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Model paths
BASE_DIR = Path(__file__).resolve().parents[1]
DEFAULT_MODEL_DIR = BASE_DIR / "ml_models"
MODEL_DIR = Path(os.getenv("MODEL_DIR", str(DEFAULT_MODEL_DIR)))

MODEL_PATH = Path(os.getenv("MODEL_PATH", str(MODEL_DIR / "urban_noise_cnn.keras")))
ENCODER_PATH = Path(os.getenv("ENCODER_PATH", str(MODEL_DIR / "label_encoder.pkl")))
