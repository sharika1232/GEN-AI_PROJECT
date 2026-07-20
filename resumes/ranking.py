# ---------------------------------------------
# Resume Ranking Engine
# ---------------------------------------------

def calculate_final_score(resume):

    ats_score = resume.ats_score or 0

    skills = []

    if resume.skills:
        skills = [
            skill.strip()
            for skill in resume.skills.split(",")
            if skill.strip()
        ]

    skill_score = min(len(skills) * 5, 100)

    text_length = len(resume.extracted_text or "")

    completeness = min(text_length // 50, 100)

    final_score = round(
        (ats_score * 0.6) +
        (skill_score * 0.2) +
        (completeness * 0.2),
        2
    )

    return {
        "ats_score": ats_score,
        "skill_score": skill_score,
        "completeness": completeness,
        "final_score": final_score,
    }


# ---------------------------------------------
# Rank All Resumes
# ---------------------------------------------

def rank_resumes(resumes):

    ranked = []

    for resume in resumes:

        scores = calculate_final_score(resume)

        ranked.append({
            "resume": resume,
            "ats_score": scores["ats_score"],
            "skill_score": scores["skill_score"],
            "completeness": scores["completeness"],
            "final_score": scores["final_score"],
        })

    ranked.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return ranked