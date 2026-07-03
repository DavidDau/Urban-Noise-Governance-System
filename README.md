# Machine Learning-Based Context-Aware Urban Acoustic Event Classification for Smart Noise Governance

Urban Noise Governance System

GitHub Repository: [https://github.com/DavidDau/Urban-Noise-Governance-System](https://github.com/DavidDau/Urban-Noise-Governance-System)
Video Demo: (https://youtu.be/OJ99LWV6-TQ)

---

## Overview

This capstone project applies machine learning to urban acoustic event classification to support smarter noise governance.

Traditional noise monitoring systems focus mainly on sound intensity (decibels), which is useful for detecting noise levels but insufficient for identifying noise sources. This limits the ability of city planners and authorities to take targeted action.

This system addresses that gap by classifying environmental sounds into meaningful urban categories such as traffic, construction, entertainment, and ambience. By combining audio signal processing with deep learning, the system provides contextual insights that support better decision-making in urban noise management.

---

## Problem Statement

Urban noise pollution is a growing environmental and public health issue, especially in rapidly developing cities.

Current noise monitoring approaches rely on:

- Decibel measurements
- Manual inspections
- Public complaints

While these methods can detect excessive noise levels, they cannot automatically identify the source of the noise. This makes it difficult for stakeholders such as urban planners, businesses, and regulators to apply effective mitigation strategies.

This project aims to solve this limitation by building a machine learning system capable of identifying urban sound sources from audio recordings.

---

## Objectives

### Main Objective

To develop a machine learning system that classifies urban acoustic events and provides contextual insights for improved noise governance.

### Specific Objectives

- Prepare and process urban sound datasets for machine learning
- Develop and compare multiple machine learning models for classification
- Evaluate models using standard performance metrics
- Deploy a working API for real-time audio classification
- Demonstrate the feasibility of context-aware noise analysis in smart cities

---

## Target Classes

The system classifies audio into four main categories:

- Traffic
- Construction
- Entertainment
- Ambience

These categories are derived by grouping classes from the UrbanSound8K dataset into broader governance-focused labels.

---

## Dataset

### Primary Dataset

- UrbanSound8K

This dataset is used for preprocessing, feature extraction, model training, and evaluation.

### Future Datasets

- ESC-50
- SONYC Urban Sound Dataset
- Local Kigali Audio Dataset

---

## Technology Stack

### Machine Learning

Python, TensorFlow, Scikit-learn, Librosa, NumPy, Pandas

### Visualization

Matplotlib, Seaborn

### API Development

FastAPI, Swagger UI

### Future Enhancements

PostgreSQL, HTML, CSS, Bootstrap

---

## Machine Learning Pipeline

The system follows a structured ML workflow:

- Audio preprocessing
- Feature extraction
- Dataset preparation
- Baseline model development
- CNN model training
- Model evaluation and comparison
- Inference pipeline design
- API deployment

---

## Feature Extraction

The model uses multiple audio features, including:

- Mel Spectrograms
- MFCCs
- Chroma Features
- Spectral Centroid
- Spectral Rolloff
- Zero Crossing Rate

---

## Models Implemented

### Random Forest Classifier

Used as a baseline model for initial performance comparison.

### Convolutional Neural Network (CNN)

Primary model used for final deployment, trained on Mel spectrograms.

### Support Vector Machine (SVM)

Evaluated during experimentation but not included in the final MVP.

---

## Model Performance

### Random Forest (Baseline)

- Accuracy: 0.82
- Precision: 0.81
- Recall: 0.80
- F1 Score: 0.80

### CNN Model (Final)

- Accuracy: 0.92
- Precision: 0.92
- Recall: 0.92
- F1 Score: 0.92

The CNN model achieved the best performance and was selected for deployment.

---

## API Prototype

A FastAPI-based inference service exposes the trained model for real-time predictions.

### Endpoint

POST /predict

### Input

Audio file in WAV format

### Example Response

```json
{
  "prediction": "Construction",
  "confidence": 0.92
}
```

Swagger documentation is available at:

[http://localhost:8000/docs](http://localhost:8000/docs)

---

## System Architecture

User
→ API Request
→ FastAPI Backend
→ CNN Model
→ Prediction Response

---

## Deployment Plan

### MVP Phase

- Local FastAPI deployment
- Swagger UI testing
- Model inference validation

### Future Deployment

- Web application interface
- Database integration (PostgreSQL)
- Cloud deployment (AWS / Azure / Render / Railway)

---

## Project Structure

```
Urban-Noise-Governance-System/

README.md

ml/
├── notebooks/
├── preprocessing/
├── saved_models/
└── data/

deployment/
├── app.py
└── models/

docs/
└── screenshots/
```

---

## Expected Outcomes

This project demonstrates that machine learning can move urban noise analysis beyond simple decibel measurement toward contextual understanding of sound sources.

The system enables:

- Identification of urban sound sources
- Context-aware noise classification
- Improved urban planning decisions
- Foundation for smart city noise governance systems

---

---

## Installation & Local Development

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 15+ (or Docker)
- Git

### Quick Start with Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/DavidDau/Urban-Noise-Governance-System.git
cd Urban-Noise-Governance-System

# Start full stack (PostgreSQL + Backend + Frontend)
docker-compose up -d

# Wait 30 seconds for services to initialize
sleep 30

# Test
curl http://localhost:8000/health        # Should return {"status": "healthy"}
curl http://localhost:3000               # Should load frontend

# Visit http://localhost:3000 in browser
```

Stop with: `docker-compose down`

### Manual Setup

#### Backend Setup

```bash
# Navigate to backend
cd Web_Dev/backend

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate
# Or (macOS/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements-prod.txt

# Create .env file
cp .env.example .env

# Edit .env and set PostgreSQL connection (or keep SQLite for dev)
# DATABASE_URL=postgresql://user:password@localhost:5432/noisegov

# Run API
uvicorn app.main:app --reload
```

API available at:

- **API:** http://localhost:8000
- **Docs:** http://localhost:8000/docs
- **Health:** http://localhost:8000/health

#### Frontend Setup

```bash
# In another terminal
cd Web_Dev/frontend

# Install dependencies
npm install

# Create environment file
echo "VITE_API_URL=http://localhost:8000" > .env.local

# Run dev server
npm run dev
```

Frontend available at: http://localhost:5173

---

## API Reference

### Health Check

```bash
curl http://localhost:8000/health
# Response: {"status": "healthy"}
```

### Analyze Audio

```bash
curl -X POST "http://localhost:8000/analysis/predict" \
  -F "file=@audio.wav" \
  -F "venue_type=Residential Zone" \
  -F "recording_time=14:30"
```

**Venue Types:**

- Residential Zone
- Commercial Zone
- Industrial Zone
- Quiet Zone
- Special Quiet Zone
- Soundproof Venue
- Non-Soundproof Venue

**Response:**

```json
{
  "report_id": 1,
  "source": "Traffic",
  "confidence": 0.9234,
  "estimated_db": 72.5,
  "severity": "High",
  "status": "Non-Compliant",
  "recommendation": "Assess peak-hour congestion around Kigali CBD."
}
```

### Get Dashboard Stats

```bash
curl http://localhost:8000/dashboard/
```

### Get Analysis History

```bash
curl http://localhost:8000/history/
```

### Download Report PDF

```bash
curl http://localhost:8000/report/download/1 -o report.pdf
```

**Full API documentation available at** `http://localhost:8000/docs`

---

## Deployment

### Environment Configuration

Create `.env` file in `Web_Dev/backend/`:

```bash
# Copy from template
cp .env.example .env

# Edit for your environment
ENVIRONMENT=production
DATABASE_URL=postgresql://user:password@host:5432/noisegov
CORS_ORIGINS=https://your-frontend-domain.com
API_HOST=0.0.0.0
API_PORT=8000
```

### Option 1: GitHub + Render (Recommended)

#### Backend on Render

1. Push to GitHub
2. Go to [render.com](https://render.com)
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Build Command:** `pip install -r Web_Dev/backend/requirements-prod.txt`
   - **Start Command:** `cd Web_Dev/backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Runtime:** Python 3.11
6. Set environment variables:
   - `ENVIRONMENT=production`
   - `DATABASE_URL=postgresql://user:pass@host:5432/noisegov`
   - `CORS_ORIGINS=https://your-frontend-domain.com`
7. Deploy

API will be at: `https://noisegov-api.onrender.com` (or your chosen name)

#### Frontend on GitHub Pages or Render

**Option A: GitHub Pages (Free, static only)**

```bash
# Build frontend
cd Web_Dev/frontend
npm run build

# Push dist/ to GitHub Pages
# Set repository settings: Deploy from branch gh-pages
# Site will be at: https://yourusername.github.io/Urban-Noise-Governance-System
```

**Option B: Render Static Site**

1. Create Static Site on Render
2. Connect GitHub
3. **Build Command:** `cd Web_Dev/frontend && npm install && npm run build`
4. **Publish Directory:** `Web_Dev/frontend/dist`
5. Set environment: `VITE_API_URL=https://noisegov-api.onrender.com`
6. Deploy

### Option 2: Docker Compose (Local/Self-Hosted)

```bash
# Build and start all services
docker-compose build
docker-compose up -d

# Services:
# - Frontend: http://localhost:3000
# - Backend: http://localhost:8000
# - Database: PostgreSQL on port 5432
```

### Option 3: Manual Server Deployment

```bash
# SSH into server
ssh user@your-server.com

# Clone repository
git clone https://github.com/DavidDau/Urban-Noise-Governance-System.git
cd Urban-Noise-Governance-System

# Setup backend
cd Web_Dev/backend
python -m venv venv
source venv/bin/activate
pip install -r requirements-prod.txt
cp .env.example .env
# Edit .env with your settings

# Run with process manager (example: PM2)
npm install -g pm2
pm2 start "uvicorn app.main:app --host 0.0.0.0 --port 8000" --name noisegov-api

# Setup frontend
cd ../frontend
npm install
npm run build

# Serve with nginx (optional, or use separate static hosting)
```

---

## Database Setup

### SQLite (Development)

- Default, automatically created
- Location: `Web_Dev/backend/noisegov.db`
- Not recommended for production

### PostgreSQL (Production)

**Local PostgreSQL:**

```bash
# Install PostgreSQL or use Docker
docker run --name postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres:15

# Update .env
DATABASE_URL=postgresql://postgres:password@localhost:5432/noisegov

# Restart backend
```

**Render PostgreSQL:**

1. Create PostgreSQL database on Render
2. Get connection string
3. Set `DATABASE_URL` in Render environment variables

---

## Troubleshooting

### Port Already in Use

```bash
# Find process using port 8000
lsof -i :8000

# Kill process
kill -9 <PID>
```

### CORS Error

```
Access-Control-Allow-Origin missing
```

**Solution:** Update `CORS_ORIGINS` in `.env` and restart backend

### Model Not Found

```
FileNotFoundError: Model not found
```

**Solution:** Verify files exist:

```bash
ls Web_Dev/backend/ml_models/
# Should contain: urban_noise_cnn.keras, label_encoder.pkl
```

### Database Connection Error

```
operational error (sqlite3.OperationalError)
```

**Solution:**

```bash
# Delete and recreate
rm Web_Dev/backend/noisegov.db

# Restart backend (auto-creates)
```

### Frontend Can't Reach Backend

1. Check `VITE_API_URL` in `.env.local`
2. Verify backend is running
3. Check CORS configuration
4. Verify firewall allows requests

---

## Project Structure

```
Urban-Noise-Governance-System/
├── README.md                    # This file
├── docker-compose.yml           # Local development stack
├── .gitignore
│
├── ml/                          # Machine Learning pipeline
│   ├── config/                  # Configuration constants
│   │   ├── classes.py          # Audio classes (traffic, construction, etc.)
│   │   ├── experiment.py       # ML experiment settings
│   │   └── paths.py            # File paths
│   ├── data/                    # Datasets
│   │   ├── raw/                # UrbanSound8K dataset
│   │   ├── processed/          # Processed audio files
│   │   └── features/           # Extracted features
│   ├── feature_engineering/     # Feature extraction
│   │   ├── mfcc.py
│   │   └── spectrogram.py
│   ├── preprocessing/           # Audio preprocessing
│   │   ├── audio_loader.py
│   │   └── resampler.py
│   ├── notebooks/               # Jupyter notebooks
│   │   ├── 01_audio_pipeline.ipynb
│   │   ├── 02_feature_extraction.ipynb
│   │   ├── 03_dataset_creation.ipynb
│   │   └── 04_baseline_models.ipynb
│   └── saved_models/            # Trained models
│       ├── urban_noise_cnn.keras
│       └── label_encoder.pkl
│
├── Web_Dev/
│   ├── backend/                 # FastAPI backend
│   │   ├── app/
│   │   │   ├── main.py         # FastAPI app
│   │   │   ├── config.py       # Configuration management
│   │   │   ├── database.py     # Database setup
│   │   │   ├── models/         # Database models
│   │   │   ├── routes/         # API endpoints
│   │   │   ├── schemas/        # Pydantic schemas
│   │   │   ├── services/       # Business logic
│   │   │   └── utils/          # Utilities
│   │   ├── ml_models/          # Model files (symlink to ml/saved_models)
│   │   ├── requirements-prod.txt # Production dependencies (minimal)
│   │   ├── .env.example         # Environment template
│   │   ├── Dockerfile          # Backend container
│   │   ├── .dockerignore
│   │   └── render.yaml         # Render deployment config
│   │
│   └── frontend/                # React + Vite
│       ├── src/
│       │   ├── components/     # React components
│       │   ├── pages/          # Page components
│       │   ├── services/       # API service
│       │   ├── context/        # React context
│       │   └── styles/         # CSS
│       ├── package.json
│       ├── vite.config.js
│       ├── Dockerfile          # Frontend container
│       ├── nginx.conf          # Nginx SPA routing
│       ├── .env.example        # Environment template
│       └── .dockerignore
│
└── docs/                        # Additional documentation
```

---

## Common Issues & Solutions

### Local Development Issues

**"ModuleNotFoundError: No module named 'app'"**

```bash
# Wrong:
cd Web_Dev
python app/main.py

# Right:
cd Web_Dev/backend
uvicorn app.main:app --reload
```

**"Cannot GET /" on frontend**

- Ensure frontend is running: `npm run dev`
- Check that it's on http://localhost:5173

**Database corrupted**

```bash
# Delete and recreate
rm Web_Dev/backend/noisegov.db
# Restart backend
```

### Deployment Issues

**Render build fails**

1. Check build logs in Render dashboard
2. Verify `render.yaml` has correct paths
3. Ensure Python version is 3.11+
4. Verify all dependencies in `requirements-prod.txt` install correctly

**502 Bad Gateway**

1. Check Render logs
2. Verify environment variables set correctly
3. Verify model files exist
4. Test locally first

**CORS errors in production**

1. Update `CORS_ORIGINS` environment variable
2. Include both http and https versions of your domain
3. Restart backend

**"Model not found" errors**

1. Verify `ml_models/` directory exists in deployment
2. Verify file paths in `app/config.py` are correct
3. Check file permissions

---

## Configuration

### Environment Variables

**Backend (.env):**

```
ENVIRONMENT=production          # or development
DATABASE_URL=postgresql://...   # or sqlite:///./noisegov.db
CORS_ORIGINS=https://your-domain.com,https://www.your-domain.com
API_HOST=0.0.0.0
API_PORT=8000
REPORTS_DIR=./reports
```

**Frontend (.env.local or .env.production):**

```
VITE_API_URL=http://localhost:8000    # or production API URL
```

---

## API Endpoints Summary

| Method | Endpoint                | Description          |
| ------ | ----------------------- | -------------------- |
| GET    | `/`                     | API info             |
| GET    | `/health`               | Health check         |
| POST   | `/analysis/predict`     | Analyze audio file   |
| GET    | `/dashboard/`           | Dashboard statistics |
| GET    | `/history/`             | Analysis history     |
| GET    | `/report/download/{id}` | Download PDF report  |

---

## Model Information

### Labels (Lowercase)

- `traffic`
- `construction`
- `entertainment`
- `worship`
- `ambience`

### Performance

- **Model:** CNN trained on Mel spectrograms
- **Accuracy:** 92%
- **Input:** WAV audio file, 22050 Hz sample rate
- **Output:** Classification + confidence score

### Updating the Model

To use a new trained model:

1. Train using Jupyter notebooks in `ml/notebooks/`
2. Export model as `urban_noise_cnn.keras`
3. Export label encoder as `label_encoder.pkl` (sklearn LabelEncoder)
4. Replace files in `Web_Dev/backend/ml_models/`
5. Restart API (model loads automatically)

---

## Testing

### Manual Testing

1. **Upload audio:**
   - Navigate to http://localhost:5173
   - Select WAV file
   - Choose venue type and time
   - Click "Analyze"

2. **Test API directly:**

   ```bash
   curl -X POST "http://localhost:8000/analysis/predict" \
     -F "file=@test.wav" \
     -F "venue_type=Residential Zone" \
     -F "recording_time=14:30"
   ```

3. **Check health:**
   ```bash
   curl http://localhost:8000/health
   ```

---

## Architecture

```
User Interface (React)
         ↓
    Frontend (Vite)
         ↓
   FastAPI Backend
         ↓
    ML Pipeline
         ├─ Audio Loading
         ├─ Feature Extraction
         ├─ CNN Model
         └─ Predictions
         ↓
    Analysis Services
         ├─ Noise Analysis
         ├─ Compliance Check
         ├─ Risk Assessment
         └─ Recommendations
         ↓
   Database (PostgreSQL)
         ↓
    PDF Reports
```

---

## Future Enhancements

- [ ] User authentication (JWT + PostgreSQL)
- [ ] Advanced analytics and visualizations
- [ ] Real-time monitoring dashboard
- [ ] Mobile app (React Native)
- [ ] AI-powered recommendations
- [ ] Integration with IoT sensors
- [ ] Government compliance reporting
- [ ] Machine learning model improvements

---

## Security Considerations

### Current Status

- Basic input validation (Pydantic)
- CORS configured
- No authentication (add for production)
- No rate limiting (add for production)

### Production Checklist

- [ ] Add JWT authentication
- [ ] Add rate limiting
- [ ] Enable HTTPS (auto on cloud platforms)
- [ ] Add request logging
- [ ] Set up monitoring and alerts
- [ ] Regular dependency updates
- [ ] Database backups

---

## Performance Optimization

### Inference Speed

- Audio loading: ~100ms
- Feature extraction: ~200ms
- Model inference: ~1-2 seconds
- **Total: ~1.5-2.5 seconds per audio file**

### Scaling Recommendations

- Use PostgreSQL for concurrent users
- Add caching for repeated analyses
- Consider GPU acceleration for inference
- Implement job queue for batch processing (Celery + Redis)

---

## Support & Contributions

### Issues

Found a bug? [Open an issue on GitHub](https://github.com/DavidDau/Urban-Noise-Governance-System/issues)

### Contributing

Pull requests welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## Author

**David Cyubahiro**

- Bachelor of Science in Machine Learning
- African Leadership University (ALU)
- Capstone Project 2026

---

## License

This project is part of an academic capstone. Please refer to LICENSE file for usage terms.

---

## Acknowledgments

- **Dataset:** UrbanSound8K
- **Framework:** FastAPI, React, TensorFlow
- **Deployment:** Render, GitHub
- **Mentors & Advisors:** ALU Faculty

---

**Last Updated:** July 3, 2026
**Status:** ✅ Production Ready (with PostgreSQL + deployment configured)
