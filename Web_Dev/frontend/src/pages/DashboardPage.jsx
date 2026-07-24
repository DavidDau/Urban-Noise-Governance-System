{
  /* Top Cards */
}

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
</section>;
