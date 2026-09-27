from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/sources/{source_id}")
async def get_source(source_id: str):
    """
    Retrieve full details of a specific source or citation by ID.
    """
    if source_id == "src1":
        return {
            "id": source_id,
            "title": "Charaka Samhita, Sutrasthana",
            "content": "Full text or detailed structured data of the source goes here.",
            "url": "https://example.com/charaka",
            "metadata": {"author": "Agnivesa", "redactor": "Charaka"}
        }
    raise HTTPException(status_code=404, detail="Source not found")
