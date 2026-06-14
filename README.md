Machine Learning-Based Context-Aware Urban Acoustic Event Classification for Smart Noise Governance
Urban Noise Governance System

GitHub Repository: https://github.com/DavidDau/Urban-Noise-Governance-System

Overview

This capstone project explores the use of Machine Learning (ML) for contextual urban noise analysis. Traditional noise monitoring systems primarily measure sound intensity in decibels (dB) but often fail to identify the source of the noise. As a result, decision-makers lack sufficient contextual information to determine appropriate mitigation strategies.

The proposed Urban Noise Governance System addresses this limitation by automatically classifying urban acoustic events into meaningful categories such as Traffic, Construction, Entertainment, and Ambience. By combining audio signal processing and machine learning techniques, the system provides contextual acoustic intelligence that supports smarter noise governance and informed decision-making.

Problem Statement

Urban noise pollution is becoming an increasingly significant environmental and public health challenge, particularly in rapidly growing cities. Existing approaches to noise management rely heavily on decibel measurements, manual inspections, and public complaints. While these methods can determine whether noise exceeds legal thresholds, they cannot automatically identify the source of the noise.

This limitation creates challenges for venue owners, businesses, local authorities, and urban planners who require contextual information to make informed noise management decisions.

This project seeks to bridge this gap by developing a machine learning-based acoustic event classification system capable of identifying urban sound sources from audio recordings.

Project Objectives
Main Objective

To develop a machine learning-based system that classifies urban acoustic events and provides contextual acoustic intelligence for improved urban noise governance.

Specific Objectives
Analyze and prepare urban sound datasets for machine learning classification.
Develop and compare multiple machine learning models for acoustic event classification.
Evaluate model performance using standard classification metrics.
Develop a prototype API capable of receiving audio files and returning classification results.
Demonstrate the feasibility of contextual noise analysis for smart urban management.
Target Sound Categories

The MVP classifies audio recordings into the following categories:

Traffic
Construction
Entertainment
Ambience

These categories were created by grouping UrbanSound8K classes into broader urban noise governance categories.

Datasets
Current Dataset
UrbanSound8K

The current implementation uses the UrbanSound8K dataset for data preprocessing, feature extraction, model training, and evaluation.

Future Datasets

The following datasets are planned for future experimentation and model enhancement:

ESC-50
SONYC Urban Sound Dataset
Local Kigali Audio Dataset
Technology Stack
Machine Learning
Python
TensorFlow
Scikit-learn
Librosa
NumPy
Pandas
Data Visualization
Matplotlib
Seaborn
API Development
FastAPI
Swagger UI
Database (Future Work)
PostgreSQL
Frontend (Future Work)
HTML
CSS
Bootstrap
Implemented Machine Learning Workflow

The machine learning pipeline was implemented through the following notebooks:

Audio Preprocessing
Feature Extraction
Dataset Creation
Baseline Model Development
CNN Model Training
Model Comparison
Inference Pipeline
API Demonstration
Feature Extraction

The project uses:

Mel Spectrograms
MFCCs
Chroma Features
Spectral Centroid
Spectral Rolloff
Zero Crossing Rate
Implemented Models
Random Forest Classifier

Used as the baseline machine learning model.

Convolutional Neural Network (CNN)

Used as the primary deep learning model for spectrogram-based acoustic event classification.

Support Vector Machine (SVM)

Considered during model selection but not included in the MVP implementation.

Evaluation Metrics

The models were evaluated using:

Accuracy
Precision
Recall
F1 Score
Confusion Matrix
Model Results
Random Forest Baseline
Metric Score
Accuracy 0.82
Precision 0.81
Recall 0.80
F1 Score 0.80
CNN Model
Metric Score
Accuracy 0.92
Precision 0.92
Recall 0.92
F1 Score 0.92

The CNN achieved the highest overall performance and was selected as the final model for deployment.

API Prototype

The MVP includes a FastAPI deployment prototype demonstrating how the trained CNN model can be exposed as a prediction service.

Endpoint

POST /predict

Input

Audio file (.wav)

Example Response
{
"prediction": "Construction",
"confidence": 0.92
}

Swagger UI documentation is available through:

http://localhost:8000/docs

Designs and Mockups

The project includes mockups and interface designs demonstrating:

Landing Page
Audio Upload Interface
Classification Results Dashboard
Historical Reports Page
API Swagger UI

Screenshots and design assets are stored in the project documentation folder.

Deployment Plan
MVP Phase
Local development environment
FastAPI backend
Swagger UI testing
Deployment Architecture

User
↓
API Request
↓
FastAPI Backend
↓
CNN Model
↓
Prediction Response

Future Deployment

User
↓
Web Application
↓
FastAPI Backend
↓
Machine Learning Model
↓
PostgreSQL Database

Potential hosting platforms:

Render
Railway
AWS
Azure
Project Structure
Urban-Noise-Governance-System/

README.md

ml/
├── notebooks/
├── preprocessing/
├── saved_models/
└── data/

deployment/
├── app.py
└── requirements.txt

docs/
└── screenshots/
Expected Outcomes

The project demonstrates that machine learning can provide contextual understanding of urban noise sources beyond traditional decibel measurements.

The system supports:

Urban sound source identification
Context-aware noise analysis
Improved decision-making for noise management
Future integration into smart city initiatives
Installation

Clone the repository:

git clone https://github.com/DavidDau/Urban-Noise-Governance-System.git

Navigate to the project directory:

cd Urban-Noise-Governance-System

Create a virtual environment:

python -m venv .venv

Activate the environment:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the FastAPI server:

uvicorn app:app --reload
Author

David Cyubahiro

Bachelor of Science in Machine Learning

African Leadership University (ALU)

Capstone Project – 2026
