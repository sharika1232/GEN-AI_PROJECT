JOB_KEYWORDS = {

    "Python Developer": [
        "python",
        "django",
        "flask",
        "rest api",
        "sql",
        "git",
        "github",
        "docker",
        "aws",
        "linux"
    ],

    "Java Developer": [
        "java",
        "spring boot",
        "hibernate",
        "mysql",
        "rest api",
        "git",
        "docker",
        "aws"
    ],

    "Frontend Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "bootstrap",
        "tailwind css",
        "git"
    ],

    "Data Scientist": [
        "python",
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn",
        "tensorflow",
        "sql"
    ]
}


def optimize_keywords(resume_skills, job_role):

    required = []

    for role, keywords in JOB_KEYWORDS.items():
        if role.lower() == job_role.lower():
            required = keywords
            break

    resume = [s.lower() for s in resume_skills]

    matched = []
    missing = []

    for skill in required:

        if skill.lower() in resume:
            matched.append(skill)

        else:
            missing.append(skill)

    if len(required) == 0:
        percentage = 0
    else:
        percentage = round(
            len(matched) / len(required) * 100
        )

    return {

        "job_role": job_role,

        "matched_keywords": matched,

        "missing_keywords": missing,

        "match_percentage": percentage

    }