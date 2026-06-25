import { useEffect, useState } from "react";
import { getHistory } from "../services/api";

function HistoryPage() {
  const [reports, setReports] = useState([]);
  const [viewMode, setViewMode] = useState("grid");

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
    .sort((a, b) => {
      if (sortOrder === "asc") {
        return a.id - b.id;
      }

      return b.id - a.id;
    });

  return (
    <div className="page">
      <h1>Analysis History</h1>

      <div style={filters}>
        <select
          value={venueFilter}
          onChange={(e) => setVenueFilter(e.target.value)}
        >
          <option value="All">All Venues</option>
          <option value="Residential Zone">Residential Zone</option>
          <option value="Commercial Zone">Commercial Zone</option>
          <option value="Industrial Zone">Industrial Zone</option>
          <option value="Quiet Zone">Quiet Zone</option>
          <option value="Special Quiet Zone">Special Quiet Zone</option>
          <option value="Soundproof Venue">Soundproof Venue</option>
          <option value="Non-Soundproof Venue">Non-Soundproof Venue</option>
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

      <div style={cardGrid}>
        {filteredReports.map((report) => (
          <div key={report.id} style={card}>
            <h2>{report.source}</h2>

            <h1>{report.estimated_db} dB</h1>

            <p>
              <strong>Severity:</strong> {report.severity}
            </p>

            <p>
              <strong>Status:</strong> {report.status}
            </p>

            <hr />

            <p>{report.venue_type}</p>

            <p>{report.time_period}</p>

            <p>Risk Score: {report.risk_score ?? "N/A"}</p>

            <p style={dateText}>
              {report.created_at
                ? new Date(report.created_at).toLocaleString()
                : "N/A"}
            </p>

            <button>View Report</button>
          </div>
        ))}
      </div>
    </div>
  );
}

const filters = {
  display: "flex",
  gap: "10px",
  marginBottom: "20px",
};

const cardGrid = {
  display: "grid",
  gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))",
  gap: "20px",
};

const card = {
  background: "#ffffff",
  borderRadius: "12px",
  padding: "20px",
  boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
};

const dateText = {
  fontSize: "12px",
  color: "#666",
  marginTop: "10px",
};

export default HistoryPage;
