from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.config import REPORTS_DIR

router = APIRouter()


@router.get("/download/{report_id}")
def download_report(report_id: int):

    pdf_path = REPORTS_DIR / f"report_{report_id}.pdf"

    return FileResponse(
        str(pdf_path),
        media_type="application/pdf",
        filename=f"noise_report_{report_id}.pdf"
    )
