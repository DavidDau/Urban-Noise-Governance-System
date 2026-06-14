# Machine Learning-Based Context-Aware Urban Acoustic Event Classification for Smart Noise Governance

Urban Noise Governance System

GitHub Repository: [https://github.com/DavidDau/Urban-Noise-Governance-System](https://github.com/DavidDau/Urban-Noise-Governance-System)

---

## Overview

This capstone project applies machine learning to urban acoustic event classification to support smarter noise governance.

Traditional noise monitoring systems focus mainly on sound intensity (decibels), which is useful for detecting noise levels but insufficient for identifying noise sources. This limits the ability of city planners and authorities to take targeted action.

This system addresses that gap by classifying environmental sounds into meaningful urban categories such as traffic, construction, entertainment, and ambience. By combining audio signal processing with deep learning, the system provides contextual insights that support better decision-making in urban noise management.

---

## Problem Statement

Urban noise pollution is a growing environmental and public health issue, especially in rapidly developing cities.

Current noise monitoring approaches rely on:

* Decibel measurements
* Manual inspections
* Public complaints

While these methods can detect excessive noise levels, they cannot automatically identify the source of the noise. This makes it difficult for stakeholders such as urban planners, businesses, and regulators to apply effective mitigation strategies.

This project aims to solve this limitation by building a machine learning system capable of identifying urban sound sources from audio recordings.

---

## Objectives

### Main Objective

To develop a machine learning system that classifies urban acoustic events and provides contextual insights for improved noise governance.

### Specific Objectives

* Prepare and process urban sound datasets for machine learning
* Develop and compare multiple machine learning models for classification
* Evaluate models using standard performance metrics
* Deploy a working API for real-time audio classification
* Demonstrate the feasibility of context-aware noise analysis in smart cities

---

## Target Classes

The system classifies audio into four main categories:

* Traffic
* Construction
* Entertainment
* Ambience

These categories are derived by grouping classes from the UrbanSound8K dataset into broader governance-focused labels.

---

## Dataset

### Primary Dataset

* UrbanSound8K

This dataset is used for preprocessing, feature extraction, model training, and evaluation.

### Future Datasets

* ESC-50
* SONYC Urban Sound Dataset
* Local Kigali Audio Dataset

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

* Audio preprocessing
* Feature extraction
* Dataset preparation
* Baseline model development
* CNN model training
* Model evaluation and comparison
* Inference pipeline design
* API deployment

---

## Feature Extraction

The model uses multiple audio features, including:

* Mel Spectrograms
* MFCCs
* Chroma Features
* Spectral Centroid
* Spectral Rolloff
* Zero Crossing Rate

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

* Accuracy: 0.82
* Precision: 0.81
* Recall: 0.80
* F1 Score: 0.80

### CNN Model (Final)

* Accuracy: 0.92
* Precision: 0.92
* Recall: 0.92
* F1 Score: 0.92

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

* Local FastAPI deployment
* Swagger UI testing
* Model inference validation

### Future Deployment

* Web application interface
* Database integration (PostgreSQL)
* Cloud deployment (AWS / Azure / Render / Railway)

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

* Identification of urban sound sources
* Context-aware noise classification
* Improved urban planning decisions
* Foundation for smart city noise governance systems

---

## Installation

### Clone repository

```
git clone https://github.com/DavidDau/Urban-Noise-Governance-System.git
```

### Navigate to project

```
cd Urban-Noise-Governance-System
```

### Create virtual environment

```
python -m venv .venv
```

### Activate environment

```
.venv\Scripts\activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run API

```
uvicorn app:app --reload
```

---

## Author

David Cyubahiro
Bachelor of Science in Machine Learning
African Leadership University (ALU)
Capstone Project 2026
