import re


def extract_candidate_name(text):
    """
    Extract candidate name from resume text.
    """

    lines = text.split("\n")

    for line in lines[:10]:

        line = line.strip()

        # Ignore empty lines
        if not line:
            continue

        # Ignore emails
        if "@" in line:
            continue

        # Ignore phone numbers
        if re.search(r"\d{6,}", line):
            continue

        # Ignore common headings
        ignore_words = [
            "resume",
            "curriculum",
            "vitae",
            "objective",
            "profile",
            "summary",
            "education",
            "experience",
            "skills",
        ]

        if any(word in line.lower() for word in ignore_words):
            continue

        # Usually the first clean line is the candidate name
        words = line.split()

        if 2 <= len(words) <= 4:
            return line

    return "Candidate"