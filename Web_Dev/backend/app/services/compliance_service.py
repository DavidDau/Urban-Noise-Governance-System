LIMITS = {
    "Residential Zone": {"Day": 55, "Night": 45},
    "Commercial Zone": {"Day": 65, "Night": 55},
    "Industrial Zone": {"Day": 75, "Night": 70},
    "Quiet Zone": {"Day": 50, "Night": 40},
    "Special Quiet Zone": {"Day": 45, "Night": 45},
    "Soundproof Venue": {"Day": 95, "Night": 95},
    "Non-Soundproof Venue": {"Day": 85, "Night": 80},
}


def get_legal_limit(venue: str, period: str) -> float:
    """
    Returns the legal noise limit for the selected venue and time period.
    """
    return LIMITS.get(venue, LIMITS["Residential Zone"]).get(period, 55)


def check_compliance(db: float, venue: str, period: str):
    """
    Checks whether the measured noise complies with the legal limit.
    """

    legal_limit = get_legal_limit(venue, period)

    exceedance = round(max(0, db - legal_limit), 2)

    status = "Compliant" if db <= legal_limit else "Non-Compliant"

    return {
        "legal_limit": legal_limit,
        "status": status,
        "exceedance": exceedance,
    }


def get_recommendation(source: str, status: str):
    """
    Returns a recommendation based on the predicted noise source.
    """

    if status == "Compliant":
        return "Noise levels are within acceptable limits."

    recommendations = {
        "Traffic": "Assess peak-hour traffic congestion and consider traffic calming measures.",
        "Construction": "Verify compliance with permitted construction hours and install temporary acoustic barriers.",
        "Entertainment": "Enforce venue noise control policies and reduce loudspeaker volume.",
        "Worship": "Review amplification levels and engage nearby residents.",
        "Ambience": "Investigate the surrounding area for unusual environmental noise sources.",
    }

    return recommendations.get(
        source,
        "Conduct further environmental noise assessment."
    )