import { useLocation, useNavigate } from "react-router-dom";
import { useEffect } from "react";

function ResultsPage() {
  const location = useLocation();
  const navigate = useNavigate();
  const result = location.state;

  useEffect(() => {
    if (result) {
      const history = JSON.parse(localStorage.getItem("noise_history") || "[]");
      history.push({
        ...result,
        timestamp: new Date().toISOString(),
      });
      localStorage.setItem("noise_history", JSON.stringify(history));
    }
  }, [result]);

  if (!result) {
    return (
      <div className="page">
        <h2>No results found</h2>
        <button onClick={() => navigate("/analyze")}>Go back</button>
      </div>
    );
  }

  return (
    <div className="page">
      <h1>Analysis Results</h1>

      <div style={card}>
        <p>
          <b>Source:</b> {result.source}
        </p>
        <p>
          <b>Confidence:</b> {(result.confidence * 100).toFixed(2)}%
        </p>
        <p>
          <b>Estimated dB:</b> {result.estimated_db}
        </p>
        <p>
          <b>Severity:</b> {result.severity}
        </p>
        <p>
          <b>Venue:</b> {result.venue_type}
        </p>
        <p>
          <b>Time:</b> {result.recording_time} ({result.time_period})
        </p>
        <p>
          <b>Limit:</b> {result.legal_limit} dB
        </p>
        <p>
          <b>Status:</b> {result.status}
        </p>
        <p>
          <b>Exceeded:</b> {result.exceedance} dB
        </p>

        <h3>Recommendation</h3>
        <p>{result.recommendation}</p>
      </div>

      <button onClick={() => navigate("/analyze")}>New Analysis</button>
    </div>
  );
}

const card = {
  background: "#fff",
  padding: "20px",
  borderRadius: "10px",
  marginTop: "20px",
  boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
};

export default ResultsPage;
