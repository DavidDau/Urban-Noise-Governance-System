def calculate_risk_score(
    severity: str,
    status: str
):
    """
    Calculates the environmental risk score and risk level.
    """

    severity_scores = {
        "Low": 10,
        "Moderate": 30,
        "High": 60,
        "Critical": 90,
    }

    score = severity_scores.get(severity, 0)

    if status == "Non-Compliant":
        score += 10

    score = min(score, 100)

    if score < 25:
        level = "Low Risk"

    elif score < 50:
        level = "Moderate Risk"

    elif score < 75:
        level = "High Risk"

    else:
        level = "Critical Risk"

    return {
        "risk_score": score,
        "risk_level": level,
    }