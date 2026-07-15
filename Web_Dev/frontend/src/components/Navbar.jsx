import { Link, useLocation } from "react-router-dom";
import { useState } from "react";
import { useTheme } from "../context/ThemeContext";
import ThemeToggle from "./ThemeToggle";

function Navbar() {
  const location = useLocation();
  const [menuOpen, setMenuOpen] = useState(false);
  const { theme } = useTheme();

  const links = [
    { to: "/", text: "Home" },
    { to: "/analyze", text: "Analyze" },
    { to: "/history", text: "History" },
    { to: "/dashboard", text: "Dashboard" },
  ];

  return (
    <header className="navbar-wrap">
      <nav className="navbar">
        <Link to="/" className="navbar-logo" onClick={() => setMenuOpen(false)}>
          <img
            src={
              theme === "dark" ? "/UNGS_Logo_dark.svg" : "/UNGS_Logo_light.svg"
            }
            alt="Urban Noise Governance System"
            className="navbar-logo-mark"
          />
          <div className="navbar-logo-text">
            <span className="navbar-logo-short">UNGS</span>
            <span className="navbar-logo-full">
              Urban Noise Governance System
            </span>
          </div>
        </Link>

        <div className={`navbar-links ${menuOpen ? "navbar-links--open" : ""}`}>
          {links.map(({ to, text }) => (
            <Link
              key={to}
              to={to}
              className={`navbar-link ${location.pathname === to ? "navbar-link--active" : ""}`}
              onClick={() => setMenuOpen(false)}
            >
              {text}
            </Link>
          ))}
        </div>

        <div className="navbar-actions">
          <button
            type="button"
            className="navbar-menu-btn"
            aria-label="Toggle menu"
            aria-expanded={menuOpen}
            onClick={() => setMenuOpen((o) => !o)}
          >
            {menuOpen ? "✕" : "☰"}
          </button>
          <ThemeToggle />
          <Link
            to="/analyze"
            className="navbar-cta navbar-cta--short"
            onClick={() => setMenuOpen(false)}
          >
            Start analysis
          </Link>
        </div>
      </nav>
    </header>
  );
}

export default Navbar;
