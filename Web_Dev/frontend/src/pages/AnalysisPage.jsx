import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { analyzeNoise } from "../services/api";
import FileDropzone from "../components/FileDropzone";

const VENUE_OPTIONS = [
  "Select venue type",
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
  const [venueType, setVenueType] = useState("Select venue type");
  const [recordingTime, setRecordingTime] = useState("");
  const [loading, setLoading] = useState(false);
  const [errors, setErrors] = useState({});

  const validate = () => {
    const next = {};

    console.log("----- VALIDATION -----");
    console.log("File:", file);
    console.log("Venue:", venueType);
    console.log("Recording time:", recordingTime);

    if (!file) next.file = "Please upload a WAV audio file.";

    if (!recordingTime) next.recordingTime = "Please select a recording time.";

    if (venueType === "Select venue type")
      next.venueType = "Please select a venue type.";

    console.log("Validation errors:", next);

    setErrors(next);

    return Object.keys(next).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    console.log("========== SUBMIT CLICKED ==========");

    if (!validate()) {
      console.log("Validation failed.");
      return;
    }

    console.log("Validation passed.");

    const formData = new FormData();

    formData.append("file", file);
    formData.append("venue_type", venueType);
    formData.append("recording_time", recordingTime);

    console.log("FormData created.");

    for (const pair of formData.entries()) {
      console.log(pair[0], pair[1]);
    }

    try {
      setLoading(true);
      setErrors({});

      console.log("Calling analyzeNoise()...");

      const result = await analyzeNoise(formData);

      console.log("API returned:");
      console.log(result);

      navigate("/results", {
        state: result,
      });
    } catch (err) {
      console.error("Analysis failed:");
      console.error(err);

      if (err.response) {
        console.log("Response status:", err.response.status);
        console.log("Response data:", err.response.data);
      } else if (err.request) {
        console.log("Request sent but no response received.");
        console.log(err.request);
      } else {
        console.log("Axios error:", err.message);
      }

      setErrors({
        form: err.response?.data?.detail || err.message || "Unknown error",
      });
    } finally {
      console.log("Request finished.");
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <header className="page-header">
        <h1>Analyze noise</h1>

        <p>
          Upload a WAV recording, set the venue and time, and get ML-powered
          classification with compliance and governance insights.
        </p>
      </header>

      <form className="form-card" onSubmit={handleSubmit} noValidate>
        <div className="form-group">
          <label className="form-label">Audio file</label>

          <FileDropzone
            file={file}
            onFileChange={(selectedFile) => {
              console.log("Selected file:", selectedFile);
              setFile(selectedFile);
            }}
          />

          {errors.file && <p className="form-error">{errors.file}</p>}
        </div>

        <div className="form-group">
          <label className="form-label">Venue type</label>

          <select
            className="form-select"
            value={venueType}
            onChange={(e) => {
              console.log("Venue selected:", e.target.value);
              setVenueType(e.target.value);
            }}
          >
            {VENUE_OPTIONS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>

          {errors.venueType && <p className="form-error">{errors.venueType}</p>}
        </div>

        <div className="form-group">
          <label className="form-label">Recording time</label>

          <input
            type="time"
            className="form-input"
            value={recordingTime}
            onChange={(e) => {
              console.log("Recording time:", e.target.value);
              setRecordingTime(e.target.value);
            }}
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
              Analyzing...
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
