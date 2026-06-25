import { useLocation, useNavigate, Link } from "react-router-dom";
import { useState } from "react";
import { downloadReport } from "../services/api";
import StatusBadge from "../components/StatusBadge";

function riskScoreClass(level) {
  const v = (level || "").toLowerCase();
  if (v === "low") return "modal-score--green";
  if (v === "medium" || v === "moderate") return "modal-score--amber";
  return "modal-score--coral";
}

function ResultRow({ label, value }) {
  return (
    <div className="result-row">
      <span>{label}</span>
      <span>{value}</span>
    </div>
  );
}

function ResultsPage() {
  const location = useLocation();
  const navigate = useNavigate();
  const result = location.state;
  const [showRiskPopup, setShowRiskPopup] = useState(true);

  if (!result) {
    return (
      <div className="page">
        <div className="empty-state">
          <div className="empty-state-icon" aria-hidden="true">
            🔍
          </div>
          <h2>No results found</h2>
          <p>Run a new analysis to see classification and compliance data.</p>
          <Link to="/analyze" className="primary-btn">
            Start analysis
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="page">
      {showRiskPopup && (
        <div className="modal-overlay" role="dialog" aria-modal="true">
          <div className="modal">
            <h2>Governance risk score</h2>
            <p className={`modal-score ${riskScoreClass(result.risk_level)}`}>
              {result.risk_score}/100
            </p>
            <StatusBadge label={result.risk_level} type="risk" />
            <div className="btn-row" style={{ justifyContent: "center" }}>
              <button
                type="button"
                className="btn-dark"
                onClick={() => setShowRiskPopup(false)}
              >
                View details
              </button>
              <button
                type="button"
                className="btn-ghost"
                onClick={() => navigate("/analyze")}
              >
                New analysis
              </button>
            </div>
          </div>
        </div>
      )}

      <header className="page-header">
        <h1>Analysis results</h1>
        <p>
          {result.source} · {result.estimated_db} dB ·{" "}
          <StatusBadge label={result.status} type="status" />
        </p>
      </header>

      <div className="results-grid">
        <article className="result-card">
          <h2>Noise classification</h2>
          <ResultRow label="Source" value={result.source} />
          <ResultRow
            label="Confidence"
            value={`${(result.confidence * 100).toFixed(1)}%`}
          />
          <ResultRow label="Estimated level" value={`${result.estimated_db} dB`} />
          <div className="result-row">
            <span>Severity</span>
            <StatusBadge label={result.severity} type="severity" />
          </div>
        </article>

        <article className="result-card">
          <h2>Location context</h2>
          <ResultRow label="Venue" value={result.venue_type} />
          <ResultRow label="Period" value={result.time_period} />
          <ResultRow label="Legal limit" value={`${result.legal_limit} dB`} />
          <ResultRow label="Recorded" value={`${result.estimated_db} dB`} />
          <ResultRow label="Exceedance" value={`${result.exceedance} dB`} />
        </article>

        <article className="result-card">
          <h2>Compliance assessment</h2>
          <div className="result-row">
            <span>Status</span>
            <StatusBadge label={result.status} type="status" />
          </div>
        </article>

        <article className="result-card result-card--highlight">
          <h2>Governance recommendation</h2>
          <p className="result-recommendation">{result.recommendation}</p>
        </article>
      </div>

      <div className="btn-row">
        <button
          type="button"
          className="btn-dark"
          onClick={() => downloadReport(result.report_id)}
        >
          Download PDF report
        </button>
        <button
          type="button"
          className="btn-ghost"
          onClick={() => navigate("/analyze")}
        >
          New analysis
        </button>
        <Link to="/history" className="btn-ghost">
          View history
        </Link>
      </div>
    </div>
  );
}

export default ResultsPage;
