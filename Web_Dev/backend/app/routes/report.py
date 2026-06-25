from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/download/{report_id}")
def download_report(report_id: int):

    pdf_path = f"reports/report_{report_id}.pdf"

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=f"noise_report_{report_id}.pdf"
    )
