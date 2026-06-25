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
          Loading history…
        </div>
      </div>
    );
  }

  return (
    <div className="page">
      <header className="page-header">
        <h1>Analysis history</h1>
        <p>Past noise analyses with compliance status and governance scores.</p>
      </header>

      {reports.length === 0 ? (
        <EmptyState
          icon="📂"
          title="No analyses yet"
          message="Your completed noise analyses will appear here. Upload your first recording to get started."
        />
      ) : (
        <>
          <div className="filter-bar">
            <select
              value={venueFilter}
              onChange={(e) => setVenueFilter(e.target.value)}
              aria-label="Filter by venue"
            >
              {VENUE_OPTIONS.map((v) => (
                <option key={v} value={v}>
                  {v === "All" ? "All venues" : v}
                </option>
              ))}
            </select>
            <select
              value={timeFilter}
              onChange={(e) => setTimeFilter(e.target.value)}
              aria-label="Filter by time period"
            >
              <option value="All">All times</option>
              <option value="Day">Day</option>
              <option value="Night">Night</option>
            </select>
            <select
              value={sortOrder}
              onChange={(e) => setSortOrder(e.target.value)}
              aria-label="Sort order"
            >
              <option value="desc">Newest first</option>
              <option value="asc">Oldest first</option>
            </select>
          </div>

          {filteredReports.length === 0 ? (
            <EmptyState
              icon="🔎"
              title="No matching reports"
              message="Try adjusting your filters or run a new analysis."
            />
          ) : (
            <div className="history-grid">
              {filteredReports.map((report) => {
                const isExpanded = expandedId === report.id;
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
                      {report.venue_type} · {report.time_period}
                      {report.created_at &&
                        ` · ${new Date(report.created_at).toLocaleString()}`}
                    </p>

                    {isExpanded && (
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
                          <span>Legal limit</span>
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
                          <span>Risk score</span>
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
                            type="button"
                            className="btn-dark"
                            onClick={() => downloadReport(report.id)}
                          >
                            Download PDF
                          </button>
                        </div>
                      </div>
                    )}

                    <button
                      type="button"
                      className="history-toggle"
                      onClick={() =>
                        setExpandedId(isExpanded ? null : report.id)
                      }
                      aria-expanded={isExpanded}
                    >
                      {isExpanded ? "Hide details" : "View details"}
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
