import { useTheme } from "../context/ThemeContext";

function ThemeToggle() {
  const { theme, toggleTheme } = useTheme();

  return (
    <label className="theme-toggle-switch" aria-label="Toggle dark mode">
      <input
        type="checkbox"
        checked={theme === "dark"}
        onChange={toggleTheme}
      />
      <span className="theme-toggle-slider"></span>
    </label>
  );
}

export default ThemeToggle;
