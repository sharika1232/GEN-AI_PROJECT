import re

try:
    import spacy
except ImportError:  # pragma: no cover - optional dependency
    spacy = None

# Load spaCy English model if available
nlp = None
if spacy is not None:
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:  # pragma: no cover - model may be missing
        nlp = None

# =====================================================
# TECHNICAL SKILLS DATABASE
# =====================================================

SKILLS = [

    # --------------------------
    # Programming Languages
    # --------------------------
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "php",
    "ruby",
    "go",
    "rust",
    "swift",
    "kotlin",
    "scala",
    "r",

    # --------------------------
    # Frontend
    # --------------------------
    "html",
    "css",
    "bootstrap",
    "tailwind css",
    "sass",
    "react",
    "angular",
    "vue",
    "next.js",
    "jquery",

    # --------------------------
    # Backend
    # --------------------------
    "django",
    "flask",
    "fastapi",
    "spring",
    "spring boot",
    "hibernate",
    "node.js",
    "express",
    "laravel",
    "asp.net",

    # --------------------------
    # Databases
    # --------------------------
    "sql",
    "mysql",
    "postgresql",
    "oracle",
    "sqlite",
    "mongodb",
    "redis",
    "firebase",

    # --------------------------
    # Version Control
    # --------------------------
    "git",
    "github",
    "gitlab",
    "bitbucket",

    # --------------------------
    # DevOps & Cloud
    # --------------------------
    "docker",
    "kubernetes",
    "jenkins",
    "terraform",
    "ansible",
    "aws",
    "azure",
    "gcp",

    # --------------------------
    # AI / Machine Learning
    # --------------------------
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "tensorflow",
    "keras",
    "pytorch",
    "opencv",
    "computer vision",
    "natural language processing",
    "nlp",

    # --------------------------
    # Data Science
    # --------------------------
    "pandas",
    "numpy",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "scipy",

    # --------------------------
    # Data Analytics
    # --------------------------
    "power bi",
    "tableau",
    "excel",

    # --------------------------
    # Mobile Development
    # --------------------------
    "android",
    "flutter",
    "react native",
    "xamarin",

    # --------------------------
    # Testing
    # --------------------------
    "selenium",
    "pytest",
    "junit",
    "postman",

    # --------------------------
    # Cyber Security
    # --------------------------
    "cyber security",
    "penetration testing",
    "ethical hacking",
    "network security",
    "owasp",

    # --------------------------
    # CS Fundamentals
    # --------------------------
    "data structures",
    "algorithms",
    "operating systems",
    "computer networks",
    "dbms",
    "oops",

    # --------------------------
    # APIs
    # --------------------------
    "rest api",
    "graphql",
]


# =====================================================
# SKILL EXTRACTION
# =====================================================

def extract_skills(text):
    """
    Extract technical skills from resume text or job description.
    Uses regex word boundaries to avoid false matches like
    'c' inside 'computer' or 'r' inside 'developer'.
    """

    if not text:
        return []

    text = text.lower()

    # Process text with spaCy when available; otherwise fall back to raw text
    if nlp is not None:
        doc = nlp(text)
        clean_text = doc.text
    else:
        clean_text = text

    found_skills = set()

    for skill in SKILLS:

        skill_lower = skill.lower()

        # Special handling for single-letter languages
        if skill_lower in ["c", "r"]:
            pattern = rf"(?<![a-zA-Z0-9]){re.escape(skill_lower)}(?![a-zA-Z0-9])"
        else:
            pattern = rf"\b{re.escape(skill_lower)}\b"

        if re.search(pattern, clean_text):
            found_skills.add(skill)

    return sorted(found_skills)