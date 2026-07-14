#  AI Resume Recommendation System

An NLP-based Resume Recommendation System that analyzes a candidate's resume and recommends the **Top 5 most suitable job roles** using **TF-IDF Vectorization** and **Cosine Similarity**.

Built with **Python**, **Scikit-learn**, **Streamlit**, and **PDF Resume Parsing**.

---

##  Features

- Upload Resume in PDF format
- Extract text from the uploaded resume
- Perform text preprocessing
- Convert text into TF-IDF vectors
- Calculate similarity using Cosine Similarity
- Recommend Top 5 matching job roles
- Display match percentage
- Simple and interactive Streamlit web interface

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- PDFPlumber
- Joblib

---

##  Project Structure

```
AI_Resume_Recommendation/
│
├── app.py
├── Resume.csv
├── Job_Description.csv
├── tfidf_vectorizer.joblib
├── job_vectors.joblib
├── job_df.joblib
├── requirements.txt
├── README.md
└── assets/
```

---

##  Workflow

```
Resume PDF
      │
      ▼
Extract Resume Text
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Top 5 Job Recommendations
```

---

##  Machine Learning & NLP Techniques

- Text Cleaning
- TF-IDF Vectorization
- Cosine Similarity
- Recommendation System

---

## Dataset

The project uses two datasets:

### Resume Dataset
Contains resume information including:

- Resume Text
- Category
- Clean Text

### Job Dataset

Contains job descriptions including:

- Job Role
- Job Description / Features

---

##  Output

The system recommends the **Top 5 matching job roles** along with their similarity score.

Example:

| Job Role | Match % |
|-----------|---------|
| Customer Support Manager | 17.14% |
| HR Generalist | 14.74% |
| Customer Experience Strategist | 14.59% |
| Marketing Communications Director | 13.82% |
| Customer Support Specialist | 12.76% |

---


##  Future Improvements

- Skill Gap Analysis
- Missing Skill Recommendation
- BERT/Sentence Transformers Embeddings
- Resume Ranking
- Job Description Summarization
- Resume PDF Download
- Explain Why a Job Was Recommended
- Multi-language Resume Support

---

##  Learning Outcomes

Through this project, I gained practical experience in:

- Natural Language Processing (NLP)
- Recommendation Systems
- Feature Extraction using TF-IDF
- Cosine Similarity
- PDF Text Extraction
- Model Serialization using Joblib
- Streamlit Web Application Development

---


## Large Files

Some trained models and datasets are not included in this repository because they exceed GitHub's file size limits.

Excluded files:
- job_vectors.joblib
- jobs_dataset_with_features.csv
- df.joblib
- job_vectors.joblib
- jobs_dataset_with_features.csv
