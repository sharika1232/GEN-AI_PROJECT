def calculate_strength(ats_score, completeness_score):
    """
    Calculates overall resume strength.
    """

    overall = round((ats_score + completeness_score) / 2)

    if overall >= 85:
        level = "Excellent"
        color = "success"

    elif overall >= 70:
        level = "Strong"
        color = "primary"

    elif overall >= 50:
        level = "Average"
        color = "warning"

    else:
        level = "Weak"
        color = "danger"

    return {
        "score": overall,
        "level": level,
        "color": color,
    }