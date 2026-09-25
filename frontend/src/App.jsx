import { useState } from "react";
import "./App.css";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [message, setMessage] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!resume) {
      setMessage("Please select a resume first.");
      return;
    }

    if (!jobDescription.trim()) {
      setMessage("Please enter a job description.");
      return;
    }

    const formData = new FormData();

    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      setLoading(true);
      setMessage("");
      setResult(null);

      const response = await fetch(
        "http://127.0.0.1:5000/upload-resume",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (response.ok) {
        setMessage("Resume analyzed successfully!");
        setResult(data);
      } else {
        setMessage(data.error || "Something went wrong.");
      }
    } catch (error) {
      console.error(error);
      setMessage("Could not connect to CareerAI backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">

      {/* HEADER */}

      <h1>CareerAI</h1>

      <p className="subtitle">
        AI Resume & Job Matching
      </p>


      {/* INPUT SECTION */}

      <div className="input-container">

        {/* RESUME */}

        <div className="input-box">

          <h2>Upload Resume</h2>

          <p>
            Upload your resume in PDF format.
          </p>

          <input
            type="file"
            accept=".pdf"
            onChange={(event) => {
              setResume(event.target.files[0]);
              setMessage("");
              setResult(null);
            }}
          />

          {resume && (
            <p className="selected-file">
              Selected:
              <strong>{resume.name}</strong>
            </p>
          )}

        </div>


        {/* JOB DESCRIPTION */}

        <div className="input-box">

          <h2>Job Description</h2>

          <p>
            Paste the job description below.
          </p>

          <textarea
            placeholder="Paste the job description here..."
            value={jobDescription}
            onChange={(event) => {
              setJobDescription(event.target.value);
              setMessage("");
              setResult(null);
            }}
          />

        </div>

      </div>


      {/* ANALYZE BUTTON */}

      <button
        className="analyze-button"
        onClick={handleUpload}
        disabled={loading}
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>


      {/* MESSAGE */}

      {message && (
        <p className="message">
          {message}
        </p>
      )}


      {/* RESULTS */}

      {result && (

        <div className="result-box">

          <h2>Match Analysis</h2>


          {/* SCORE */}

          <div
            className="score"
            style={{
              "--score": `${result.match_score}%`,
            }}
          >
            {result.match_score}%
          </div>

          <p className="score-label">
            Resume–Job Match
          </p>


          {/* SKILLS */}

          <div className="skills-grid">

            {/* MATCHED */}

            <div className="skills-section matched-section">

              <h3>✓ Matched Skills</h3>

              {result.matched_skills.length > 0 ? (
                <ul>
                  {result.matched_skills.map((skill) => (
                    <li key={skill}>
                      {skill}
                    </li>
                  ))}
                </ul>
              ) : (
                <p>No matching skills found.</p>
              )}

            </div>


            {/* MISSING */}

            <div className="skills-section missing-section">

              <h3>✗ Missing Skills</h3>

              {result.missing_skills.length > 0 ? (
                <ul>
                  {result.missing_skills.map((skill) => (
                    <li key={skill}>
                      {skill}
                    </li>
                  ))}
                </ul>
              ) : (
                <p>No missing skills found.</p>
              )}

            </div>

          </div>


          {/* AI ANALYSIS */}

          {result.ai_analysis && (

            <div className="ai-analysis">

              <h2>
                🤖 AI Career Analysis
              </h2>

              <p className="ai-subtitle">
                Personalized recommendations based on your
                resume and the job description.
              </p>


              <div className="ai-cards">


                {/* STRENGTHS */}

                <div className="ai-card strengths-card">

                  <div className="ai-card-icon">
                    💪
                  </div>

                  <div>

                    <h3>
                      Strengths
                    </h3>

                    <ul>

                      {result.ai_analysis.strengths?.map(
                        (item, index) => (
                          <li key={index}>
                            {item}
                          </li>
                        )
                      )}

                    </ul>

                  </div>

                </div>


                {/* SKILL GAPS */}

                <div className="ai-card gaps-card">

                  <div className="ai-card-icon">
                    ⚠️
                  </div>

                  <div>

                    <h3>
                      Skill Gaps
                    </h3>

                    <ul>

                      {result.ai_analysis.skill_gaps?.map(
                        (item, index) => (
                          <li key={index}>
                            {item}
                          </li>
                        )
                      )}

                    </ul>

                  </div>

                </div>


                {/* LEARNING */}

                <div className="ai-card learning-card">

                  <div className="ai-card-icon">
                    📚
                  </div>

                  <div>

                    <h3>
                      Learning Suggestions
                    </h3>

                    <ul>

                      {result.ai_analysis.learning_suggestions?.map(
                        (item, index) => (
                          <li key={index}>
                            {item}
                          </li>
                        )
                      )}

                    </ul>

                  </div>

                </div>


                {/* RESUME */}

                <div className="ai-card resume-card">

                  <div className="ai-card-icon">
                    📝
                  </div>

                  <div>

                    <h3>
                      Resume Suggestions
                    </h3>

                    <ul>

                      {result.ai_analysis.resume_suggestions?.map(
                        (item, index) => (
                          <li key={index}>
                            {item}
                          </li>
                        )
                      )}

                    </ul>

                  </div>

                </div>

              </div>

            </div>

          )}

        </div>

      )}

    </div>
  );
}

export default App;