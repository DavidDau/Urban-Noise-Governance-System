import { useLocation, useNavigate } from "react-router-dom";
import { useState } from "react";
import { downloadReport } from "../services/api";

function ResultsPage() {
  const location = useLocation();
  const navigate = useNavigate();

  const result = location.state;

  const [showRiskPopup, setShowRiskPopup] = useState(true);

  if (!result) {
    return (
      <div className="page">
        <h2>No results found</h2>

        <button onClick={() => navigate("/analyze")}>Go Back</button>
      </div>
    );
  }

  return (
    <div className="page">
      {/* Risk Popup */}

      {showRiskPopup && (
        <div style={overlay}>
          <div style={popup}>
            <h2>Governance Risk Score</h2>

            <h1 style={score}>{result.risk_score}/100</h1>

            <h3>{result.risk_level}</h3>

            <div style={buttonRow}>
              <button onClick={() => setShowRiskPopup(false)}>Close</button>

              <button onClick={() => navigate("/analyze")}>New Analysis</button>
            </div>
          </div>
        </div>
      )}

      <h1>Analysis Results</h1>

      {/* Main Results */}

      <div style={card}>
        <h2>Noise Classification</h2>

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
      </div>

      {/* Kigali Context */}

      <div style={card}>
        <h2>Location Context</h2>

        <p>
          <b>Venue:</b> {result.venue_type}
        </p>

        <p>
          <b>Period:</b> {result.time_period}
        </p>

        <p>
          <b>Legal Limit:</b> {result.legal_limit} dB
        </p>

        <p>
          <b>Recorded:</b> {result.estimated_db} dB
        </p>

        <p>
          <b>Violation:</b> {result.exceedance} dB
        </p>
      </div>

      {/* Compliance */}

      <div style={card}>
        <h2>Compliance Assessment</h2>

        <p>
          <b>Status:</b> {result.status}
        </p>
      </div>

      {/* Recommendation */}

      <div style={card}>
        <h2>Governance Recommendation</h2>

        <p>{result.recommendation}</p>
      </div>

      <button onClick={() => downloadReport(result.report_id)}>
        {" "}
        Download PDF Report{" "}
      </button>
      <button onClick={() => navigate("/analyze")}>New Analysis</button>
    </div>
  );
}

const card = {
  background: "#ffffff",
  padding: "20px",
  borderRadius: "10px",
  marginBottom: "20px",
};

const overlay = {
  position: "fixed",
  top: 0,
  left: 0,
  width: "100%",
  height: "100%",
  background: "rgba(0,0,0,0.6)",
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
};

const popup = {
  background: "#ffffff",
  padding: "30px",
  borderRadius: "15px",
  width: "350px",
  textAlign: "center",
};

const score = {
  fontSize: "48px",
  margin: "20px 0",
};

const buttonRow = {
  display: "flex",
  justifyContent: "space-between",
  margin: "20px 0 0 0",
};

export default ResultsPage;
