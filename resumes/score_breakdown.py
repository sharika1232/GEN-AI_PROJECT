def generate_score_breakdown(
    ats_score,
    completeness_score
):

    if ats_score >= 90:
        formatting = 95
    elif ats_score >= 75:
        formatting = 85
    else:
        formatting = 70

    if completeness_score >= 90:
        projects = 90
        experience = 90
    elif completeness_score >= 70:
        projects = 80
        experience = 80
    else:
        projects = 65
        experience = 65

    if ats_score >= 90:
        rating = "⭐⭐⭐⭐⭐"
        level = "Excellent"

    elif ats_score >= 75:
        rating = "⭐⭐⭐⭐"
        level = "Very Good"

    elif ats_score >= 60:
        rating = "⭐⭐⭐"
        level = "Good"

    else:
        rating = "⭐⭐"
        level = "Needs Improvement"

    return {

        "skills_match": ats_score,

        "completeness": completeness_score,

        "formatting": formatting,

        "projects": projects,

        "experience": experience,

        "rating": rating,

        "level": level,

    }