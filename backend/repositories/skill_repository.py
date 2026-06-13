from sqlalchemy.orm import Session

from models.skill import Skill


class SkillRepository:

    @staticmethod
    def create(
        db: Session,
        skill: Skill
    ):

        db.add(skill)
        db.commit()
        db.refresh(skill)

        return skill

    @staticmethod
    def get_all_by_user(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Skill)
            .filter(
                Skill.user_id == user_id
            )
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        skill_id: int
    ):

        return (
            db.query(Skill)
            .filter(
                Skill.id == skill_id
            )
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        skill: Skill
    ):

        db.commit()
        db.refresh(skill)

        return skill

    @staticmethod
    def delete(
        db: Session,
        skill: Skill
    ):

        db.delete(skill)
        db.commit()