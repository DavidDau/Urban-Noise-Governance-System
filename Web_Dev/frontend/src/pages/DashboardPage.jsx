import { useEffect, useState } from "react";
import { getDashboard } from "../services/api";
import EmptyState from "../components/EmptyState";

function DashboardPage() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadDashboard = async () => {
      try {
        const response = await getDashboard();
        setData(response);
      } catch (err) {
        console.error(err);
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
          <span className="spinner" />
          Loading dashboard...
        </div>
      </div>
    );
  }

  const totalReports = data?.total_reports ?? 0;

  if (totalReports === 0) {
    return (
      <div className="page">
        <EmptyState
          icon="📊"
          title="No dashboard data"
          message="Run your first analysis to populate the dashboard."
        />
      </div>
    );
  }

  const complianceRate = (
    (data.compliant_reports / totalReports) *
    100
  ).toFixed(1);

  const maxSource = Math.max(...data.sources.map((s) => s.count), 1);

  return (
    <div className="page">
      <header className="page-header">
        <h1>Dashboard</h1>
        <p>Urban Noise Governance Overview</p>
      </header>

      {/* Top Cards */}

      <section className="dashboard-stats">
        <div className="dashboard-card">
          <p className="dashboard-label">Total Analyses</p>
          <div className="dashboard-value">{totalReports}</div>
        </div>

        <div className="dashboard-card">
          <p className="dashboard-label">Average Noise</p>
          <div className="dashboard-value">{data.average_noise_db} dB</div>
        </div>

        <div className="dashboard-card">
          <p className="dashboard-label">Average Risk</p>
          <div className="dashboard-value">{data.average_risk_score}</div>
        </div>

        <div className="dashboard-card">
          <p className="dashboard-label">Compliance Rate</p>
          <div className="dashboard-value">{complianceRate}%</div>
        </div>
      </section>
      {/* Middle Panels */}

      <section className="dashboard-section">
        <div className="dashboard-panel">
          <h3>Detected Noise Sources</h3>

          {data.sources.map((item) => (
            <div key={item.source} className="source-row">
              <div className="source-label">{item.source}</div>

              <div className="source-bar">
                <div
                  className="source-fill"
                  style={{
                    width: `${(item.count / maxSource) * 100}%`,
                  }}
                />
              </div>

              <div className="source-count">{item.count}</div>
            </div>
          ))}
        </div>

        <div className="dashboard-panel">
          <h3>Compliance Summary</h3>

          <div className="recent-report">
            <div className="recent-left">
              <span className="recent-source">Compliant</span>
              <span className="recent-meta">Within legal limits</span>
            </div>

            <strong>{data.compliant_reports}</strong>
          </div>

          <div className="recent-report">
            <div className="recent-left">
              <span className="recent-source">Non-Compliant</span>
              <span className="recent-meta">Above legal limits</span>
            </div>

            <strong>{data.non_compliant_reports}</strong>
          </div>

          <div className="recent-report">
            <div className="recent-left">
              <span className="recent-source">Average Risk</span>
            </div>

            <strong>{data.average_risk_score}</strong>
          </div>
        </div>
      </section>

      {/* Recent Analyses */}

      <section className="dashboard-panel recent-analysis-panel">
        <div className="section-header">
          <h3>Recent Analyses</h3>
        </div>

        <div className="recent-table">
          <div className="recent-header">
            <span>Source</span>
            <span>Noise</span>
            <span>Severity</span>
            <span>Status</span>
            <span>Venue</span>
            <span>Date</span>
          </div>

          {data.recent_reports.map((report) => (
            <div key={report.id} className="recent-row">
              <span>{report.source}</span>

              <span>{report.estimated_db} dB</span>

              <span>{report.severity}</span>

              <span>{report.status}</span>

              <span>{report.venue_type}</span>

              <span>{new Date(report.created_at).toLocaleDateString()}</span>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

export default DashboardPage;
