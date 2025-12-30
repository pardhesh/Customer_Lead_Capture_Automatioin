from sqlalchemy.orm import Session
from ..models import Lead


def update_lead_category(db: Session, lead: Lead, category: str):
    lead.category = category
    lead.status = "CATEGORIZED"
    db.commit()


def update_lead_status(db: Session, lead: Lead, status: str):
    lead.status = status
    db.commit()
