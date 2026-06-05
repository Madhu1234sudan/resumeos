class JDAnalyzer:

    KNOWN_SKILLS = {
        "python",
        "sql",
        "machine learning",
        "pandas",
        "numpy",
        "scikit-learn",
        "statistics",
        "nlp",
        "tensorflow",
        "pytorch",
        "aws",
        "tableau",
        "power bi",
        "excel"
    }

    @staticmethod
    def extract_skills(
        job_description: str
    ):

        jd_lower = job_description.lower()

        found_skills = []

        for skill in JDAnalyzer.KNOWN_SKILLS:

            if skill in jd_lower:
                found_skills.append(skill)

        return sorted(found_skills)