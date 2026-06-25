import { useRef, useState } from "react";

function FileDropzone({ file, onFileChange, accept = ".wav" }) {
  const inputRef = useRef(null);
  const [dragging, setDragging] = useState(false);

  const handleFiles = (files) => {
    const selected = files?.[0];
    if (selected) onFileChange(selected);
  };

  const onDrop = (e) => {
    e.preventDefault();
    setDragging(false);
    handleFiles(e.dataTransfer.files);
  };

  return (
    <div
      className={`dropzone ${dragging ? "dropzone--active" : ""} ${file ? "dropzone--filled" : ""}`}
      onClick={() => inputRef.current?.click()}
      onDragOver={(e) => {
        e.preventDefault();
        setDragging(true);
      }}
      onDragLeave={() => setDragging(false)}
      onDrop={onDrop}
      role="button"
      tabIndex={0}
      onKeyDown={(e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          inputRef.current?.click();
        }
      }}
    >
      <input
        ref={inputRef}
        type="file"
        accept={accept}
        className="dropzone-input"
        onChange={(e) => handleFiles(e.target.files)}
      />
      <div className="dropzone-icon" aria-hidden="true">
        🎙️
      </div>
      <p className="dropzone-title">
        {file ? "File ready" : "Drop your audio file here"}
      </p>
      <p className="dropzone-hint">WAV format · or click to browse</p>
      {file && <p className="dropzone-file">{file.name}</p>}
    </div>
  );
}

export default FileDropzone;
