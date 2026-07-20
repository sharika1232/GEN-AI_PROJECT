def improve_resume(missing_skills, ats_score):
    """
    Generates AI-like resume improvement suggestions.
    """

    improvements = []

    if ats_score >= 90:
        improvements.append(
            "Excellent resume. Only minor improvements are recommended."
        )

    elif ats_score >= 70:
        improvements.append(
            "Your resume is good, but adding more job-specific keywords will improve ATS performance."
        )

    else:
        improvements.append(
            "Your resume requires significant improvements to pass ATS filters."
        )

    if missing_skills:
        improvements.append(
            "Add the following missing skills if you possess them:"
        )

        for skill in missing_skills:
            improvements.append(f"• {skill}")

    improvements.extend([
        "Write a strong professional summary.",
        "Quantify achievements using numbers and percentages.",
        "Include relevant certifications.",
        "Highlight projects with technologies used.",
        "Use action verbs like Developed, Designed, Implemented and Optimized.",
        "Keep formatting clean and ATS-friendly.",
        "Avoid tables, images and excessive graphics.",
    ])

    return improvements