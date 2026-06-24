LIMITS = {
    "Residential Zone": {"Day": 55, "Night": 45},
    "Commercial Zone": {"Day": 65, "Night": 55},
    "Industrial Zone": {"Day": 75, "Night": 70},
    "Quiet Zone": {"Day": 50, "Night": 40},
    "Special Quiet Zone": {"Day": 45, "Night": 45},
    "Soundproof Venue": {"Day": 95, "Night": 95},
    "Non-Soundproof Venue": {"Day": 85, "Night": 80}
}


def check_compliance(db: float, venue: str, period: str):
    limit = LIMITS[venue][period]

    exceedance = round(db - limit, 2)

    status = "Compliant" if db <= limit else "Non-Compliant"

    return {
        "legal_limit": limit,
        "status": status,
        "exceedance": max(0, exceedance)
    }


def get_recommendation(source: str, status: str):

    if status == "Compliant":
        return "Noise levels are within acceptable limits."

    mapping = {
        "Traffic": "Assess peak-hour congestion around Kigali CBD.",
        "Construction": "Verify compliance with permitted construction hours.",
        "Entertainment": "Enforce venue noise control policies.",
        "Worship": "Review amplification and community impact.",
        "Ambience": "Investigate abnormal ambient noise levels."
    }

    return mapping.get(source, "Conduct further noise assessment.")