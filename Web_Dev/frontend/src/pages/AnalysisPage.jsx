import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { analyzeNoise } from "../services/api";
import FileDropzone from "../components/FileDropzone";

const VENUE_OPTIONS = [
  "Residential Zone",
  "Commercial Zone",
  "Industrial Zone",
  "Quiet Zone",
  "Special Quiet Zone",
  "Soundproof Venue",
  "Non-Soundproof Venue",
];

function AnalysisPage() {
  const navigate = useNavigate();
  const [file, setFile] = useState(null);
  const [venueType, setVenueType] = useState("Residential Zone");
  const [recordingTime, setRecordingTime] = useState("");
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState({});

  const validate = () => {
    const next = {};
    if (!file) next.file = "Please upload a WAV audio file.";
    if (!recordingTime) next.recordingTime = "Please select a recording time.";
    setErrors(next);
    return Object.keys(next).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validate()) return;

    const formData = new FormData();
    formData.append("file", file);
    formData.append("venue_type", venueType);
    formData.append("recording_time", recordingTime);

    try {
      setLoading(true);
      setErrors({});
      const result = await analyzeNoise(formData);
      navigate("/results", { state: result });
    } catch {
      setErrors({ form: "Analysis failed. Check your file and try again." });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <header className="page-header">
        <h1>Analyze noise</h1>
        <p>
          Upload a WAV recording, set the venue and time, and get AI-powered
          classification with compliance and governance insights.
        </p>
      </header>

      <form className="form-card" onSubmit={handleSubmit} noValidate>
        <div className="form-group">
          <label className="form-label" htmlFor="audio-file">
            Audio file
          </label>
          <FileDropzone file={file} onFileChange={setFile} />
          {errors.file && <p className="form-error">{errors.file}</p>}
        </div>

        <div className="form-group">
          <label className="form-label" htmlFor="venue-type">
            Venue type
          </label>
          <select
            id="venue-type"
            className="form-select"
            value={venueType}
            onChange={(e) => setVenueType(e.target.value)}
          >
            {VENUE_OPTIONS.map((v) => (
              <option key={v} value={v}>
                {v}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label className="form-label" htmlFor="recording-time">
            Recording time
          </label>
          <input
            id="recording-time"
            type="time"
            className="form-input"
            value={recordingTime}
            onChange={(e) => setRecordingTime(e.target.value)}
          />
          {errors.recordingTime && (
            <p className="form-error">{errors.recordingTime}</p>
          )}
        </div>

        {errors.form && <p className="form-error">{errors.form}</p>}

        <button type="submit" className="btn-dark" disabled={loading}>
          {loading ? (
            <span className="spinner-wrap">
              <span className="spinner" aria-hidden="true" />
              Analyzing…
            </span>
          ) : (
            "Run analysis"
          )}
        </button>
      </form>
    </div>
  );
}

export default AnalysisPage;
