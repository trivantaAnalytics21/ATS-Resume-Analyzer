from flask import Flask, render_template, request
from utils import extract_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)


UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    
    resume_file = request.files.get("resume")
    job_desc = request.form.get("job_desc")

    
    if not resume_file or resume_file.filename == "":
        return render_template("index.html", score="No file uploaded")

    if not job_desc or job_desc.strip() == "":
        return render_template("index.html", score="Job description required")

    
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], resume_file.filename)
    resume_file.save(filepath)

    try:
        
        resume_text = extract_text(resume_file)

        if not resume_text or resume_text.strip() == "":
            return render_template("index.html", score="Could not read resume")

        
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform([resume_text, job_desc])

        similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
        ats_score = round(similarity * 100, 2)

    except Exception as e:
        return render_template("index.html", score=f"Error: {str(e)}")

    return render_template("index.html", score=ats_score)


if __name__ == "__main__":
    app.run(debug=True)