from models.user import User

from services.jd_analyzer import (
    JDAnalyzer
)


class GapAnalysisService:

    @staticmethod
    def analyze(
        current_user: User,
        jd_text: str
    ):

        jd_skills = (
            JDAnalyzer.extract_skills(
                jd_text
            )
        )

        evidence = {}

        # Skills
        for skill in current_user.skills:

            evidence[
                skill.skill_name.lower()
            ] = "skill"

        # Certifications
        for cert in current_user.certifications:

            cert_text = (
                cert.certification_name.lower()
            )

            if "aws" in cert_text:
                evidence["aws"] = (
                    "certification"
                )

        # Projects
        for project in current_user.projects:

            project_text = (
                f"{project.project_name} "
                f"{project.description}"
            ).lower()

            if "fastapi" in project_text:
                evidence["fastapi"] = (
                    "project"
                )

            if "sql" in project_text:
                evidence["sql"] = (
                    "project"
                )

            if "python" in project_text:
                evidence["python"] = (
                    "project"
                )

            if "machine learning" in project_text:
                evidence[
                    "machine learning"
                ] = "project"

        matched_skills = []
        missing_skills = []

        for skill in jd_skills:

            if skill in evidence:
                matched_skills.append(skill)

            else:
                missing_skills.append(skill)

        if len(jd_skills) == 0:

            match_score = 0

        else:

            match_score = int(
                (
                    len(matched_skills)
                    / len(jd_skills)
                ) * 100
            )

        return {
            "match_score": match_score,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "evidence": evidence
        }