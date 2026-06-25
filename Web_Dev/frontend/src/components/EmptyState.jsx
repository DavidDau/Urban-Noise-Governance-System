import { Link } from "react-router-dom";

function EmptyState({ icon = "📋", title, message }) {
  return (
    <div className="empty-state">
      <div className="empty-state-icon" aria-hidden="true">
        {icon}
      </div>
      <h2>{title}</h2>
      <p>{message}</p>
      <Link to="/analyze" className="primary-btn">
        Start analysis
      </Link>
    </div>
  );
}

export default EmptyState;
