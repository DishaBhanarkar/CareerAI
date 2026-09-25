from flask import Flask, request, jsonify
from flask_cors import CORS
import pdfplumber
import io

from matcher import match_resume_to_job
from ai_analyzer import analyze_with_gemini


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "CareerAI backend is running!"


@app.route("/upload-resume", methods=["POST"])
def upload_resume():

    if "resume" not in request.files:
        return jsonify({
            "error": "No resume uploaded"
        }), 400

    resume = request.files["resume"]

    if resume.filename == "":
        return jsonify({
            "error": "No file selected"
        }), 400

    job_description = request.form.get(
        "job_description",
        ""
    )

    if not job_description.strip():
        return jsonify({
            "error": "No job description provided"
        }), 400

    # -----------------------------
    # Extract text from PDF
    # -----------------------------

    extracted_text = ""

    try:
        pdf_bytes = io.BytesIO(resume.read())

        with pdfplumber.open(pdf_bytes) as pdf:

            for page in pdf.pages:

                text = page.extract_text()

                if text:
                    extracted_text += text + "\n"

    except Exception as error:

        return jsonify({
            "error": f"Could not read PDF: {str(error)}"
        }), 400


    # -----------------------------
    # Match resume with job
    # -----------------------------

    result = match_resume_to_job(
        extracted_text,
        job_description
    )


    # -----------------------------
    # Gemini AI analysis
    # -----------------------------

    try:

        ai_analysis = analyze_with_gemini(
            extracted_text,
            job_description,
            result["matched_skills"],
            result["missing_skills"],
            result["match_score"]
        )

    except Exception as error:

        ai_analysis = (
            "AI analysis could not be generated. "
            f"Error: {str(error)}"
        )


    # -----------------------------
    # Send result to frontend
    # -----------------------------

    return jsonify({

        "message": "Resume analyzed successfully",

        "filename": resume.filename,

        "match_score": result["match_score"],

        "resume_skills": result["resume_skills"],

        "job_skills": result["job_skills"],

        "matched_skills": result["matched_skills"],

        "missing_skills": result["missing_skills"],

        "ai_analysis": ai_analysis
    })


if __name__ == "__main__":

    app.run(debug=True)