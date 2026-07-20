CAREER_PATHS = {

    "Python Backend Developer": {
        "keywords": ["python", "django", "flask"],
        "required_skills": [
            "python",
            "django",
            "django rest framework",
            "rest api",
            "sql",
            "git",
            "docker",
            "aws"
        ],
        "projects": [
            "Hospital Management System",
            "E-Commerce Website",
            "AI Resume Screener",
            "Blog REST API"
        ],
        "certifications": [
            "Python Programming",
            "Django",
            "AWS Cloud Practitioner"
        ]
    },

    "Java Full Stack Developer": {
        "keywords": ["java", "spring", "spring boot"],
        "required_skills": [
            "java",
            "spring boot",
            "hibernate",
            "mysql",
            "rest api",
            "docker",
            "aws"
        ],
        "projects": [
            "Banking System",
            "Library Management System",
            "Employee Portal"
        ],
        "certifications": [
            "Oracle Java",
            "Spring Boot"
        ]
    },

    "Data Scientist": {
        "keywords": [
            "pandas",
            "numpy",
            "machine learning",
            "tensorflow",
            "scikit-learn"
        ],
        "required_skills": [
            "python",
            "numpy",
            "pandas",
            "matplotlib",
            "scikit-learn",
            "tensorflow",
            "sql"
        ],
        "projects": [
            "House Price Prediction",
            "Customer Churn Prediction",
            "Disease Prediction"
        ],
        "certifications": [
            "Google Data Analytics",
            "IBM Data Science"
        ]
    },

    "Frontend Developer": {
        "keywords": [
            "html",
            "css",
            "javascript",
            "react"
        ],
        "required_skills": [
            "html",
            "css",
            "javascript",
            "react",
            "redux",
            "bootstrap",
            "git"
        ],
        "projects": [
            "Portfolio Website",
            "Netflix Clone",
            "Weather App"
        ],
        "certifications": [
            "Meta Front-End Developer"
        ]
    },

    "DevOps Engineer": {
        "keywords": [
            "docker",
            "kubernetes",
            "aws"
        ],
        "required_skills": [
            "linux",
            "docker",
            "kubernetes",
            "aws",
            "jenkins",
            "terraform"
        ],
        "projects": [
            "CI/CD Pipeline",
            "Docker Deployment",
            "Kubernetes Cluster"
        ],
        "certifications": [
            "AWS Solutions Architect",
            "Docker Certified Associate"
        ]
    }
}

def generate_career_roadmap(resume_skills):

    skills = [skill.lower() for skill in resume_skills]

    best_match = None
    highest_score = 0

    for career, details in CAREER_PATHS.items():

        score = len(
            set(skills) &
            set(details["keywords"])
        )

        if score > highest_score:
            highest_score = score
            best_match = career

    if not best_match:

        return {
            "career_goal": "Software Developer",
            "missing_skills": [],
            "projects": [],
            "certifications": [],
            "monthly_plan": [
                "Improve programming fundamentals.",
                "Learn Git & GitHub.",
                "Build portfolio projects.",
                "Practice DSA.",
                "Prepare for interviews."
            ]
        }

    details = CAREER_PATHS[best_match]

    missing = [
        skill
        for skill in details["required_skills"]
        if skill not in skills
    ]

    monthly_plan = [
        f"Month 1: Learn {missing[0]}" if len(missing) > 0 else "Revise current skills.",
        f"Month 2: Learn {missing[1]}" if len(missing) > 1 else "Build projects.",
        f"Month 3: Learn {missing[2]}" if len(missing) > 2 else "Practice interviews.",
        "Month 4: Build an advanced project.",
        "Month 5: Prepare for placements.",
        "Month 6: Apply for jobs and internships."
    ]

    return {

        "career_goal": best_match,

        "missing_skills": missing,

        "projects": details["projects"],

        "certifications": details["certifications"],

        "monthly_plan": monthly_plan
    }