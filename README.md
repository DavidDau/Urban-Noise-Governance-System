# Urban Noise Classification and Governance Decision Support System

A Bachelor's Capstone Project that combines Deep Learning and Web Technologies to automatically classify environmental noise sources, estimate noise pollution levels, assess legal compliance, generate governance recommendations and visualize historical analyses through an interactive dashboard.

## Project Overview

Urban noise pollution has become a growing environmental challenge in rapidly developing cities. Traditional monitoring methods rely heavily on manual inspections, making it difficult for environmental agencies to monitor noise trends continuously.

This project presents an intelligent decision support system capable of:

- Classifying environmental noise using a Convolutional Neural Network (CNN)
- Estimating environmental noise levels (dB)
- Assessing compliance with environmental regulations
- Calculating governance risk scores
- Generating automated recommendations
- Producing PDF reports
- Visualizing historical analyses through a web dashboard

The system combines Machine Learning, FastAPI, React and SQLite into a complete end-to-end solution.

# Features

## Machine Learning

- Audio preprocessing
- Mel Spectrogram generation
- CNN-based environmental sound classification
- Transfer Learning using SONYC-UST
- Fine-tuning using Kigali environmental noise recordings
- Confidence score prediction

Supports five environmental noise classes:

- Traffic
- Construction
- Entertainment
- Worship
- Ambience

## Web Application

- Audio upload
- Noise classification
- Noise level estimation
- Compliance assessment
- Governance risk assessment
- Recommendation generation
- PDF report generation
- Historical analysis storage
- Interactive dashboard

# Repository Structure

```
.
├── Web_Dev
│   ├── backend
│   └── frontend
│
├── ml
│   ├── notebooks
│   ├── preprocessing
│   ├── feature_engineering
│   ├── config
│   └── utils
│
├── reports
├── requirements.txt
├── docker-compose.yml
└── README.md
```

# System Architecture

The Urban Noise Governance System follows a modular client-server architecture that integrates a React frontend, a FastAPI backend, a PostgreSQL database, and a Convolutional Neural Network (CNN) for environmental sound classification.

```text
                     User
                       │
                Interacts with
                       │
                       ▼
          Frontend UI (React + Vite)
      ┌──────────────────────────────────┐
      │ • Upload Audio                   │
      │ • Dashboard                      │
      │ • Reports                        │
      │ • History                        │
      └──────────────────────────────────┘
                       │
                REST API Requests
                       │
                       ▼
             FastAPI Backend
      ┌──────────────────────────────────┐
      │ • Audio Processing (Librosa)     │
      │ • CNN Classification             │
      │ • Noise Estimation               │
      │ • Compliance Assessment          │
      │ • Risk Score Calculation         │
      │ • Governance Recommendations     │
      │ • PDF Report Generation          │
      └──────────────────────────────────┘
             │                      │
             │                      │
             ▼                      ▼
     PostgreSQL Database       CNN Model
 ┌────────────────────────┐  ┌────────────────────┐
 │ • Analysis Records     │  │ TensorFlow / Keras │
 │ • Generated Reports    │  │ Mel Spectrograms   │
 │ • Dashboard Statistics │  └────────────────────┘
 └────────────────────────┘
```

## Architecture Description

The system is organized into four major components:

### Frontend (React)

The frontend provides an intuitive user interface developed using React and Vite. Users can:

- Upload environmental noise recordings
- View prediction results
- Browse historical analyses
- Download generated reports
- Monitor system statistics through an interactive dashboard

The frontend communicates with the backend exclusively through RESTful API requests.

### Backend (FastAPI)

The FastAPI backend acts as the core application layer responsible for orchestrating the complete analysis workflow. After receiving an uploaded audio recording, it:

- Preprocesses the audio using Librosa
- Generates Mel Spectrogram features
- Performs environmental sound classification using the CNN model
- Estimates the corresponding environmental noise level
- Evaluates compliance against predefined legal noise limits
- Calculates a governance risk score
- Generates recommendations based on the analysis results
- Stores completed analyses in the database
- Produces downloadable PDF reports

### CNN Classification Model

The machine learning component is implemented using TensorFlow and Keras.

The model receives Mel Spectrogram images extracted from uploaded audio recordings and predicts one of the five environmental noise classes used throughout the application:

- Traffic
- Construction
- Entertainment
- Worship
- Ambience

The predicted class is then passed back to the FastAPI backend for governance analysis.

### PostgreSQL Database

The PostgreSQL database stores all persistent application data, including:

- Historical analysis records
- Generated reports
- Dashboard statistics

This enables users to review previous analyses and provides aggregated information for the dashboard.

# Machine Learning Pipeline

The machine learning workflow is fully reproducible using the notebooks provided in:

```
ml/notebooks
```

Run the notebooks in the following order.

## 1 Dataset Preparation

Notebook

