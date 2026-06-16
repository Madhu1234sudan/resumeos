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

        resume_skills = [
            skill.skill_name.lower()
            for skill in current_user.skills
        ]

        matched_skills = [
            skill
            for skill in jd_skills
            if skill in resume_skills
        ]

        missing_skills = [
            skill
            for skill in jd_skills
            if skill not in resume_skills
        ]

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
            "missing_skills": missing_skills
        }