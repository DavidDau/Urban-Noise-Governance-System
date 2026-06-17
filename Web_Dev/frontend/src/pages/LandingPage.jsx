import { useNavigate } from "react-router-dom";

function LandingPage() {
  const navigate = useNavigate();

  return (
    <div className="page">
      <h1>Urban Noise Governance System</h1>

      <p>
        Machine Learning-Based Context-Aware Urban Acoustic Event Classification
        for Smart Noise Governance
      </p>

      <button onClick={() => navigate("/analyze")}>Start Analysis</button>
    </div>
  );
}

export default LandingPage;
