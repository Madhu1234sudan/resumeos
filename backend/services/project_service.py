from sqlalchemy.orm import Session

from models.project import Project
from models.user import User

from repositories.project_repository import (
    ProjectRepository
)


class ProjectService:

    @staticmethod
    def create_project(
        db: Session,
        current_user: User,
        data
    ):

        project = Project(
            user_id=current_user.id,
            project_name=data.project_name,
            description=data.description,
            github_url=data.github_url
        )

        return ProjectRepository.create(
            db,
            project
        )

    @staticmethod
    def get_projects(
        db: Session,
        current_user: User
    ):

        return ProjectRepository.get_all_by_user(
            db,
            current_user.id
        )

    @staticmethod
    def update_project(
        db: Session,
        project_id: int,
        current_user: User,
        data
    ):

        project = ProjectRepository.get_by_id(
            db,
            project_id
        )

        if not project:
            return None

        if project.user_id != current_user.id:
            return None

        project.project_name = data.project_name
        project.description = data.description
        project.github_url = data.github_url

        return ProjectRepository.update(
            db,
            project
        )

    @staticmethod
    def delete_project(
        db: Session,
        project_id: int,
        current_user: User
    ):

        project = ProjectRepository.get_by_id(
            db,
            project_id
        )

        if not project:
            return False

        if project.user_id != current_user.id:
            return False

        ProjectRepository.delete(
            db,
            project
        )

        return True