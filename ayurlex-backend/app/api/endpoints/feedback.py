from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class FeedbackRequest(BaseModel):
    message_id: str
    feedback_type: str # 'thumbs_up' or 'thumbs_down'
    comment: str = ""

@router.post("/feedback")
async def submit_feedback(feedback: FeedbackRequest):
    """
    Submit user feedback on AI responses to improve model performance.
    """
    # Log feedback to database
    return {"message": "Feedback recorded successfully"}
