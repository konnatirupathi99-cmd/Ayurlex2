# AYURLEX Deployment Guide

## Prototype (V0.1) Deployment

The prototype is designed to run locally or on a single small VM without requiring expensive cloud infrastructure.

### Prerequisites
- Python 3.9+
- Node.js 18+
- SQLite (built-in)

### Step 1: Clone and Configure
1. Clone the repository to the target server.
2. Navigate to `backend` and copy `.env.example` to `.env`.
3. Provide an `LLM_API_KEY` (e.g., Gemini or OpenAI).

### Step 2: Backend (FastAPI)
1. `cd backend`
2. Create virtualenv: `python -m venv venv`
3. Activate: `source venv/bin/activate` or `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the server: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

### Step 3: Frontend (Next.js)
1. `cd frontend`
2. `npm install`
3. Build for production: `npm run build`
4. Start Next.js server: `npm start`

### Step 4: Accessing
Navigate to the server's IP address on port 3000 to access the UI.

## Future Production Deployment (V1.1+)
- **Database**: Migrate from SQLite to Managed PostgreSQL.
- **Vector DB**: Migrate from local Chroma to Pinecone or managed ChromaDB.
- **Frontend**: Deploy on Vercel or AWS Amplify.
- **Backend**: Containerize using the provided `docker-compose.yml` and deploy via ECS, GKE, or a standard VPS with Docker.
