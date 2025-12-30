# Customer_Lead_Capture_Automatioin

An AI-assisted lead capture and automation system designed for AEC (Architecture, Engineering, and Construction) material brands to ensure no website inquiry is lost and every lead is handled in a timely and structured manner.

## Problem Statement
Some brands invest heavily in marketing, but a significant portion of inbound inquiries are lost due to:

Delayed responses

No lead prioritization

Lack of follow-up systems

Poor visibility into inquiry status

This project addresses these issues by introducing an automated yet human-controlled lead management workflow.

## Solution Overview
The system captures website inquiries, categorizes them using AI, sends automated acknowledgments, and provides an admin dashboard for human-in-the-loop follow-ups.

Key Features

Website inquiry capture

AI-based lead categorization

Automated initial responses

Human-in-the-loop admin dashboard

Manual follow-up triggering

End-to-end lead lifecycle visibility

## Architecture Overview
```
Website (HTML Form)
        |
        v
FastAPI Backend
        |
        |-- AI Lead Categorization (Groq LLM)
        |
        |-- Workflow Orchestration
        |
        |-- SQLite Database
        |
        v
Admin Dashboard (Human-in-the-loop)

```

## Lead Categories
```
| Category     | Description                                           |
|-------------|-------------------------------------------------------|
| Hot Lead    | High purchase intent (pricing, timelines, commercial) |
| Medium Lead | Product exploration or catalog requests               |
| Low Lead    | Informational or browsing inquiries                   |
| Support     | Post-sales or support queries                         |
```

## Tech Stack
### Backend
FastAPI

Python

SQLAlchemy

SQLite

Groq LLM (AI categorization)

### Frontend
HTML

CSS

Vanilla JavaScript

### Deployment
Backend: Render (Free Tier)

## Setup Instructions

### Prerequisites
Python 3.9+

Git

Groq API Key

## Backend Setup
```
git clone https://github.com/pardhesh/Customer_Lead_Capture_Automation.git
cd Customer_Lead_Capture_Automation/backend

pip install -r requirements.txt
```
Set environment variable:
```
export GROQ_API_KEY="your_groq_api_key"
```
Start the server:
```
uvicorn app.main:app --reload
```
Backend runs at:
```
http://localhost:8000
```
## Frontend Setup
Open the following files directly in your browser:
```
frontend/index.html
frontend/admin.html
```
Ensure frontend API URLs point to the correct backend.

## API Endpoints
### Create Inquiry
```
POST /inquiry/
```
### Get All Leads (Admin)
```
GET /admin/leads
```
### Mark Lead Contacted
```
POST /admin/leads/{id}/mark-contacted
```
### Trigger Follow-up
```
POST /admin/leads/{id}/trigger-follow-up
```
### Workflow Logic
```
1. Inquiry submitted via website
2. Lead stored in database
3. AI categorizes inquiry
4. Automated acknowledgment triggered
5. Lead status updated
6. Admin reviews leads
7. Admin triggers follow-ups
```

## Evaluation Results
All inquiries are captured reliably

AI categorization improves prioritization

Immediate acknowledgment reduces response delays

Human-in-the-loop ensures quality control

System works end-to-end without paid services
