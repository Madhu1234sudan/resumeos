from sqlalchemy.orm import Session

from models.skill import Skill
from models.user import User

from repositories.skill_repository import (
    SkillRepository
)


class SkillService:

    @staticmethod
    def create_skill(
        db: Session,
        current_user: User,
        data
    ):

        skill = Skill(
            user_id=current_user.id,
            skill_name=data.skill_name,
            category=data.category,
            proficiency_level=data.proficiency_level
        )

        return SkillRepository.create(
            db,
            skill
        )

    @staticmethod
    def get_skills(
        db: Session,
        current_user: User
    ):

        return SkillRepository.get_all_by_user(
            db,
            current_user.id
        )

    @staticmethod
    def update_skill(
        db: Session,
        skill_id: int,
        current_user: User,
        data
    ):

        skill = SkillRepository.get_by_id(
            db,
            skill_id
        )

        if not skill:
            return None

        if skill.user_id != current_user.id:
            return None

        skill.skill_name = data.skill_name
        skill.category = data.category
        skill.proficiency_level = data.proficiency_level

        return SkillRepository.update(
            db,
            skill
        )

    @staticmethod
    def delete_skill(
        db: Session,
        skill_id: int,
        current_user: User
    ):

        skill = SkillRepository.get_by_id(
            db,
            skill_id
        )

        if not skill:
            return False

        if skill.user_id != current_user.id:
            return False

        SkillRepository.delete(
            db,
            skill
        )

        return True