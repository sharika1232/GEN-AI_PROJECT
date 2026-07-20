# ==========================================================
# AI Interview Question Database
# ==========================================================

from unittest import result


interview_questions = {

    "python": [
        "What are decorators?",
        "What is list comprehension?",
        "Difference between list and tuple?",
        "Explain generators.",
        "What are lambda functions?"
    ],

    "java": [
        "What is JVM?",
        "Difference between JDK and JRE?",
        "Explain inheritance.",
        "What is polymorphism?",
        "What is exception handling?"
    ],

    "django": [
        "What is MVT architecture?",
        "Explain Django ORM.",
        "What are migrations?",
        "Difference between GET and POST?",
        "What are middleware?"
    ],

    "flask": [
        "What is Flask?",
        "Explain Blueprints.",
        "What is Jinja2?",
        "How do you handle sessions?",
        "Difference between Flask and Django?"
    ],

    "sql": [
        "What is normalization?",
        "Difference between WHERE and HAVING?",
        "Explain INNER JOIN.",
        "Difference between DELETE, DROP and TRUNCATE?",
        "What is a Primary Key?"
    ],

    "mysql": [
        "What is MySQL?",
        "Difference between CHAR and VARCHAR?",
        "Explain indexing.",
        "What is a Foreign Key?",
        "Explain transactions."
    ],

    "html": [
        "What are semantic tags?",
        "Difference between div and span?",
        "Explain forms.",
        "What is HTML5?",
        "What are meta tags?"
    ],

    "css": [
        "Difference between Flexbox and Grid?",
        "Explain CSS Box Model.",
        "What is responsive design?",
        "What is media query?",
        "Difference between relative and absolute positioning?"
    ],

    "javascript": [
        "Difference between var, let and const?",
        "Explain promises.",
        "What is event bubbling?",
        "What is closure?",
        "Difference between == and ===?"
    ],

    "git": [
        "What is Git?",
        "Difference between Git Pull and Git Fetch?",
        "Explain Git Merge.",
        "What is Git Rebase?",
        "What is a branch?"
    ],

    "github": [
        "What is GitHub?",
        "What is Pull Request?",
        "Difference between Fork and Clone?",
        "Explain GitHub Actions.",
        "How do you resolve merge conflicts?"
    ],

    "docker": [
        "What is Docker?",
        "Difference between Image and Container?",
        "Explain Docker Compose.",
        "What is Dockerfile?",
        "Why use Docker?"
    ],

    "aws": [
        "What is AWS?",
        "Explain EC2.",
        "What is Amazon S3?",
        "Difference between EC2 and Lambda?",
        "What is IAM?"
    ],

    "rest api": [
        "What is REST API?",
        "Difference between GET and POST?",
        "What are HTTP status codes?",
        "Explain PUT and PATCH.",
        "What is JSON?"
    ],

    "data science": [
        "What is feature engineering?",
        "Explain supervised learning.",
        "Difference between classification and regression.",
        "What is Pandas?",
        "Explain NumPy."
    ],

    "machine learning": [
        "What is overfitting?",
        "Bias vs Variance?",
        "Explain cross validation.",
        "What is Random Forest?",
        "What is Gradient Descent?"
    ],

    "artificial intelligence": [
        "What is AI?",
        "Difference between AI and ML?",
        "Explain neural networks.",
        "What is Deep Learning?",
        "What is NLP?"
    ],

    "web development": [
        "What is REST API?",
        "Difference between GET and POST?",
        "Explain CORS.",
        "What is authentication?",
        "Explain MVC architecture."
    ],

    "cloud computing": [
        "What is cloud computing?",
        "Explain IaaS, PaaS and SaaS.",
        "What is serverless architecture?",
        "Difference between public and private cloud?",
        "What is scalability?"
    ],

    "devops": [
        "What is CI/CD?",
        "Explain Docker and Kubernetes.",
        "What is Infrastructure as Code?",
        "What is Jenkins?",
        "What is deployment pipeline?"
    ],

    "cybersecurity": [
        "What is encryption?",
        "Explain SSL/TLS.",
        "What is a firewall?",
        "What is SQL Injection?",
        "What is XSS?"
    ],

    "blockchain": [
        "What is blockchain?",
        "Explain smart contracts.",
        "Difference between public and private blockchain?",
        "What is mining?",
        "What is cryptocurrency?"
    ],

    "big data": [
        "What is Big Data?",
        "Explain Hadoop.",
        "What is Spark?",
        "What is Data Lake?",
        "Difference between structured and unstructured data?"
    ],

    "internet of things": [
        "What is IoT?",
        "Explain IoT architecture.",
        "What are IoT protocols?",
        "What are sensors?",
        "Explain MQTT."
    ],

}


# ==========================================================
# Generate Interview Questions
# ==========================================================

import random

def generate_interview_questions(skills):

    if isinstance(skills, str):
        skills = skills.split(",")

    questions = []
    used = set()

    # Resume Skill Questions
    for skill in skills:

        key = skill.strip().lower()

        if key in interview_questions:

            available = interview_questions[key]

            count = min(2, len(available))

            selected = random.sample(available, count)

            for q in selected:

                if q not in used:

                    questions.append(q)
                    used.add(q)

    # Project Questions
    project_questions = [
        "Explain your major project.",
        "What technologies did you use in your project?",
        "What challenges did you face during development?",
        "How did you solve those challenges?",
        "What improvements would you make if given more time?"
    ]

    questions.extend(random.sample(project_questions, 3))

    # HR Questions
    hr_questions = [
        "Tell me about yourself.",
        "Why should we hire you?",
        "What are your strengths?",
        "What are your weaknesses?",
        "Describe one challenging project you worked on.",
        "Where do you see yourself in five years?",
        "Why do you want to join our company?",
        "How do you handle pressure?"
    ]

    questions.extend(random.sample(hr_questions, 5))

    # Fill up to 15 Questions
    if len(questions) < 15:

        all_questions = []

        for value in interview_questions.values():
            all_questions.extend(value)

        remaining = [q for q in all_questions if q not in used]

        random.shuffle(remaining)

        questions.extend(
            remaining[:15 - len(questions)]
        )

    random.shuffle(questions)

    return questions[:15]