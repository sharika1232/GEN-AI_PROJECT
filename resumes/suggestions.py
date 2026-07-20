def generate_suggestions(missing_skills):

    suggestions = []

    skill_suggestions = {
        "django": "Learn Django and build at least one full-stack project.",
        "python": "Strengthen your Python programming fundamentals and solve coding problems.",
        "html": "Improve your HTML skills and create responsive web pages.",
        "css": "Practice modern CSS concepts like Flexbox and Grid.",
        "javascript": "Learn JavaScript ES6+, DOM manipulation, and asynchronous programming.",
        "react": "Build React applications and understand component-based architecture.",
        "sql": "Practice SQL queries, joins, and database design.",
        "mysql": "Gain experience with MySQL database management.",
        "git": "Learn Git commands and version control workflows.",
        "github": "Upload your projects to GitHub and maintain a professional portfolio.",
        "bootstrap": "Use Bootstrap to create responsive and attractive user interfaces.",
        "flask": "Develop REST APIs and web applications using Flask."
    }

    for skill in missing_skills:
        if skill.lower() in skill_suggestions:
            suggestions.append(skill_suggestions[skill.lower()])

    if len(suggestions) == 0:
        suggestions.append(
            "Excellent! Your resume matches the selected job requirements very well."
        )

    return suggestions