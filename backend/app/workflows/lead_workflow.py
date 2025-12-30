from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Lead
from ..services.ai_classifier import classify_lead
from ..services.auto_response import get_auto_response
from ..services.lead_service import update_lead_category, update_lead_status


def start_lead_workflow(lead_id: int):
    """
    Entry point for Mastra-like workflow.
    """
    db: Session = SessionLocal()

    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        db.close()
        return

    # STEP 1: AI Categorization
    result = classify_lead(lead.message)
    update_lead_category(db, lead, result["category"])


    # STEP 2: Branch workflow
    if lead.category == "Hot Lead":
        handle_hot_lead(lead, db)
    elif lead.category == "Medium Lead":
        handle_medium_lead(lead, db)
    elif lead.category == "Low Lead":
        handle_low_lead(lead, db)
    else:
        handle_support_lead(lead, db)

    db.close()


def handle_hot_lead(lead: Lead, db: Session):
    message = get_auto_response("Hot Lead")
    print(f"[Auto-response] {message}")

    update_lead_status(db, lead, "AUTO_RESPONDED")

    print(f"[Mastra] Hot lead {lead.id}: Auto-response sent")
    print("[Mastra] Waiting 12 hours for human action...")

    

def handle_medium_lead(lead: Lead, db: Session):
    message = get_auto_response("Medium Lead")
    print(f"[Auto-response] {message}")

    update_lead_status(db, lead, "INFO_SENT")

    print(f"[Mastra] Medium lead {lead.id}: Info sent")
    print("[Mastra] Waiting 24 hours for optional follow-up...")


def handle_low_lead(lead: Lead, db: Session):
    message = get_auto_response("Low Lead")
    print(f"[Auto-response] {message}")

    update_lead_status(db, lead, "INFO_SENT")

    print(f"[Mastra] Low lead {lead.id}: Info sent")
    print("[Mastra] Workflow ended")


def handle_support_lead(lead: Lead, db: Session):
    message = get_auto_response("Support Lead")
    print(f"[Auto-response] {message}")

    update_lead_status(db, lead, "SUPPORT_ROUTED")

    print(f"[Mastra] Support inquiry {lead.id}: Routed to support")
    print("[Mastra] Workflow ended")

def check_follow_up(lead_id: int):
    db = SessionLocal()
    lead = db.query(Lead).filter(Lead.id == lead_id).first()

    if not lead:
        db.close()
        return

    if lead.status != "CONTACTED":
        lead.status = "NEEDS_ATTENTION"
        db.commit()
        print(f"[Mastra] Follow-up triggered for lead {lead.id}")
    else:
        print(f"[Mastra] Lead {lead.id} already contacted")

    db.close()