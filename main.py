import streamlit as st
import joblib
import pdfplumber

from sklearn.metrics.pairwise import cosine_similarity

# load saves file

tfidf = joblib.load("tfidf_vectorizer.joblib")
job_vectors = joblib.load("job_vectors.joblib")
df = joblib.load("df.joblib")

# upload pdf

def extract_text_from_pdf(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for pages in pdf.pages:
            pages_text = pages.extract_text()

            if pages_text:
                text +=pages_text + "\n"
    return text


st.title("Ai Resume Recommendation System ")

uploaded_file = st.file_uploader("upload Resume pdf",type =["pdf"])

if uploaded_file is not None:

    resume_text = extract_text_from_pdf(uploaded_file)

    resume_vectors = tfidf.transform([resume_text])

    similarity = cosine_similarity(resume_vectors,job_vectors)[0]

    df["similarity"] = similarity

    top_jobs = (df.sort_values("similarity", ascending=False).drop_duplicates(subset=["Role"]).head(5))

    st.subheader("Top 5 jobs")

    st.dataframe(top_jobs[["Role","similarity"]])