# Urban Noise Governance System (UNGS)

A machine learning-powered web application for intelligent urban noise monitoring, acoustic event classification, environmental compliance assessment, and governance support.

Developed as a Bachelor's Degree Capstone Project in Machine Learning.

---

# Project Overview

The Urban Noise Governance System (UNGS) enables environmental agencies and city authorities to:

- Upload environmental audio recordings
- Estimate environmental noise levels (dB)
- Classify the dominant sound source using a Convolutional Neural Network (CNN)
- Assess compliance against Rwanda Environmental Noise Regulations
- Calculate environmental risk levels
- Generate governance recommendations
- Store every analysis in a PostgreSQL database
- View historical analyses
- Monitor statistics through an analytics dashboard

The system demonstrates how Artificial Intelligence can support evidence-based environmental governance.

---

# System Architecture

```
React + Vite Frontend
        │
        │ REST API
        ▼
FastAPI Backend
        │
 ├── CNN Sound Classification
 ├── Noise Estimation
 ├── Compliance Engine
 ├── Severity Assessment
 ├── Risk Assessment
 ├── Recommendation Engine
        │
        ▼
PostgreSQL Database
```

---

# Machine Learning Model

The acoustic event classifier was trained using TensorFlow/Keras.

Input:

- WAV audio
- Mel Spectrogram (128 × 128)

Output Classes:

- Traffic
- Construction
- Entertainment
- Worship
- Ambience

The model predicts:

- Sound source
- Confidence score

---

# Features

## Audio Analysis

Users upload a WAV recording together with:

- Venue Type
- Recording Time

The backend automatically performs:

- Noise estimation (dB)
- Sound classification
- Time period detection (Day/Night)
- Compliance assessment
- Severity classification
- Risk scoring
- Recommendation generation

---

## Compliance Assessment

The system compares estimated noise levels against predefined legal limits.

Supported venue categories include:

- Residential Zone
- Commercial Zone
- Industrial Zone
- Quiet Zone
- Special Quiet Zone
- Soundproof Venue
- Non-Soundproof Venue

Outputs include:

- Legal limit
- Compliance status
- Noise exceedance

---

## Risk Assessment

Risk is determined using:

- Noise severity
- Compliance status

Outputs:

- Risk score
- Risk level

---

## Recommendation Engine

Recommendations are generated based on:

- Predicted sound source
- Compliance result

Examples:

Construction

> Verify compliance with permitted construction hours and install temporary acoustic barriers.

Traffic

> Assess congestion mitigation and roadside noise barriers.

Entertainment

> Enforce venue noise control policies.

---

## Database Storage

Every completed analysis is automatically stored.

Each report contains:

- Report ID
- Source
- Confidence
- Estimated dB
- Severity
- Venue Type
- Recording Time
- Time Period
- Legal Limit
- Compliance Status
- Exceedance
- Risk Score
- Risk Level
- Recommendation
- Created Date

The backend uses PostgreSQL hosted on Render.

---

## History

The History page retrieves every stored analysis from PostgreSQL.

Users can review previous analyses without re-uploading recordings.

---

## Dashboard

The Dashboard summarizes stored analyses, including:

- Total analyses
- Compliance distribution
- Noise severity distribution
- Sound source distribution
- Average noise level

These statistics are generated directly from the database.

---

# Tech Stack

## Frontend

- React
- Vite
- React Router
- Axios
- CSS

---

## Backend

- FastAPI
- SQLAlchemy
- TensorFlow
- Librosa
- NumPy
- Scikit-learn

---

## Database

- PostgreSQL

Hosted on Render.

---

# Project Structure

```
frontend/
    src/
        components/
        pages/
        services/
        context/
        styles/

backend/
    app/
        models/
        routes/
        services/
        dependencies.py
        database.py
        config.py
        main.py

model/
    cnn_model.keras
    label_encoder.pkl
```

---

# Backend Services

## ML Service

Responsible for:

- Audio preprocessing
- Spectrogram generation
- CNN inference
- Label decoding

---

## Noise Service

Responsible for:

- RMS calculation
- Noise estimation
- Day/Night determination

---

## Compliance Service

Responsible for:

- Legal limit lookup
- Compliance evaluation
- Recommendation generation

---

## Severity Service

Responsible for assigning:

- Low
- Moderate
- High
- Critical

---

## Risk Service

Responsible for computing:

- Risk Score
- Risk Level

---

# Current Workflow

1. User uploads a WAV file.
2. User selects the venue type.
3. User selects the recording time.
4. Frontend sends the request to the FastAPI backend.
5. Backend estimates the sound pressure level.
6. Backend classifies the sound source using the CNN.
7. Backend determines whether the recording occurred during the day or night.
8. Compliance is evaluated against environmental regulations.
9. Severity and risk are calculated.
10. Recommendations are generated.
11. Results are saved to PostgreSQL.
12. The analysis report is returned to the frontend and displayed.

---

# Deployment

## Frontend

Hosted on Render

```
https://urban-noise-governance-system.onrender.com
```

---

## Backend

Hosted on Render

```
https://ungs-docker.onrender.com
```

---

## Database

PostgreSQL 18

Hosted on Render

---

# Future Improvements

- User authentication (JWT)
- User-specific analysis history
- PDF report generation
- Interactive dashboard charts
- Live environmental monitoring
- Mobile application
- GIS-based noise heatmaps
- Kigali-specific model fine-tuning
- Government reporting tools

---

# Author

David Cyubahiro

Bachelor of Science in Machine Learning

Capstone Project

Urban Noise Governance System (UNGS)
