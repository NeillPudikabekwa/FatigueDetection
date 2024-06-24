def calculate_fatigue_index(heart_rate, sleep_duration, activity_levels):
    # Implement fatigue assessment algorithm, such as Fatigue Risk Index (FRI)
    fri = (heart_rate_variability + sleep_duration - activity_levels) / 3
    return fri
