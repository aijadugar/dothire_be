import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_candidates(resume_texts, job_description):
    tfidf = TfidfVectorizer()
    corpus = resume_texts + [job_description]
    vectors = tfidf.fit_transform(corpus)

    job_vector = vectors[-1]  # Last is job description
    scores = cosine_similarity(vectors[:-1], job_vector)

    ranked_resumes = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    return ranked_resumes
