from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Lead
from ..schemas import LeadCreate, LeadResponse
from ..workflows.lead_workflow import start_lead_workflow


router = APIRouter(prefix="/inquiry", tags=["Inquiry"])


@router.post("/", response_model=LeadResponse)
def create_inquiry(lead: LeadCreate, db: Session = Depends(get_db)):
    new_lead = Lead(
        name=lead.name,
        email=lead.email,
        product=lead.product,
        message=lead.message,
        status="NEW"
    )

    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)

    # Mastra workflow will be triggered here later
    start_lead_workflow(new_lead.id)
    return new_lead
