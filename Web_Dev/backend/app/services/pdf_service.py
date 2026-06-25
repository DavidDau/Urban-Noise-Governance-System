from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report, filepath):

    doc = SimpleDocTemplate(filepath)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Urban Noise Governance Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Source: {report.source}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Noise Level: {report.estimated_db} dB",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Severity: {report.severity}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Venue: {report.venue_type}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Period: {report.time_period}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Compliance Status: {report.status}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Recommendation: {report.recommendation}",
            styles["Normal"]
        )
    )

    doc.build(content)
