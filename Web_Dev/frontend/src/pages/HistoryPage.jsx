import { useEffect, useState } from "react";
import { getHistory, downloadReport } from "../services/api";
import StatusBadge from "../components/StatusBadge";
import EmptyState from "../components/EmptyState";

const VENUE_OPTIONS = [
  "All",
  "Residential Zone",
  "Commercial Zone",
  "Industrial Zone",
  "Quiet Zone",
  "Special Quiet Zone",
  "Soundproof Venue",
  "Non-Soundproof Venue",
];

// Convert UTC timestamp to Rwanda local time
function formatDate(dateString) {
  if (!dateString) return "";

  return new Date(dateString + "Z").toLocaleString("en-RW", {
    dateStyle: "medium",
    timeStyle: "short",
    timeZone: "Africa/Kigali",
  });
}

function HistoryPage() {
  const [reports, setReports] = useState([]);
  const [loading, setLoading] = useState(true);
  const [expandedId, setExpandedId] = useState(null);
  const [venueFilter, setVenueFilter] = useState("All");
  const [timeFilter, setTimeFilter] = useState("All");
  const [sortOrder, setSortOrder] = useState("desc");

  useEffect(() => {
    const loadReports = async () => {
      try {
        const data = await getHistory();
        setReports(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    };

    loadReports();
  }, []);

  const filteredReports = reports
    .filter((report) => {
      const venueMatch =
        venueFilter === "All" || report.venue_type === venueFilter;

      const timeMatch =
        timeFilter === "All" || report.time_period === timeFilter;

      return venueMatch && timeMatch;
    })
    .sort((a, b) => (sortOrder === "asc" ? a.id - b.id : b.id - a.id));

  if (loading) {
    return (
      <div className="page">
        <div className="page-loading">
          <span className="spinner" aria-hidden="true" />
          Loading history...
        </div>
      </div>
    );
  }

  return (
    <div className="page">
      <header className="page-header">
        <h1>Analysis History</h1>
        <p>
          Browse previous analyses, review compliance results, and download
          official reports.
        </p>
      </header>

      {reports.length === 0 ? (
        <EmptyState
          icon="📂"
          title="No analyses yet"
          message="Run your first analysis to populate the history."
        />
      ) : (
        <>
          <div className="filter-bar">
            <select
              value={venueFilter}
              onChange={(e) => setVenueFilter(e.target.value)}
            >
              {VENUE_OPTIONS.map((venue) => (
                <option key={venue} value={venue}>
                  {venue === "All" ? "All Venues" : venue}
                </option>
              ))}
            </select>

            <select
              value={timeFilter}
              onChange={(e) => setTimeFilter(e.target.value)}
            >
              <option value="All">All Times</option>
              <option value="Day">Day</option>
              <option value="Night">Night</option>
            </select>

            <select
              value={sortOrder}
              onChange={(e) => setSortOrder(e.target.value)}
            >
              <option value="desc">Newest First</option>
              <option value="asc">Oldest First</option>
            </select>
          </div>

          {filteredReports.length === 0 ? (
            <EmptyState
              icon="🔍"
              title="No matching reports"
              message="Try changing your filters."
            />
          ) : (
            <div className="history-grid">
              {filteredReports.map((report) => {
                const expanded = expandedId === report.id;

                return (
                  <article key={report.id} className="history-card">
                    <div className="history-card-header">
                      <h2 className="history-card-source">{report.source}</h2>

                      <StatusBadge label={report.status} type="status" />
                    </div>

                    <p className="history-card-db">{report.estimated_db} dB</p>

                    <div className="history-card-meta">
                      <StatusBadge label={report.severity} type="severity" />

                      {report.risk_level && (
                        <StatusBadge label={report.risk_level} type="risk" />
                      )}
                    </div>

                    <p className="history-card-date">
                      {report.venue_type}
                      {" • "}
                      {report.time_period}
                      {report.created_at &&
                        ` • ${formatDate(report.created_at)}`}
                    </p>

                    {expanded && (
                      <div className="history-card-details">
                        <div className="result-row">
                          <span>Confidence</span>
                          <span>
                            {report.confidence != null
                              ? `${(report.confidence * 100).toFixed(1)}%`
                              : "N/A"}
                          </span>
                        </div>

                        <div className="result-row">
                          <span>Legal Limit</span>
                          <span>
                            {report.legal_limit != null
                              ? `${report.legal_limit} dB`
                              : "N/A"}
                          </span>
                        </div>

                        <div className="result-row">
                          <span>Exceedance</span>
                          <span>
                            {report.exceedance != null
                              ? `${report.exceedance} dB`
                              : "N/A"}
                          </span>
                        </div>

                        <div className="result-row">
                          <span>Risk Score</span>
                          <span>
                            {report.risk_score != null
                              ? `${report.risk_score}/100`
                              : "N/A"}
                          </span>
                        </div>

                        {report.recommendation && (
                          <p
                            className="result-recommendation"
                            style={{ marginTop: 12 }}
                          >
                            {report.recommendation}
                          </p>
                        )}

                        <div className="btn-row">
                          <button
                            className="btn-dark"
                            onClick={() => downloadReport(report.id)}
                          >
                            Download PDF
                          </button>
                        </div>
                      </div>
                    )}

                    <button
                      className="history-toggle"
                      onClick={() => setExpandedId(expanded ? null : report.id)}
                    >
                      {expanded ? "Hide details" : "View details"}
                    </button>
                  </article>
                );
              })}
            </div>
          )}
        </>
      )}
    </div>
  );
}

export default HistoryPage;
