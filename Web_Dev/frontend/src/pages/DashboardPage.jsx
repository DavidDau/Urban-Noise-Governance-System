import { useEffect, useState } from "react";
import { getHistory } from "../services/api";

function DashboardPage() {
  const [reports, setReports] = useState([]);
  const [viewMode, setViewMode] = useState("grid");
  useEffect(() => {
    const loadReports = async () => {
      try {
        const data = await getHistory();
        setReports(data);
      } catch (error) {
        console.error(error);
      }
    };

    loadReports();
  }, []);

  const totalReports = reports.length;

  const averageNoise =
    reports.length > 0
      ? (
          reports.reduce((sum, r) => sum + r.estimated_db, 0) / reports.length
        ).toFixed(1)
      : 0;

  const compliantReports = reports.filter(
    (r) => r.status === "Compliant",
  ).length;

  const complianceRate =
    reports.length > 0
      ? ((compliantReports / reports.length) * 100).toFixed(1)
      : 0;

  const sourceCounts = {};

  reports.forEach((r) => {
    sourceCounts[r.source] = (sourceCounts[r.source] || 0) + 1;
  });

  const mostCommonSource =
    Object.keys(sourceCounts).length > 0
      ? Object.keys(sourceCounts).reduce((a, b) =>
          sourceCounts[a] > sourceCounts[b] ? a : b,
        )
      : "N/A";

  return (
    <div className="page">
      <h1>Dashboard Analytics</h1>

      <div style={grid}>
        <div style={card}>
          <h3>Total Reports</h3>
          <h1>{totalReports}</h1>
        </div>

        <div style={card}>
          <h3>Average Noise</h3>
          <h1>{averageNoise} dB</h1>
        </div>

        <div style={card}>
          <h3>Most Common Source</h3>
          <h2>{mostCommonSource}</h2>
        </div>

        <div style={card}>
          <h3>Compliance Rate</h3>
          <h1>{complianceRate}%</h1>
        </div>
      </div>

      <div style={toolbar}>
        <h2>Recent Reports</h2>

        <button
          style={viewButton}
          onClick={() => setViewMode(viewMode === "grid" ? "list" : "grid")}
        >
          {viewMode === "grid" ? "List View" : "Grid View"}
        </button>
      </div>

      <div style={viewMode === "grid" ? reportGrid : reportList}>
        {reports.slice(0, 10).map((report) => (
          <div
            key={report.id}
            style={viewMode === "grid" ? reportCard : reportRow}
          >
            <h3>{report.source}</h3>

            <p>{report.estimated_db} dB</p>

            <p>{report.severity}</p>

            <p>{report.status}</p>

            <p>{report.venue_type}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

const grid = {
  display: "grid",
  gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
  gap: "20px",
  marginBottom: "40px",
};

const card = {
  background: "#fff",
  padding: "20px",
  borderRadius: "12px",
  textAlign: "center",
};

const reportGrid = {
  display: "grid",
  gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))",
  gap: "20px",
};

const reportList = {
  display: "flex",
  flexDirection: "column",
  gap: "12px",
};

const reportRow = {
  background: "#fff",
  padding: "15px",
  borderRadius: "10px",
  display: "grid",
  gridTemplateColumns: "1.5fr 1fr 1fr 1fr 1.5fr",
  alignItems: "center",
};

const toolbar = {
  display: "flex",
  justifyContent: "space-between",
  alignItems: "center",
  marginBottom: "20px",
};

const viewButton = {
  padding: "10px 18px",
  border: "none",
  borderRadius: "8px",
  cursor: "pointer",
  fontWeight: "600",
  background: "#111827",
  color: "#ffffff",
};

const reportCard = {
  background: "#fff",
  padding: "15px",
  borderRadius: "10px",
};

export default DashboardPage;
