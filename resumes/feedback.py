def generate_feedback(score, matched_skills, missing_skills):
    """
    Generate AI-like resume feedback based on ATS score and skills.
    """

    feedback = {}

    # -----------------------------
    # Overall Evaluation
    # -----------------------------
    if score >= 85:
        feedback["overall"] = (
            "Excellent resume! Your resume is highly compatible with the selected job description."
        )

    elif score >= 70:
        feedback["overall"] = (
            "Good resume. You have a solid foundation, but adding a few missing skills could significantly improve your ATS score."
        )

    elif score >= 50:
        feedback["overall"] = (
            "Average resume. Several important skills are missing. Updating your resume will improve your chances."
        )

    else:
        feedback["overall"] = (
            "Your resume needs significant improvement to match the selected job role."
        )

    # -----------------------------
    # Strengths
    # -----------------------------
    strengths = []

    if matched_skills:
        strengths.append(
            f"Matched {len(matched_skills)} required skill(s)."
        )

    if score >= 80:
        strengths.append(
            "Strong ATS compatibility."
        )

    if score >= 60:
        strengths.append(
            "Good technical profile."
        )

    feedback["strengths"] = strengths

    # -----------------------------
    # Improvements
    # -----------------------------
    improvements = []

    for skill in missing_skills:
        improvements.append(
            f"Consider adding '{skill}' to your resume if you have experience with it."
        )

    improvements.append(
        "Use measurable achievements (e.g., 'Improved API performance by 30%')."
    )

    improvements.append(
        "Include impactful projects with clear outcomes."
    )

    improvements.append(
        "Tailor your resume for each job application."
    )

    feedback["improvements"] = improvements

    # -----------------------------
    # Interview Readiness
    # -----------------------------
    if score >= 85:
        feedback["rating"] = "★★★★★"

    elif score >= 70:
        feedback["rating"] = "★★★★☆"

    elif score >= 50:
        feedback["rating"] = "★★★☆☆"

    else:
        feedback["rating"] = "★★☆☆☆"

    return feedback