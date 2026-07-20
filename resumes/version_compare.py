def compare_versions(old_resume, new_resume):

    comparison = {}

    comparison["old_title"] = old_resume.title
    comparison["new_title"] = new_resume.title

    comparison["old_score"] = old_resume.ats_score
    comparison["new_score"] = new_resume.ats_score

    old_skills = []

    if old_resume.skills:
        old_skills = [
            s.strip()
            for s in old_resume.skills.split(",")
            if s.strip()
        ]

    new_skills = []

    if new_resume.skills:
        new_skills = [
            s.strip()
            for s in new_resume.skills.split(",")
            if s.strip()
        ]

    comparison["old_skill_count"] = len(old_skills)
    comparison["new_skill_count"] = len(new_skills)

    comparison["new_skills_added"] = list(
        set(new_skills) - set(old_skills)
    )

    comparison["skills_removed"] = list(
        set(old_skills) - set(new_skills)
    )

    comparison["score_difference"] = (
        new_resume.ats_score -
        old_resume.ats_score
    )

    if comparison["score_difference"] > 0:
        comparison["winner"] = "Latest Resume"

    elif comparison["score_difference"] < 0:
        comparison["winner"] = "Previous Resume"

    else:
        comparison["winner"] = "Tie"

    return comparison