from .skills import extract_skills


def normalize_skill(skill):

    return skill.lower().strip()



def predict_job_match(resume_text, job_description):


    # Extract skills

    resume_skills = extract_skills(
        resume_text
    )

    job_skills = extract_skills(
        job_description
    )


    # Normalize skills

    resume_skills = [
        normalize_skill(skill)
        for skill in resume_skills
    ]


    job_skills = [
        normalize_skill(skill)
        for skill in job_skills
    ]



    matched_skills = []

    missing_skills = []



    for skill in job_skills:


        if skill in resume_skills:

            matched_skills.append(skill)

        else:

            missing_skills.append(skill)



    # Match Percentage


    if job_skills:

        match_score = int(
            (
                len(matched_skills)
                /
                len(job_skills)
            )
            *
            100
        )

    else:

        match_score = 0




    # Interview Probability


    if match_score >= 85:

        interview = "⭐⭐⭐⭐⭐ Very High Chance"


    elif match_score >= 70:

        interview = "⭐⭐⭐⭐ High Chance"


    elif match_score >= 55:

        interview = "⭐⭐⭐ Medium Chance"


    else:

        interview = "⭐⭐ Low Chance"





    # Salary Estimate


    if match_score >= 90:

        salary = "₹12 - ₹18 LPA"


    elif match_score >= 80:

        salary = "₹8 - ₹12 LPA"


    elif match_score >= 65:

        salary = "₹5 - ₹8 LPA"


    else:

        salary = "₹3 - ₹5 LPA"






    # Improvement Suggestions


    improvement = []


    for skill in missing_skills:


        improvement.append(
            f"Learn {skill}"
        )



    if not improvement:

        improvement.append(
            "Your resume matches most required skills."
        )





    # Final Recommendation


    if match_score >= 70:


        recommendation = (
            "✅ Your profile is suitable "
            "for this job. Apply now."
        )


    else:


        recommendation = (
            "⚠ Improve missing skills "
            "before applying."
        )





    return {


        "match_score":
            match_score,


        "matched_skills":
            matched_skills,


        "missing_skills":
            missing_skills,


        "interview":
            interview,


        "salary":
            salary,


        "recommendation":
            recommendation,


        "improvement":
            improvement

    }