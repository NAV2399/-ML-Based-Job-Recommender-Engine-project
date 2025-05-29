import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from embeddings.bert_embedder import get_bert_embedding

def match_jobs(resume_text, job_df):
    resume_vec = get_bert_embedding(resume_text)
    job_df['embedding'] = job_df['description'].apply(get_bert_embedding)
    job_df['similarity'] = job_df['embedding'].apply(lambda x: cosine_similarity([resume_vec], [x])[0][0])
    return job_df.sort_values(by='similarity', ascending=False).head(5)

def extract_transform_load():
    print("ETL pipeline executed")  # Placeholder for Airflow task