def get_severity(db: float) -> str:
    """
    Classifies the noise severity based on the estimated decibel level.
    """

    if db < 50:
        return "Low"

    elif db < 70:
        return "Moderate"

    elif db < 85:
        return "High"

    return "Critical"