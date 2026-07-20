def recommend_jobs(skills):

    skills = set(skill.lower() for skill in skills)

    jobs = []

    if "python" in skills:
        jobs.append("Python Developer")

    if "django" in skills:
        jobs.append("Django Developer")

    if "flask" in skills:
        jobs.append("Backend Developer")

    if {"html", "css", "javascript"}.issubset(skills):
        jobs.append("Frontend Developer")

    if {"python", "django", "javascript"}.issubset(skills):
        jobs.append("Full Stack Developer")

    if {"machine learning", "deep learning"}.issubset(skills):
        jobs.append("AI / Machine Learning Engineer")

    if {"sql", "mysql"}.issubset(skills):
        jobs.append("Database Developer")

    if not jobs:
        jobs.append("Software Developer")

    return jobs