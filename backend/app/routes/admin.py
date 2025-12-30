from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Lead
from ..workflows.lead_workflow import check_follow_up

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/leads")
def get_all_leads(db: Session = Depends(get_db)):
    leads = db.query(Lead).order_by(Lead.created_at.desc()).all()
    return leads


@router.post("/leads/{lead_id}/mark-contacted")
def mark_lead_contacted(lead_id: int, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()

    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    lead.status = "CONTACTED"
    db.commit()

    return {
        "message": f"Lead {lead_id} marked as CONTACTED"
    }

@router.post("/leads/{lead_id}/trigger-follow-up")
def trigger_follow_up(lead_id: int):
    check_follow_up(lead_id)
    return {"message": f"Follow-up triggered for lead {lead_id}"}