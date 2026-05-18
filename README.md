# ATS Resume Analyzer

A web-based Applicant Tracking System (ATS) Resume Analyzer that evaluates how well a resume matches a given job description using Natural Language Processing (NLP) techniques.

---

## Features

- Upload Resume in PDF or DOCX format
- Input Job Description
- ATS Score Calculation
- Resume & Job Description Similarity Analysis
- NLP-based Text Processing
- Responsive and Modern UI
- Real-time Resume Relevance Evaluation

---

## Tech Stack

### Frontend
- HTML
- CSS
- Bootstrap

### Backend
- Python
- Flask

### NLP & Data Processing
- Scikit-learn
- NLTK
- TF-IDF Vectorization
- Cosine Similarity

### File Processing
- PyPDF2
- python-docx

---

## How It Works

1. Upload Resume (PDF/DOCX)
2. Enter Job Description
3. Resume text extraction
4. Text preprocessing:
   - Lowercasing
   - Stopword removal
   - Text cleaning
5. TF-IDF Vectorization
6. Cosine Similarity calculation
7. ATS score generation

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ats-resume-analyzer.git
cd ats-resume-analyzer
