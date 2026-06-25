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

    if (!file) {
      alert("Please upload a WAV file.");
      return;
    }

    if (!recordingTime) {
      alert("Please select recording time.");
      return;
    }

    const formData = new FormData();

    formData.append("file", file);
    formData.append("venue_type", venueType);
    formData.append("recording_time", recordingTime);

    try {
      setLoading(true);
      console.log(venueType);
      console.log(recordingTime);
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
          <label>Audio File (.wav)</label>
          <br />

          <input
            type="file"
            accept=".wav"
            onChange={(e) => setFile(e.target.files[0])}
          />
        </div>

        <br />

        <div>
          <label>Venue Type</label>
          <br />

          <select
            value={venueType}
            onChange={(e) => setVenueType(e.target.value)}
          >
            <option value="Residential Zone">Residential Zone</option>

            <option value="Commercial Zone">Commercial Zone</option>

            <option value="Industrial Zone">Industrial Zone</option>

            <option value="Quiet Zone">Quiet Zone</option>

            <option value="Special Quiet Zone">Special Quiet Zone</option>

            <option value="Soundproof Venue">Soundproof Venue</option>

            <option value="Non-Soundproof Venue">Non-Soundproof Venue</option>
          </select>
        </div>

        <br />

        <div>
          <label>Recording Time</label>
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
