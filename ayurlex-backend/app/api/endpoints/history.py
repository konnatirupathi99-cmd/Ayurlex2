from fastapi import APIRouter

router = APIRouter()

@router.get("/history")
async def get_history():
    """
    Retrieve user chat and analysis history.
    """
    return [
        {"id": "hist-1", "title": "Ashwagandha Patent Analysis", "date": "2026-09-25T10:00:00Z", "type": "analysis"}
    ]
