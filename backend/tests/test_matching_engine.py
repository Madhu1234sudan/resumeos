from services.matching_engine import MatchingEngine

profile_skills = [
    "Python",
    "SQL",
    "Machine Learning"
]

jd_skills = [
    "Python",
    "Machine Learning",
    "Statistics",
    "Pandas"
]

result = MatchingEngine.match_skills(
    profile_skills,
    jd_skills
)

print(result)