```
09_dataset_preparation.ipynb
```

Tasks

- Load datasets
- Clean audio
- Remove invalid samples
- Resample audio
- Prepare training folders

## 2 SONYC Label Mapping

Notebook

```
10_sonyc_label_mapping.ipynb
```

Maps SONYC labels into the five classes used by the application.

Final labels:

- Traffic
- Construction
- Entertainment
- Worship
- Ambience

## 3 Transfer Learning on SONYC

Notebook

```
11_sonyc_transfer_learning.ipynb
```

This notebook

- loads the pretrained CNN
- freezes feature extraction layers
- trains the classifier using SONYC

## 4 Kigali Fine-Tuning

Notebook

```
12_kigali_transfer_learning.ipynb
```

The SONYC model is fine-tuned using locally collected Kigali environmental noise recordings to improve performance on real-world Rwandan urban environments.

Outputs

```
urban_noise_kigali.keras

label_encoder_kigali.pkl
```

## 5 CNN Architecture

Notebook

```
05_cnn_model.ipynb
```

Contains

- CNN architecture
- Training configuration
- Loss function
- Optimizer
- Evaluation

## 6 Baseline Models

Notebook

```
06_model_comparison.ipynb
```

Baseline models include

- Logistic Regression
- Random Forest
- Support Vector Machine
- CNN

All models are evaluated using the same five environmental noise classes implemented in the deployed application.

## 7 Inference Pipeline

Notebook

```
07_inference_pipeline.ipynb
```

Demonstrates

- Audio loading
- Feature extraction
- Prediction
- Confidence estimation
- Label decoding

## 8 API Demonstration

Notebook

```
08_api_demo.ipynb
```

Shows how the trained CNN integrates with the FastAPI backend.

# Datasets

Three datasets were used.

## Kigali Environmental Noise Dataset

Collected specifically for this project.

https://www.kaggle.com/datasets/davidcyubahiro/kigali-environmental-noise

## UrbanSound8K

https://urbansounddataset.weebly.com/download-urbansound8k.html

## SONYC-UST

https://zenodo.org/records/3966543

# Installation

## Clone Repository

```bash
git clone -b Post https://github.com/DavidDau/Urban-Noise-Governance-System.git

cd Urban-Noise-Governance-System
```

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Install Frontend Dependencies

```bash
cd Web_Dev/frontend

npm install
```

# Environment Variables

Backend

Create

```
Web_Dev/backend/.env
```

Example

```
DATABASE_URL=sqlite:///noise.db

SECRET_KEY=your_secret

MODEL_PATH=ml_models/urban_noise_kigali.keras

ENCODER_PATH=ml_models/label_encoder_kigali.pkl
```

# Running the Backend

```bash
cd Web_Dev/backend

uvicorn app.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

# Running the Frontend

```bash
cd Web_Dev/frontend

npm run dev
```

Frontend

```
http://localhost:5173
```

# Training the CNN

Run notebooks sequentially.

```
09_dataset_preparation.ipynb

↓

10_sonyc_label_mapping.ipynb

↓

11_sonyc_transfer_learning.ipynb

↓

12_kigali_transfer_learning.ipynb
```

The final notebook generates

```
urban_noise_kigali.keras

label_encoder_kigali.pkl
```

Copy these files into

```
Web_Dev/backend/ml_models/
```

before running the backend.

# Evaluating the CNN

The repository includes

```
06_model_comparison.ipynb
```

This notebook evaluates

- CNN
- Random Forest
- Logistic Regression
- Support Vector Machine

using the same five environmental noise classes implemented by the web application.

# Web Application

Main pages include

- Landing Page
- Analysis Page
- Results Page
- Dashboard
- History
- PDF Report Generation

# API Endpoints

| Method | Endpoint     | Description          |
| ------ | ------------ | -------------------- |
| POST   | /analysis    | Run audio analysis   |
| GET    | /dashboard   | Dashboard statistics |
| GET    | /history     | Analysis history     |
| GET    | /report/{id} | Download PDF         |
| POST   | /login       | User authentication  |

# Technologies Used

## Machine Learning

- TensorFlow
- Keras
- Librosa
- NumPy
- Scikit-learn
- Joblib

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- ReportLab

## Frontend

- React
- Vite
- CSS
- JavaScript

## Deployment

- Render
- Docker

# Reproducing Results

To reproduce the project

1. Clone the repository.
2. Download the three datasets.
3. Execute all notebooks in order.
4. Generate the trained CNN model and label encoder.
5. Copy the generated files into `Web_Dev/backend/ml_models/`.
6. Install dependencies.
7. Run the backend.
8. Run the frontend.
9. Upload an audio file through the web interface.

# Contributors

**David Cyubahiro**

Bachelor's Capstone Project

African Leadership University (ALU)

# License

This project is intended for academic and research purposes.
