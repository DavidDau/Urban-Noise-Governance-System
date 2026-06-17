import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { analyzeNoise } from "../services/api";

function AnalysisPage() {
  const navigate = useNavigate();

  const [file, setFile] = useState(null);
  const [venueType, setVenueType] = useState("Residential Zone");
  const [recordingTime, setRecordingTime] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file || !recordingTime) {
      alert("Please provide all fields.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("venue_type", venueType);
    formData.append("recording_time", recordingTime);

    try {
      setLoading(true);

      const result = await analyzeNoise(formData);

      navigate("/results", {
        state: result,
      });
    } catch (error) {
      console.error(error);
      alert("Analysis failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <h1>Analyze Noise</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Audio File (.wav):</label>
          <br />
          <input
            type="file"
            accept=".wav"
            onChange={(e) => setFile(e.target.files[0])}
          />
        </div>

        <br />

        <div>
          <label>Venue Type:</label>
          <br />
          <select
            value={venueType}
            onChange={(e) => setVenueType(e.target.value)}
          >
            <option>Residential Zone</option>
            <option>Commercial Zone</option>
            <option>Industrial Zone</option>
            <option>Quiet Zone</option>
            <option>Special Quiet Zone</option>
            <option>Soundproof Venue</option>
            <option>Non-Soundproof Venue</option>
          </select>
        </div>

        <br />

        <div>
          <label>Recording Time:</label>
          <br />
          <input
            type="time"
            value={recordingTime}
            onChange={(e) => setRecordingTime(e.target.value)}
          />
        </div>

        <br />

        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Noise"}
        </button>
      </form>
    </div>
  );
}

export default AnalysisPage;
