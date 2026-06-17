from models.user import User

from services.gap_analysis_service import (
    GapAnalysisService
)


class ATSScorer:

    @staticmethod
    def score(
        current_user: User,
        jd_text: str
    ):

        gap = GapAnalysisService.analyze(
            current_user,
            jd_text
        )

        recommendations = []

        for skill in gap["missing_skills"]:

            recommendations.append(
                f"Add {skill.upper()} to your Skills section."
            )

            recommendations.append(
                f"Mention {skill.upper()} in a project."
            )

            recommendations.append(
                f"Include {skill.upper()} in your professional summary."
            )

        return {
            "ats_score": gap["match_score"],
            "keyword_hit_rate": gap["match_score"],
            "matched_skills": gap["matched_skills"],
            "missing_skills": gap["missing_skills"],
            "recommendations": recommendations
        }