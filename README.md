# Urban Noise Governance System

> **Machine Learning-Based Context-Aware Urban Acoustic Event Classification for Smart Noise Governance**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Vite](https://img.shields.io/badge/Vite-Build-646CFF)
![TensorFlow](https://img.shields.io/badge/TensorFlow-CNN-FF6F00)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![License](https://img.shields.io/badge/License-Academic-green)

## Project Overview

The **Urban Noise Governance System** is a full-stack machine learning application developed as a Bachelor of Science in Machine Learning Capstone Project at the African Leadership University (ALU).

The system applies deep learning and environmental noise analysis to classify urban acoustic events, estimate sound pressure levels, evaluate compliance with Rwanda's environmental noise regulations, compute governance risk scores, and generate comprehensive PDF reports.

Unlike traditional noise monitoring systems that rely solely on sound intensity measurements, this project combines **context-aware sound classification** with regulatory compliance analysis to support informed decision-making for urban planners, regulators, businesses, and environmental authorities.

---

# Live Demo

### Web Application

https://urban-noise-governance-system.onrender.com

### Backend API

https://noisegov-api.onrender.com

### GitHub Repository

https://github.com/DavidDau/Urban-Noise-Governance-System

### Demonstration Video

https://drive.google.com/file/d/1tKlUI6ZHv2f32MKb6ltGrrvTpPrpj6lI/view?usp=sharing

---

# Key Features

- Upload WAV audio recordings
- Urban acoustic event classification using a CNN model
- Sound pressure level (dB) estimation
- Rwanda environmental noise compliance evaluation
- Governance risk score computation
- Automatic recommendation generation
- PDF report generation
- Dashboard with analysis statistics
- Analysis history
- PostgreSQL database integration
- Responsive web interface
- REST API with Swagger documentation

---

# Problem Statement

Urban noise pollution continues to affect environmental quality and public health in rapidly growing cities.

Conventional monitoring systems primarily measure sound intensity in decibels without identifying the underlying source of the noise. This limits the ability of authorities to determine appropriate mitigation measures and enforce regulations effectively.

This project addresses that challenge by introducing machine learning-based urban sound classification combined with contextual governance analysis.

---

# Objectives

## Main Objective

Develop a context-aware machine learning system that classifies urban acoustic events and supports smart noise governance through automated compliance analysis.

## Specific Objectives

- Develop a CNN model for urban sound classification
- Estimate environmental noise levels
- Evaluate compliance with Rwanda noise regulations
- Compute governance risk scores
- Generate automated PDF reports
- Store historical analyses
- Deploy a production-ready web application

---

# System Workflow

```
User Uploads WAV Audio
            │
            ▼
React Frontend
            │
            ▼
FastAPI Backend
            │
            ▼
CNN Noise Classification
            │
            ▼
Sound Level Estimation
            │
            ▼
Compliance Evaluation
            │
            ▼
Governance Risk Assessment
            │
            ▼
PDF Report Generation
            │
            ▼
PostgreSQL Storage
            │
            ▼
Results Dashboard
```

---

# Machine Learning Pipeline

The machine learning workflow consists of:

1. Audio preprocessing
2. Feature extraction
3. Mel Spectrogram generation
4. CNN inference
5. Noise category prediction
6. Decibel estimation
7. Compliance analysis
8. Governance risk computation
9. Recommendation generation
10. Report generation

---

# Target Noise Categories

The CNN model classifies urban sounds into four governance-oriented categories:

- Traffic
- Construction
- Entertainment
- Ambience

These categories were derived from the UrbanSound8K dataset to better support urban governance applications.

---

# Feature Extraction

Audio features include:

- Mel Spectrograms
- MFCCs
- Chroma Features
- Spectral Centroid
- Spectral Rolloff
- Zero Crossing Rate

---

# Technology Stack

## Frontend

- React
- Vite
- Axios
- CSS3

## Backend

- FastAPI
- Uvicorn
- TensorFlow/Keras
- Librosa
- ReportLab

## Machine Learning

- TensorFlow
- Scikit-learn
- NumPy
- Pandas

## Database

- PostgreSQL

## Deployment

- Render Web Service
- Render Static Site

---

# Repository Structure

```
Urban-Noise-Governance-System/

backend/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── schemas/
│   └── utils/
│
├── ml_models/
│   ├── urban_noise_cnn.keras
│   └── label_encoder.pkl
│
└── requirements.txt

frontend/
│
├── src/
│   ├── pages/
│   ├── components/
│   ├── services/
│   ├── context/
│   └── styles/
│
└── package.json
```

---

# Installation Guide

## Clone the Repository (Deployment branch)

```bash
git clone https://github.com/DavidDau/Urban-Noise-Governance-System.git
```

```
cd Urban-Noise-Governance-System
```

---

## Backend Setup

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure environment variables

```env
DATABASE_URL=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

Run the backend

```bash
uvicorn app.main:app --reload
```

Backend available at

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

---

## Frontend Setup

Navigate to the frontend directory

```bash
cd frontend
```

Install dependencies

```bash
npm install
```

Configure environment variables

```env
VITE_API_URL=http://localhost:8000
```

Run the application

```bash
npm run dev
```

Frontend available at

```
http://localhost:5173
```

---

# Deployment

## Frontend

Hosted on Render Static Site

https://urban-noise-governance-system.onrender.com

## Backend

Hosted on Render Web Service

https://noisegov-api.onrender.com

## Database

PostgreSQL hosted on Render

Deployment verification included:

- Backend health endpoint
- Frontend connectivity
- API communication
- Database connectivity
- PDF generation
- End-to-end prediction workflow

---

# REST API

## Health Check

```
GET /
```

```
GET /health
```

## Documentation

```
GET /docs
```

## Noise Analysis

```
POST /analysis/predict
```

Input:

- WAV audio
- Venue
- Time period

Output:

- Predicted class
- Estimated dB
- Compliance status
- Governance risk score
- Recommendations
- Generated report

---

# Testing Strategy

The application was tested using multiple testing strategies to validate functionality and deployment.

## Functional Testing

Validated:

- Audio upload
- File validation
- CNN inference
- dB estimation
- Compliance evaluation
- Risk score computation
- PDF generation
- Dashboard updates
- History retrieval

## Input Validation Testing

Different data values were tested including:

- Different urban sound recordings
- Different venue selections
- Different operational time periods
- Invalid file handling

## Integration Testing

Verified interactions between:

- React Frontend
- FastAPI Backend
- CNN Model
- PostgreSQL Database
- PDF Generation Service

## Deployment Testing

Verified after deployment on Render by confirming:

- API accessibility
- Frontend accessibility
- Database connectivity
- End-to-end analysis workflow

---

# Performance Evaluation

The deployed application was tested on multiple devices and browsers.

| Device     | Browser | Result |
| ---------- | ------- | ------ |
| Windows 11 | Chrome  | Passed |
| Windows 11 | Edge    | Passed |
| Android    | Chrome  | Passed |
| iPhone     | Safari  | Passed |

The application demonstrated responsive performance and consistent functionality across tested environments.

---

# Testing Results

The demonstration video includes successful execution of:

- WAV file upload
- Noise classification
- Venue-based analysis
- Time-aware compliance evaluation
- Governance risk assessment
- Dashboard statistics
- Analysis history retrieval
- PDF report generation

---

# Analysis of Results

The developed system successfully achieved the primary objectives defined during the project proposal.

The CNN model accurately classified urban acoustic events and enabled context-aware governance analysis beyond traditional decibel monitoring. Integration of sound classification with compliance evaluation and governance risk assessment demonstrated the practical application of machine learning in environmental management.

Deployment of both the frontend and backend validated the feasibility of providing noise analysis as a web-based service. PostgreSQL integration enabled persistent storage of historical analyses, while automated PDF generation improved reporting capabilities.

The system therefore extends conventional environmental noise monitoring by incorporating contextual information necessary for evidence-based governance and decision-making.

---

# Discussion

The milestones achieved throughout the project demonstrate the successful integration of machine learning, software engineering, and environmental governance principles.

Developing the CNN classification model established the core intelligent component of the application, while subsequent integration with FastAPI, PostgreSQL, and the React frontend transformed the research prototype into a deployable decision-support system.

The deployed application provides stakeholders with automated noise analysis, regulatory compliance evaluation, and governance recommendations through an accessible web interface. This demonstrates how machine learning can contribute to smarter urban management and sustainable city planning.

---

# Recommendations and Future Work

Future improvements include:

- User authentication and role-based access control
- Real-time environmental monitoring using IoT sensors
- Mobile application development
- Live audio streaming support
- Expanded urban sound datasets
- Improved CNN architectures for higher classification accuracy
- GIS-based visualization of noise hotspots
- Integration with national environmental monitoring systems
- Multi-language reporting
- Automated alert notifications for regulatory violations

---

# Visuals

The following Visuals are demonstrated in the accompanying project video:

- Landing Page
- Dashboard
- Analysis Page
- Results Page
- History Page

---

# Demonstration Video

https://drive.google.com/file/d/1tKlUI6ZHv2f32MKb6ltGrrvTpPrpj6lI/view?usp=sharing

---

# Author

**David Cyubahiro**

Bachelor of Science in Machine Learning

African Leadership University (ALU)

Capstone Project 2026

---

# License

This project was developed for academic purposes as part of the Bachelor of Science in Machine Learning Capstone Project at the African Leadership University.
