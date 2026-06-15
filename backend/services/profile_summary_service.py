from models.user import User


class ProfileSummaryService:

    @staticmethod
    def generate_summary(
        current_user: User
    ):

        skills = [
            skill.skill_name
            for skill in current_user.skills
        ]

        projects = [
            project.project_name
            for project in current_user.projects
        ]

        certifications = [
            cert.certification_name
            for cert in current_user.certifications
        ]

        summary = (
            f"{current_user.full_name} is a "
            f"{current_user.role} based in "
            f"{current_user.location}. "
        )

        if skills:
            summary += (
                "Skilled in "
                + ", ".join(skills)
                + ". "
            )

        if projects:
            summary += (
                "Worked on projects such as "
                + ", ".join(projects)
                + ". "
            )

        if certifications:
            summary += (
                "Holds certifications including "
                + ", ".join(certifications)
                + "."
            )

        return {
            "summary": summary
        }