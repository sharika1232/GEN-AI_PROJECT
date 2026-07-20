from difflib import SequenceMatcher


def calculate_similarity(resume_text, job_description):
    """
    Calculates similarity percentage between
    resume text and job description.
    """

    similarity = SequenceMatcher(
        None,
        resume_text.lower(),
        job_description.lower()
    ).ratio()

    percentage = round(similarity * 100)

    if percentage >= 80:
        level = "Excellent Match"
        color = "success"

    elif percentage >= 60:
        level = "Good Match"
        color = "primary"

    elif percentage >= 40:
        level = "Average Match"
        color = "warning"

    else:
        level = "Poor Match"
        color = "danger"

    return {
        "percentage": percentage,
        "level": level,
        "color": color,
    }