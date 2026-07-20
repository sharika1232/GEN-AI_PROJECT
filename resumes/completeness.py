import re


def calculate_completeness(text):

    report = {}

    report["Name"] = True if len(text.split()) > 2 else False

    report["Email"] = bool(
        re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    )

    report["Phone"] = bool(
        re.search(r"\d{10}", text)
    )

    report["Skills"] = "skills" in text.lower()

    report["Education"] = any(
        word in text.lower()
        for word in [
            "education",
            "b.tech",
            "btech",
            "degree",
            "college",
            "university",
        ]
    )

    report["Experience"] = any(
        word in text.lower()
        for word in [
            "experience",
            "worked",
            "internship",
        ]
    )

    report["Projects"] = any(
        word in text.lower()
        for word in [
            "project",
            "projects",
        ]
    )

    report["Certifications"] = any(
        word in text.lower()
        for word in [
            "certificate",
            "certification",
        ]
    )

    total = len(report)

    completed = sum(report.values())

    score = round((completed / total) * 100)

    return score, report