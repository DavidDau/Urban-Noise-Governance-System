from io import BytesIO

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

from app.dependencies import get_db
from app.models.report import AnalysisReport

router = APIRouter()


@router.get("/download/{report_id}")
def download_report(
    report_id: int,
    db: Session = Depends(get_db)
):

    report = (
        db.query(AnalysisReport)
        .filter(AnalysisReport.id == report_id)
        .first()
    )

    if report is None:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    buffer = BytesIO()

    document = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Urban Noise Analysis Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Report ID:</b> {report.id}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Date:</b> {report.created_at}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"<b>Noise Source:</b> {report.source}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Confidence:</b> {report.confidence:.2%}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Estimated Noise Level:</b> {report.estimated_db} dB", styles["BodyText"]))
    story.append(Paragraph(f"<b>Severity:</b> {report.severity}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"<b>Venue Type:</b> {report.venue_type}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Time Period:</b> {report.time_period}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"<b>Legal Limit:</b> {report.legal_limit} dB", styles["BodyText"]))
    story.append(Paragraph(f"<b>Status:</b> {report.status}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Exceedance:</b> {report.exceedance} dB", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph(f"<b>Risk Score:</b> {report.risk_score}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Risk Level:</b> {report.risk_level}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Recommendation</b>", styles["Heading2"]))
    story.append(Paragraph(report.recommendation, styles["BodyText"]))

    document.build(story)

    buffer.seek(0)

    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            f"attachment; filename=report_{report.id}.pdf"
        },
    )