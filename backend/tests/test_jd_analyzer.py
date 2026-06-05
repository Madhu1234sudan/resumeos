from services.jd_analyzer import JDAnalyzer


job_description = """
We are looking for a Data Scientist
with strong skills in Python,
SQL, Pandas, Machine Learning,
Statistics and AWS.
"""


skills = JDAnalyzer.extract_skills(
    job_description
)

print(skills)