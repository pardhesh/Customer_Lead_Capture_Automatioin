from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import inquiry,admin


app = FastAPI(title="AEC Lead Automation")

#for stopping the error in front end
#will check on this after
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
