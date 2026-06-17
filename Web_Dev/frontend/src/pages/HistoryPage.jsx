import { useEffect, useState } from "react";

function HistoryPage() {
  const [history, setHistory] = useState([]);
  const [venueFilter, setVenueFilter] = useState("All");
  const [timeFilter, setTimeFilter] = useState("All");
  const [sortOrder, setSortOrder] = useState("desc");

  useEffect(() => {
    const data = JSON.parse(localStorage.getItem("noise_history") || "[]");
    setHistory(data);
  }, []);

  const filtered = history
    .filter((item) => {
      const venueMatch =
        venueFilter === "All" || item.venue_type === venueFilter;

      const timeMatch = timeFilter === "All" || item.time_period === timeFilter;

      return venueMatch && timeMatch;
    })
    .sort((a, b) => {
      if (sortOrder === "asc") {
        return new Date(a.timestamp) - new Date(b.timestamp);
      }
      return new Date(b.timestamp) - new Date(a.timestamp);
    });

  return (
    <div className="page">
      <h1>History</h1>

      {/* Filters */}
      <div style={filters}>
        <select onChange={(e) => setVenueFilter(e.target.value)}>
          <option>All</option>
          <option>Residential Zone</option>
          <option>Commercial Zone</option>
          <option>Industrial Zone</option>
          <option>Quiet Zone</option>
        </select>

        <select onChange={(e) => setTimeFilter(e.target.value)}>
          <option>All</option>
          <option>Day</option>
          <option>Night</option>
        </select>

        <select onChange={(e) => setSortOrder(e.target.value)}>
          <option value="desc">Newest First</option>
          <option value="asc">Oldest First</option>
        </select>
      </div>

      {/* Table */}
      <div style={table}>
        {filtered.map((item, i) => (
          <div key={i} style={row}>
            <p>
              <b>{item.source}</b>
            </p>
            <p>{item.venue_type}</p>
            <p>{item.time_period}</p>
            <p>{item.estimated_db} dB</p>
            <p>{item.status}</p>
            <p>{new Date(item.timestamp).toLocaleString()}</p>
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

const table = {
  display: "flex",
  flexDirection: "column",
  gap: "10px",
};

const row = {
  display: "grid",
  gridTemplateColumns: "1fr 1fr 1fr 1fr 1fr 1fr",
  background: "#fff",
  padding: "10px",
  borderRadius: "8px",
};

export default HistoryPage;
