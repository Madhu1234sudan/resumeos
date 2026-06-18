from models.user import User

from services.profile_summary_service import (
    ProfileSummaryService
)

from services.gap_analysis_service import (
    GapAnalysisService
)


class ResumeRewriter:

    @staticmethod
    def rewrite(
        current_user: User,
        jd_text: str
    ):

        original_summary = (
            ProfileSummaryService.generate_summary(
                current_user
            )["summary"]
        )

        gap = GapAnalysisService.analyze(
            current_user,
            jd_text
        )

        rewritten_summary = original_summary

        if gap["missing_skills"]:

            rewritten_summary += (
                " Currently strengthening expertise in "
                + ", ".join(
                    skill.upper()
                    for skill in gap["missing_skills"]
                )
                + " to better align with target job requirements."
            )

        improvements = []

        for skill in gap["missing_skills"]:

            improvements.append(
                f"Add {skill.upper()} to the Skills section."
            )

            improvements.append(
                f"Include a project demonstrating {skill.upper()}."
            )

            improvements.append(
                f"Mention {skill.upper()} in the professional summary."
            )

        return {
            "original_summary": original_summary,
            "rewritten_summary": rewritten_summary,
            "improvements": improvements
        }