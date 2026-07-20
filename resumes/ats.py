def calculate_ats_score(resume_skills, job_skills):
    """
    Compare resume skills with job skills and calculate ATS score.
    """

    # Convert to lowercase for comparison
    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    # Find matched and missing skills
    matched_skills = sorted(list(resume_set & job_set))
    missing_skills = sorted(list(job_set - resume_set))

    # Calculate ATS score
    if len(job_set) == 0:
        score = 0
    else:
        score = round((len(matched_skills) / len(job_set)) * 100, 2)

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }