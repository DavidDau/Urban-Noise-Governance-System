from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

FEATURES_DIR = DATA_DIR / "features"

MODEL_DIR = ROOT_DIR / "saved_models"

REPORT_DIR = ROOT_DIR / "reports"