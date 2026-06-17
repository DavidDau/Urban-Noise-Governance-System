def get_recommendation(
    source,
    status
):

    if status == "Compliant":
        return (
            "Noise levels are within acceptable limits."
        )

    recommendations = {

        "Traffic": (
            "Assess peak-hour congestion around Kigali CBD."
        ),

        "Construction": (
            "Verify compliance with Rwanda noise regulations and operating hours."
        ),

        "Entertainment": (
            "Assess venue compliance with local entertainment noise limits."
        ),

        "Worship": (
            "Review amplification practices and community noise mitigation measures."
        ),

        "Ambience": (
            "Investigate unusual ambient noise conditions."
        )
    }

    return recommendations.get(
        source,
        "Conduct further noise assessment."
    )