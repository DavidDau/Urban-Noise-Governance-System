# Machine Learning-Based Context-Aware Urban Acoustic Event Classification for Smart Noise Governance

Github link: [https://github.com/DavidDau/Urban-Noise-Governance-System.git]

## Overview

This project is a capstone research project that explores the use of Machine Learning (ML) for contextual urban noise analysis. Traditional noise monitoring systems primarily measure sound intensity in decibels (dB) but often fail to identify the source of the noise. As a result, decision-makers lack sufficient contextual information to determine appropriate mitigation strategies.

The proposed system addresses this limitation by automatically classifying urban acoustic events into meaningful categories such as traffic noise, construction noise, entertainment venue noise, worship/prayer noise, and normal urban ambience. By combining audio signal processing and machine learning techniques, the system aims to provide contextual acoustic intelligence that supports smarter noise governance and informed decision-making.

---

## Problem Statement

Urban noise pollution is becoming an increasingly significant environmental and public health challenge, particularly in rapidly growing cities. Existing approaches to noise management rely heavily on decibel measurements, manual inspections, and public complaints. While these methods can determine whether noise exceeds legal thresholds, they cannot automatically identify the source of the noise.

This limitation creates challenges for venue owners, businesses, local authorities, and urban planners who need contextual information to make informed noise management decisions.

The project seeks to bridge this gap by developing a machine learning-based acoustic event classification system capable of identifying urban sound sources from audio recordings.

---

## Project Objectives

### Main Objective

To develop a machine learning-based system that classifies urban acoustic events and provides contextual acoustic intelligence for improved urban noise governance.

### Specific Objectives

1. Analyze and prepare urban sound datasets for machine learning classification.
2. Develop and compare multiple machine learning models for acoustic event classification.
3. Evaluate model performance using standard classification metrics.
4. Develop a prototype API capable of receiving audio files and returning classification results.
5. Demonstrate the feasibility of contextual noise analysis for smart urban management.

---

## Target Sound Categories

The system classifies audio recordings into the following categories:

- Traffic Noise
- Construction Noise
- Entertainment Venue Noise
- Worship/Prayer Noise
- Normal Urban Ambience

---

## Datasets

The project is designed to support multiple environmental sound datasets.

### Planned Datasets

#### UrbanSound8K

A widely used environmental sound dataset containing urban sound recordings across multiple categories.

#### ESC-50

A benchmark dataset for environmental sound classification.

#### SONYC Urban Sound Dataset

A large-scale urban acoustic monitoring dataset developed for smart city applications.

#### Local Kigali Audio Dataset

Approximately 100 locally collected audio recordings from selected locations in Kigali City.

---

## Technology Stack

### Machine Learning

- Python
- TensorFlow
- Scikit-learn
- Librosa
- NumPy
- Pandas

### Data Visualization

- Matplotlib
- Seaborn

### API Development

- FastAPI
- Swagger UI

### Database (Future Work)

- PostgreSQL

### Frontend (Future Work)

- HTML
- CSS
- Bootstrap

---

## Machine Learning Workflow

1. Data Collection
2. Audio Preprocessing
3. Feature Extraction
4. Exploratory Data Analysis
5. Model Training
6. Model Evaluation
7. Model Selection
8. API Integration

### Feature Extraction

The following audio features will be extracted:

- Mel-Frequency Cepstral Coefficients (MFCCs)
- Mel Spectrograms
- Chroma Features
- Spectral Centroid
- Spectral Rolloff
- Zero Crossing Rate

---

## Planned Models

### Random Forest Classifier

Used as a baseline traditional machine learning model.

### Support Vector Machine (SVM)

Used for comparative performance analysis.

### Convolutional Neural Network (CNN)

Used for spectrogram-based deep learning classification.

---

## Evaluation Metrics

The models will be evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

The best-performing model will be selected based on overall classification performance.

---

## API Prototype

The MVP will expose a simple FastAPI endpoint.

### Endpoint

```http
POST /predict
```

### Input

Audio file (.wav, .mp3)

### Example Response

```json
{
  "prediction": "Traffic Noise",
  "confidence": 0.92
}
```

Swagger UI documentation will be available through:

```http
http://localhost:8000/docs
```

---

## Mockups

The MVP includes user interface mockups demonstrating:

- Landing Page
- Audio Upload Interface
- Classification Results Dashboard
- Historical Reports Page

---

## Deployment Plan

### MVP Phase

- Local development environment
- FastAPI backend
- Swagger UI testing

### Future Deployment

```text
User
 ↓
Web Application
 ↓
FastAPI Backend
 ↓
Machine Learning Model
 ↓
PostgreSQL Database
```

Potential hosting platforms:

- Render
- Railway
- AWS
- Azure

---

## Expected Outcomes

The project is expected to demonstrate that machine learning can provide contextual understanding of urban noise sources beyond traditional decibel measurements.

The final system will support:

- Urban sound source identification
- Context-aware noise analysis
- Improved decision-making for noise management
- Future integration into smart city initiatives

---

## Installation

Clone the repository:

```bash
git clone https://github.com/DavidDau/Urban-Noise-Governance-System.git
```

Navigate to the project directory:

```bash
cd Urban-Noise-Governance
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

---

## Author

David Cyubahiro

Bachelor of Science in Machine Learning

African Leadership University (ALU)

Capstone Project – 2026
