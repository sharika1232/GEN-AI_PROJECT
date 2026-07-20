learning_resources = {

    "python": [
        "Python Official Documentation",
        "Real Python",
        "W3Schools Python"
    ],

    "java": [
        "Oracle Java Documentation",
        "GeeksforGeeks Java",
        "JavaTPoint"
    ],

    "django": [
        "Django Official Documentation",
        "Django Girls Tutorial",
        "Corey Schafer Django Playlist"
    ],

    "sql": [
        "SQLBolt",
        "W3Schools SQL",
        "Mode SQL Tutorial"
    ],

    "javascript": [
        "MDN JavaScript",
        "JavaScript.info",
        "W3Schools JavaScript"
    ],

    "react": [
        "React Official Documentation",
        "Scrimba React Course",
        "freeCodeCamp React"
    ],

    "aws": [
        "AWS Skill Builder",
        "AWS Documentation",
        "freeCodeCamp AWS"
    ],

    "docker": [
        "Docker Official Documentation",
        "Docker Getting Started",
        "KodeKloud Docker"
    ],

}

def get_learning_resources(skills):

    result = {}

    for skill in skills:

        key = skill.strip().lower()

        if key in learning_resources:
            result[skill] = learning_resources[key]

    return result
