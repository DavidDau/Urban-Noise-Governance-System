from venue_limits import LIMITS


def check_compliance(
    estimated_db,
    venue_type,
    time_period
):
    """
    Compare estimated dB against Rwanda limits.
    """

    legal_limit = LIMITS[venue_type][time_period]

    exceedance = round(
        estimated_db - legal_limit,
        2
    )

    status = (
        "Compliant"
        if estimated_db <= legal_limit
        else "Non-Compliant"
    )

    return {
        "legal_limit": legal_limit,
        "status": status,
        "exceedance": max(0, exceedance)
    }
