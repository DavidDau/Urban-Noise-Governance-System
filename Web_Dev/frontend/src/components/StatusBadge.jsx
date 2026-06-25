function getVariant(type, value) {
  const v = (value || "").toLowerCase();

  if (type === "status") {
    if (v === "compliant") return "green";
    if (v.includes("minor") || v.includes("moderate")) return "amber";
    return "coral";
  }

  if (type === "severity") {
    if (v === "low" || v === "minimal") return "green";
    if (v === "medium" || v === "moderate") return "amber";
    return "coral";
  }

  if (type === "risk") {
    if (v === "low") return "green";
    if (v === "medium" || v === "moderate") return "amber";
    return "coral";
  }

  return "amber";
}

function StatusBadge({ label, type = "status" }) {
  const variant = getVariant(type, label);

  return <span className={`badge badge--${variant}`}>{label}</span>;
}

export default StatusBadge;
