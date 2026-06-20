from models.user import User

from services.prompt_builder import (
    PromptBuilder
)

from services.llm_service import (
    LLMService
)

from services.profile_summary_service import (
    ProfileSummaryService
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

        prompt = (
            PromptBuilder.build_resume_prompt(
                current_user,
                jd_text
            )
        )

        ai_response = (
            LLMService.rewrite_resume(
                prompt
            )
        )

        return {
            "original_summary": original_summary,
            "ai_response": ai_response
        }