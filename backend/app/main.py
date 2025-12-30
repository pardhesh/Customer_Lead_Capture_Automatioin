from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import inquiry,admin


app = FastAPI(title="AEC Lead Automation")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       
    allow_credentials=False,
    allow_methods=["*"],        
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(inquiry.router)
app.include_router(admin.router)


@app.get("/")
def health_check():
    return {"status": "running"}
