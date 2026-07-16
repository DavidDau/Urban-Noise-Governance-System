import { useEffect, useState } from "react";
import { getDashboard } from "../services/api";
import StatusBadge from "../components/StatusBadge";
import EmptyState from "../components/EmptyState";

function DashboardPage() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [viewMode, setViewMode] = useState("grid");

  useEffect(() => {
    const loadDashboard = async () => {
      try {
        const response = await getDashboard();
        setData(response);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    };
    loadDashboard();
  }, []);

  if (loading) {
    return (
      <div className="page">
        <div className="page-loading">
          <span className="spinner" aria-hidden="true" />
          Loading dashboard…
        </div>
      </div>
    );
  }

  const reports = data?.recent_reports ?? [];
  const isEmpty = (data?.total_reports ?? 0) === 0;

  return (
    <div className="page">
      <header className="page-header">
        <h1>Dashboard</h1>
        <p>
          Overview of noise analyses, compliance trends, and recent reports.
        </p>
      </header>

      {isEmpty ? (
        <EmptyState
          icon="📊"
          title="No data to display"
          message="Run your first noise analysis to populate the dashboard with insights and trends."
        />
      ) : (
        <>
          <div className="stats-grid">
            <div className="stat-card">
              <p className="stat-card-label">Total reports</p>
              <p className="stat-card-value">{data.total_reports}</p>
            </div>
            <div className="stat-card">
              <p className="stat-card-label">Average noise</p>
              <p className="stat-card-value stat-card-value--accent">
                {data.average_noise_db} dB
              </p>
            </div>
            <div className="stat-card">
              <p className="stat-card-label">Most common source</p>
              <p className="stat-card-value" style={{ fontSize: "1.35rem" }}>
                {data.most_common_source}
              </p>
            </div>
            <div className="stat-card">
              <p className="stat-card-label">Compliance rate</p>
              <p className="stat-card-value">{data.compliance_rate}%</p>
            </div>
          </div>

          <div className="section-toolbar">
            <h2>Recent reports</h2>
            <button
              type="button"
              className="btn-ghost"
              onClick={() => setViewMode(viewMode === "grid" ? "list" : "grid")}
            >
              {viewMode === "grid" ? "List view" : "Grid view"}
            </button>
          </div>

          <div className={viewMode === "grid" ? "report-grid" : "report-list"}>
            {reports.map((report) =>
              viewMode === "grid" ? (
                <article key={report.id} className="report-item">
                  <p className="report-item-source">{report.source}</p>
                  <p className="report-item-meta">{report.estimated_db} dB</p>
                  <div style={{ margin: "8px 0" }}>
                    <StatusBadge label={report.severity} type="severity" />
                  </div>
                  <StatusBadge label={report.status} type="status" />
                  <p className="report-item-meta" style={{ marginTop: 8 }}>
                    {report.venue_type}
                  </p>
                </article>
              ) : (
                <article
                  key={report.id}
                  className="report-item report-item--row"
                >
                  <span className="report-item-source">{report.source}</span>
                  <span className="report-item-meta">
                    {report.estimated_db} dB
                  </span>
                  <StatusBadge label={report.severity} type="severity" />
                  <StatusBadge label={report.status} type="status" />
                  <span className="report-item-meta">{report.venue_type}</span>
                </article>
              ),
            )}
          </div>
        </>
      )}
    </div>
  );
}

export default DashboardPage;
