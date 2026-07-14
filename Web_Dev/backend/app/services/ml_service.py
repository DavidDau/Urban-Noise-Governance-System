import os
import time

import joblib
import librosa
import numpy as np
from tensorflow.keras.models import load_model

def predict_source(audio_path: str):

    total_start = time.perf_counter()

    print("========== ML START ==========")

    features = preprocess_audio(audio_path)

    print("Input shape:", features.shape)

    output = MODEL(
        features,
        training=False
    )

    predictions = output.numpy()

    predicted_index = int(np.argmax(predictions))

    confidence = float(
        np.max(predictions)
    )

    label = ENCODER.inverse_transform(
        [predicted_index]
    )[0]

    label_normalized = label.strip().lower()

    mapping = {
        "traffic": "Traffic",
        "construction": "Construction",
        "entertainment": "Entertainment",
        "worship": "Worship",
        "ambience": "Ambience",
        "normal_ambience": "Ambience",
    }

    label = mapping.get(
        label_normalized,
        label.capitalize()
    )

    print(
        f"Prediction: {label}"
    )

    print(
        f"Confidence: {confidence:.4f}"
    )

    print(
        f"ML time: {time.perf_counter() - total_start:.2f}s"
    )

    print("========== ML END ==========")

    return label, confidence