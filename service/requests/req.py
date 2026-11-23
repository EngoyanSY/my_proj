import requests
import time
import random as rnd

for i in range(50):
    params = {'item_id': i}
    data = {
              "Major_Category" : "STEM",
              "Year_of_Study": "Graduate",
              "Primary_Use_Case": rnd.choice(["Copywriting/Drafting", "Debugging/Troubleshooting", "Direct_Answer_Generation"]),
              "Prompt_Engineering_Skill": rnd.choice(["Advanced", "Beginner", "Intermediate"]),
              "Institutional_Policy": "Allowed_With_Citation",
              "Burnout_Risk_Level":"Low",
              "Pre_Semester_GPA": round(rnd.uniform(2.0, 4.0), 2),
              "Weekly_GenAI_Hours": rnd.randint(5, 15),
              "Tool_Diversity":2,
              "Traditional_Study_Hours": rnd.randint(5, 15),
              "Perceived_AI_Dependency":5,
              "Anxiety_Level_During_Exams":4,
              "Skill_Retention_Score": rnd.randint(80, 95)
    }
    response = requests.post('http://localhost:8001/api/prediction', params=params, json=data)
    time.sleep(rnd.randint(1,5))
    print(response.json())