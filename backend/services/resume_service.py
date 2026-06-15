from models.user import User

from services.profile_summary_service import (
    ProfileSummaryService
)


class ResumeService:

    @staticmethod
    def build_resume(
        current_user: User
    ):

        profile = {
            "full_name": current_user.full_name,
            "email": current_user.email,
            "phone": current_user.phone,
            "linkedin_url": current_user.linkedin_url,
            "github_url": current_user.github_url,
            "location": current_user.location
        }

        summary = (
            ProfileSummaryService.generate_summary(
                current_user
            )["summary"]
        )

        skills = [
            {
                "skill_name": skill.skill_name,
                "category": skill.category,
                "proficiency_level":
                    skill.proficiency_level
            }
            for skill in current_user.skills
        ]

        projects = [
            {
                "project_name":
                    project.project_name,
                "description":
                    project.description,
                "github_url":
                    project.github_url
            }
            for project in current_user.projects
        ]

        certifications = [
            {
                "certification_name":
                    cert.certification_name,
                "issuing_organization":
                    cert.issuing_organization,
                "credential_id":
                    cert.credential_id,
                "credential_url":
                    cert.credential_url
            }
            for cert in current_user.certifications
        ]

        return {
            "profile": profile,
            "summary": summary,
            "skills": skills,
            "projects": projects,
            "certifications": certifications
        }