import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div style={styles.nav}>
      <h3 style={styles.logo}>NoiseGov</h3>

      <div style={styles.links}>
        <Link to="/" style={styles.link}>
          Home
        </Link>
        <Link to="/analyze" style={styles.link}>
          Analyze
        </Link>
        <Link to="/history" style={styles.link}>
          History
        </Link>
        <Link to="/dashboard">Dashboard</Link>
      </div>
    </div>
  );
}

const styles = {
  nav: {
    display: "flex",
    justifyContent: "space-between",
    padding: "12px 20px",
    background: "#111",
    color: "white",
  },
  logo: { margin: 0 },
  links: { display: "flex", gap: "15px" },
  link: { color: "white", textDecoration: "none" },
};

export default Navbar;
