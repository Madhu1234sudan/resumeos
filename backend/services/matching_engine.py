class MatchingEngine:

    @staticmethod
    def match_skills(
        profile_skills,
        jd_skills
    ):

        profile_set = {
            skill.lower().strip()
            for skill in profile_skills
        }

        jd_set = {
            skill.lower().strip()
            for skill in jd_skills
        }

        matched = list(
            profile_set.intersection(jd_set)
        )

        missing = list(
            jd_set.difference(profile_set)
        )

        if len(jd_set) == 0:
            score = 0
        else:
            score = (
                len(matched) /
                len(jd_set)
            ) * 100

        return {
            "matched": matched,
            "missing": missing,
            "match_score": round(score, 2)
        }