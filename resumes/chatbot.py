from .career import recommend_jobs
from .career_roadmap import generate_career_roadmap
from .learning_resources import get_learning_resources
from .ats import calculate_ats_score
from .skills import extract_skills


def get_chatbot_response(question, resume):

    print("========== CHATBOT FUNCTION STARTED ==========")
    print("QUESTION =", question)

    question = question.lower().strip()


    # -----------------------------
    # Resume Skills
    # -----------------------------

    resume_skills = []

    if resume.skills:

        resume_skills = [
            skill.strip()
            for skill in resume.skills.split(",")
            if skill.strip()
        ]

    print("=" * 50)
    print("Resume Skills:", resume.skills)
    print("Resume Skills List:", resume_skills)
    print("=" * 50)


    job_skills = extract_skills(
        resume.job_description
    )


    ats = calculate_ats_score(
        resume_skills,
        job_skills
    )


    roadmap = generate_career_roadmap(
        resume_skills
    )

    print("Career Roadmap:", roadmap)

    resources = get_learning_resources(
        resume_skills
    )


# -----------------------------
# Greeting
# -----------------------------

    words = question.split()

    if any(word in words for word in [
        "hi",
        "hello",
        "hey"
    ]):

        return (
            "Hello! 👋\n\n"
            "I'm your AI Resume Assistant.\n"
            "Ask me anything about your resume."
        )



    # -----------------------------
    # ATS Score
    # -----------------------------

    elif any(word in question for word in [
        "ats",
        "score"
    ]):

        return (

            f"ATS Score : {resume.ats_score}%\n\n"

            f"Matched Skills:\n"
            f"{', '.join(ats['matched_skills']) if ats['matched_skills'] else 'None'}\n\n"

            f"Missing Skills:\n"
            f"{', '.join(ats['missing_skills']) if ats['missing_skills'] else 'None'}"

        )



    # -----------------------------
    # Missing Skills
    # -----------------------------

    elif any(phrase in question for phrase in [
        "missing",
        "missing skills",
        "missing keywords",
        "keywords",
        "keyword",
        "what skills are missing",
        "which skills are missing",
        "skills missing",
        "what am i missing"
    ]):


        if ats["missing_skills"]:

            return (

                "Missing Skills:\n\n"
                +
                "\n".join(
                    f"• {skill}"
                    for skill in ats["missing_skills"]
                )

            )


        return "Excellent! No important skills are missing."



    # -----------------------------
    # Resume Improvement
    # -----------------------------

    elif any(word in question for word in [
        "improve",
        "improvement",
        "better"
    ]):


        suggestions = []


        if resume.ats_score < 80:

            suggestions.append(
                "• Improve ATS keyword matching"
            )


        if len(resume_skills) < 8:

            suggestions.append(
                "• Add more technical skills"
            )


        suggestions.extend([

            "• Add measurable achievements",

            "• Add GitHub projects",

            "• Add LinkedIn profile",

            "• Add certifications",

            "• Mention project technologies"

        ])


        return "\n".join(suggestions)



    # -----------------------------
    # Jobs
    # -----------------------------

    elif any(phrase in question for phrase in [
        "job",
        "jobs",
        "role",
        "roles",
        "career",
        "career option",
        "career options",
        "suitable job",
        "suitable jobs",
        "which jobs",
        "what jobs",
        "job recommendation",
        "recommended jobs",
        "best job",
        "job for me"
    ]):

        jobs = recommend_jobs(resume_skills)

        print("Recommended Jobs:", jobs)

        if jobs:

            return (
                "Recommended Jobs:\n\n"
                +
                "\n".join(
                    f"• {job}"
                        for job in jobs
                )
            )
        

        return "No suitable jobs found."




# -----------------------------
# Projects
# -----------------------------

    elif any(phrase in question for phrase in [
        "project",
        "projects",
        "build",
        "create project",
        "project ideas",
        "recommended projects",
        "which projects",
        "what projects"
    ]):

        if roadmap.get("projects", []):

            return (
                "Recommended Projects:\n\n"
                +
                "\n".join(
                    f"• {p}"
                    for p in roadmap["projects"]
                )
            )

        return "No project recommendations available."




# -----------------------------
# Certifications
# -----------------------------

    elif any(phrase in question for phrase in [
        "certification",
        "certifications",
        "certificate",
        "certificates",
        "course",
        "courses",
        "certified",
        "which certification",
        "what certification",
        "recommended certification"
    ]):

        if roadmap.get("certifications", []):

            return (
                "Recommended Certifications:\n\n"
                +
                "\n".join(
                    f"• {c}"
                    for c in roadmap["certifications"]
                )
            )

        return "No certification recommendations available."




    # -----------------------------
    # Career Roadmap
    # -----------------------------

    elif any(word in question for word in [
        "roadmap",
        "career roadmap",
        "career path",
        "growth plan",
        "future"
    ]):

        return (

            f"Career Goal:\n"
            f"{roadmap['career_goal']}\n\n"

            f"Missing Skills:\n"
            f"{', '.join(roadmap['missing_skills']) if roadmap['missing_skills'] else 'None'}\n\n"

            f"Projects:\n"
            +
            "\n".join(roadmap["projects"])
            +
            "\n\n"

            f"Certifications:\n"
            +
            "\n".join(roadmap["certifications"])
            +
            "\n\n"

            f"Monthly Plan:\n"
            +
            "\n".join(roadmap["monthly_plan"])

        )



    # -----------------------------
    # Learning Resources
    # -----------------------------

    elif any(word in question for word in [
        "learn",
        "learning",
        "resource",
        "resources"
    ]):


        return (

            "Learning Resources:\n\n"
            +
            "\n".join(
                f"• {r}"
                for r in resources
            )

        )



    # -----------------------------
    # Skills
    # -----------------------------

    elif "skill" in question:


        return (

            "Your detected skills:\n\n"
            +
            resume.skills

        )



    # -----------------------------
    # Cover Letter
    # -----------------------------

    elif "cover letter" in question:


        return (

            resume.cover_letter
            if getattr(resume,"cover_letter",None)
            else
            "No cover letter generated."

        )



    # -----------------------------
    # Summary
    # -----------------------------

    elif "summary" in question:


        return (

            f"Resume Title : {resume.title}\n"
            f"ATS Score : {resume.ats_score}%\n"
            f"Skills : {resume.skills}"

        )



    return (

        "I can help with:\n\n"
        "• ATS Score\n"
        "• Missing Skills\n"
        "• Resume Improvement\n"
        "• Jobs\n"
        "• Projects\n"
        "• Certifications\n"
        "• Career Roadmap\n"
        "• Learning Resources\n"
        "• Cover Letter"

    )