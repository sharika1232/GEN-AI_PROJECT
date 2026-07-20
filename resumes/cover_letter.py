def generate_cover_letter(
    candidate_name,
    job_role,
    skills,
    company_name,
    job_description,
):

    if isinstance(skills, list):
        skills = ", ".join(skills)

    if not company_name:
        company_name = "Your Company"

    if not job_role:
        job_role = "Software Developer"

    if not job_description:
        job_description = "No job description provided."

    return f"""
Dear Hiring Manager,

I am excited to apply for the position of {job_role} at {company_name}.

My name is {candidate_name}, and I have strong knowledge in {skills}. Through academic and personal projects, I have developed practical experience in software development, problem-solving, debugging, teamwork, and building real-world applications.

After reviewing your job requirements, I believe my technical skills and enthusiasm for continuous learning make me a suitable candidate for this role.

Job Description:
{job_description[:400]}

I am eager to contribute to your organization, learn from experienced professionals, and help deliver high-quality software solutions. I am confident that my dedication and willingness to learn will allow me to become a valuable member of your team.

Thank you for taking the time to review my application. I would welcome the opportunity to discuss how my skills and passion align with your organization's goals.

Sincerely,

{candidate_name}
"""