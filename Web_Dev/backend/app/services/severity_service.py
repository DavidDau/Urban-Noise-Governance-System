def get_severity(db: float):

    if db < 50:
        return "Low"

    elif db < 70:
        return "Moderate"

    elif db < 85:
        return "High"

    return "Critical"