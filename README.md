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

# NLP-Based Job Recommendation System


## Project Overview

Excluded files:
- job_vectors.joblib
- jobs_dataset_with_features.csv
- df.joblib
- job_vectors.joblib
- jobs_dataset_with_features.csv

The **NLP-Based Job Recommendation System** is a content-based recommendation system that helps users identify relevant job roles based on their skills, knowledge, and professional profile.

The project uses Natural Language Processing (NLP) techniques to clean and preprocess textual data, followed by TF-IDF vectorization and Cosine Similarity to measure the relevance between user-provided text and available job descriptions.

Unlike traditional job recommendation approaches that rely on classification models, this system uses text similarity to rank and recommend relevant job opportunities.

## Objectives

- Preprocess textual job-related data using NLP techniques.
- Clean and standardize job descriptions and skill-related information.
- Convert text into numerical representations using TF-IDF.
- Calculate similarity between user profiles and job descriptions.
- Recommend the most relevant job roles based on similarity scores.

## Technologies Used

- **Programming Language:** Python
- **Data Processing:** Pandas, NumPy
- **Natural Language Processing:** NLTK, Regular Expressions
- **Text Vectorization:** TF-IDF
- **Similarity Measurement:** Cosine Similarity
- **Interface:** Streamlit (if applicable)

## Dataset

The project uses a job-related dataset containing:

- **Role:** Job titles or professional roles.
- **Features:** Skills, knowledge, and textual descriptions associated with each role.

The dataset was cleaned and prepared before applying NLP preprocessing and recommendation techniques.

## Methodology

### 1. Data Preprocessing
- Loaded and explored the job dataset.
- Handled missing values.
- Checked and removed duplicate records where necessary.
- Prepared textual features for NLP processing.

### 2. NLP Text Cleaning
Applied text preprocessing techniques to improve text consistency:

- Lowercasing
- Removing URLs and HTML tags
- Removing punctuation and unnecessary characters
- Tokenization
- Stopword removal
- Lemmatization

### 3. TF-IDF Vectorization

Term Frequency–Inverse Document Frequency (TF-IDF) converts textual information into numerical vectors.

It assigns importance to words based on their frequency within a document and their distribution across the dataset.

### 4. Cosine Similarity

Cosine Similarity measures the similarity between the user's input text and job-related feature vectors.

The similarity scores are used to rank available job roles according to their relevance.

### 5. Job Recommendation

The system sorts job roles based on their similarity scores and returns the most relevant recommendations.

## Recommendation Workflow

1. User provides skills or resume-related text.
2. The input text is cleaned using NLP.
3. The cleaned text is transformed using the fitted TF-IDF vectorizer.
4. Cosine Similarity calculates similarity against available job descriptions.
5. Job roles are ranked by similarity.
6. The system displays the top relevant recommendations.

## Project Structure

```text
Job-Recommendation-System/
│
├── dataset/
│   └── job_dataset.csv
│
├── notebooks/
│   └── job_recommendation.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```


## Key Features

- NLP-based text preprocessing.
- Skill and job-description matching.
- TF-IDF-based text representation.
- Cosine similarity-based recommendation.
- Ranked job recommendations.

## Limitations

- Recommendations depend on the quality and coverage of the dataset.
- Cosine similarity measures textual similarity, not actual candidate suitability.
- Semantically similar words may not always receive high similarity scores.
- The
