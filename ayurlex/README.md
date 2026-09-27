# AYURLEX V0.1

**Evidence-Grounded Ayurveda, IP & Regulatory Intelligence Assistant**

AYURLEX is an AI-assisted research and intelligence system for Ayurveda, Traditional Knowledge, Intellectual Property, and Regulatory Research.

## Core Principles
AYURLEX is NOT a replacement for legal professionals, patent examiners, or regulatory authorities. All outputs clearly distinguish retrieved evidence from interpretation, cite sources, and note evidence gaps.

## Demo Instructions (Government / Institutional)

### Workflow 1: Ayurvedic Terminology Intelligence
1. Open the UI, select "Research Mode".
2. Type a query in English, Hindi, or Telugu (e.g., "What is Ashwagandha used for?").
3. Observe the "TERMINOLOGY IDENTIFIED" step.
4. The response will cite the Ayurvedic Pharmacopoeia.

### Workflow 2: IP / Prior-Art Intelligence
1. Ensure Research Mode is ON.
2. Ask: "Can I patent the use of turmeric for wound healing in the US?"
3. The system maps jurisdiction, searches knowledge base, and retrieves the CSIR TKDL case study, stating that traditional knowledge is prior art.

### Workflow 3: Regulatory Intelligence
1. Ask: "What are the regulatory acts for proprietary medicines?"
2. The system retrieves and cites the "Drugs and Cosmetics Act, 1940".

## Features & Implementation Status
For a detailed feature matrix, see [docs/architecture.md](docs/architecture.md).

- **Frontend**: Next.js, React, Tailwind CSS (Botanical dark theme)
- **Backend**: Python, FastAPI, SQLAlchemy
- **Vector Database**: ChromaDB (Local)
- **LLM Abstraction**: Configurable (Gemini 2.5 Flash used for demo)

## Quick Start

### Backend
1. `cd backend`
2. `python -m venv venv` and activate it.
3. `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and set `LLM_API_KEY`.
5. Run ingestion: `python scripts/ingest_documents.py`
6. Run API: `uvicorn app.main:app --reload`

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run dev`
4. Open `http://localhost:3000`

## Documentation
- [Architecture](docs/architecture.md)
- [Evaluation Strategy](docs/evaluation.md)
- [Deployment](docs/deployment.md)
