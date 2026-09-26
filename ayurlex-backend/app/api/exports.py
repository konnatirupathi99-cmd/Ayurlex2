from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import List
import io
import csv

from app.api.auth import require_user
from app.models.auth import User
from app.db.database import DatabaseInterface

router = APIRouter()

@router.get("/csv/{report_id}")
async def export_report_csv(report_id: str, user: User = Depends(require_user)):
    """Export Jurisdiction comparison data to valid CSV."""
    reports = DatabaseInterface.get_reports_by_user(user.internal_id)
    report = next((r for r in reports if r['id'] == report_id), None)
    
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")
        
    payload = report.get('payload', {})
    
    # Mock CSV generation based on payload
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Jurisdiction", "Status", "Details"])
    
    # Example parsing from Jurisdiction comparison payload
    if isinstance(payload, dict):
        for jurisdiction, data in payload.items():
            if isinstance(data, dict):
                writer.writerow([jurisdiction, data.get("status", ""), data.get("details", "")])
            else:
                writer.writerow([jurisdiction, str(data), ""])
                
    response = Response(content=output.getvalue(), media_type="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename=export_{report_id}.csv"
    return response

@router.get("/pdf/{report_id}")
async def export_report_pdf(report_id: str, user: User = Depends(require_user)):
    """Export Jurisdiction comparison data to print-ready PDF output."""
    reports = DatabaseInterface.get_reports_by_user(user.internal_id)
    report = next((r for r in reports if r['id'] == report_id), None)
    
    if not report:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")
        
    # In a real app, use reportlab or weasyprint to generate PDF
    # Mocking PDF binary content for now
    pdf_content = b"%PDF-1.4\n%Mock PDF Content for " + report['title'].encode('utf-8')
    
    response = Response(content=pdf_content, media_type="application/pdf")
    response.headers["Content-Disposition"] = f"attachment; filename=export_{report_id}.pdf"
    return response
