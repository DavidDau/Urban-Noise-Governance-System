def get_time_period(
    recording_time
):
    """
    Convert HH:MM to Day/Night
    """

    hour = int(
        recording_time.split(":")[0]
    )

    if 6 <= hour < 21:
        return "Day"

    return "Night"
