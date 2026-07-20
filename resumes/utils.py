import pdfplumber
from docx import Document


# ==========================================================
# PDF TEXT EXTRACTION
# ==========================================================

def extract_text_from_pdf(pdf_path):
    """
    Extract text from PDF resume.
    """

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text



# ==========================================================
# DOCX TEXT EXTRACTION
# ==========================================================

def extract_text_from_docx(docx_path):
    """
    Extract text from DOCX resume.
    """

    document = Document(docx_path)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text



# ==========================================================
# RESUME TEXT EXTRACTION HANDLER
# ==========================================================

def extract_resume_text(file_path):
    """
    Detect file type and extract resume text.
    """

    if file_path.lower().endswith(".pdf"):

        return extract_text_from_pdf(file_path)


    elif file_path.lower().endswith(".docx"):

        return extract_text_from_docx(file_path)


    else:

        return ""



# ==========================================================
# AI COVER LETTER GENERATOR
# ==========================================================

# ==========================================================
# AI COVER LETTER GENERATOR
# ==========================================================

def generate_cover_letter(
    candidate_name,
    company_name,
    job_role,
    skills,
    job_description
):

    skills_text = ", ".join(skills)


    cover_letter = f"""
Dear Hiring Manager at {company_name},

I am {candidate_name}, and I am applying for the 
{job_role} position at {company_name}.

My technical skills include:

{skills_text}


I have developed practical experience through projects,
problem-solving, and continuous learning.

The job requirements match my technical background,
and I believe my skills will allow me to contribute
effectively to your development team.


I am excited about this opportunity and look forward
to contributing my knowledge and growing with your organization.


Thank you for considering my application.


Sincerely,

{candidate_name}
"""

    return cover_letter.strip()