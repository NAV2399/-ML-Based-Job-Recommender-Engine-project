from fastapi import FastAPI
from pydantic import BaseModel
from model.recommender import match_jobs
import pandas as pd

app = FastAPI()

job_data = pd.DataFrame({
    'job_id': [1, 2, 3],
    'description': ["Data scientist with NLP", "Backend engineer with FastAPI", "ML engineer with PySpark"]
})

class Resume(BaseModel):
    text: str

@app.post("/recommend/")
def recommend_jobs(resume: Resume):
    results = match_jobs(resume.text, job_data)
    return results[['job_id', 'description', 'similarity']].to_dict(orient="records")