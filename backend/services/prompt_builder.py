from models.user import User

from services.resume_service import (ResumeService)

from services.gap_analysis_service import (GapAnalysisService)

from services.ats_scorer import (ATSScorer)

import json



class PromptBuilder:

    @staticmethod
    def build_resume_prompt(
        current_user: User,
        jd_text: str
    ):

        resume = ResumeService.build_resume(
            current_user
        )
        resume_json = json.dumps(
         resume,
        indent=4
        )


        gap = GapAnalysisService.analyze(
            current_user,
            jd_text
        )

        ats = ATSScorer.score(
            current_user,
            jd_text
        )

        prompt = f"""
You are an expert ATS Resume Writer.

Rewrite the following resume to better match the job description.

=========================
JOB DESCRIPTION
=========================

{jd_text}

=========================
CURRENT RESUME
=========================

{resume_json}

=========================
GAP ANALYSIS
=========================

Matched Skills:
{gap["matched_skills"]}

Missing Skills:
{gap["missing_skills"]}

=========================
ATS SCORE
=========================

Current ATS Score:
{ats["ats_score"]}

Recommendations:
{ats["recommendations"]}

=========================
TASK
=========================

Rewrite the professional summary.

Improve ATS keyword coverage.

Do not invent experience.

Do not fabricate projects.

Only strengthen wording using existing information.

Return JSON only.
"""

        return prompt