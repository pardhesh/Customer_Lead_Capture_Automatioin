from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Lead

#some random data

def seed_data():
    db: Session = SessionLocal()


    sample_leads = [
        Lead(
            name="Test Studio",
            email="test@studio.com",
            product="Flooring",
            message="Please share catalogue",
            status="NEW"
            
            
        ),
        Lead(
            
            name="Demo Architects",
            email="demo@arch.com",
            product="Lighting",
            message="Need pricing for commercial project",
            status="NEW"
        )
    ]

    db.add_all(sample_leads)
    db.commit()
    
    db.close()


if __name__ == "__main__":
    seed_data()
