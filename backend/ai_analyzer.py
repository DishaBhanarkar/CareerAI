import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)


def analyze_with_gemini(
    resume_text,
    job_description,
    matched_skills,
    missing_skills,
    match_score
):
    prompt = f"""
You are CareerAI, an AI career assistant.

Analyze the candidate's resume against the given job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

MATCH SCORE:
{match_score}%

MATCHED SKILLS:
{", ".join(matched_skills)}

MISSING SKILLS:
{", ".join(missing_skills)}

Return ONLY valid JSON in exactly this structure:

{{
  "strengths": [
    "strength 1",
    "strength 2",
    "strength 3"
  ],
  "skill_gaps": [
    "skill gap 1",
    "skill gap 2"
  ],
  "learning_suggestions": [
    "learning suggestion 1",
    "learning suggestion 2",
    "learning suggestion 3"
  ],
  "resume_suggestions": [
    "resume suggestion 1",
    "resume suggestion 2",
    "resume suggestion 3"
  ]
}}

Rules:
- Do not change or recalculate the match score.
- Do not invent skills, projects, education, or experience.
- Base the strengths only on information present in the resume.
- Skill gaps should focus on relevant missing requirements.
- Learning suggestions should be practical and specific.
- Resume suggestions should explain how the candidate can better present relevant experience.
- Keep each item concise.
- Do not include Markdown.
- Do not include ```json or ``` around the response.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    response_text = response.text.strip()

    # Remove accidental Markdown code fences if Gemini adds them
    if response_text.startswith("```"):
        response_text = response_text.replace("```json", "")
        response_text = response_text.replace("```", "")
        response_text = response_text.strip()

    try:
        return json.loads(response_text)

    except json.JSONDecodeError:
        return {
            "strengths": [],
            "skill_gaps": [],
            "learning_suggestions": [],
            "resume_suggestions": [],
            "raw_analysis": response_text
        }