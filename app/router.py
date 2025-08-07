from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
import os, requests

router = APIRouter()

class PingRequest(BaseModel):
    pr: int
    repo: str
    comment_url: HttpUrl

@router.get("/health")
async def health():
    return {"status": "healthy"}

@router.post("/ping")
async def ping(request: PingRequest):
    github_token = os.environ.get("GITHUB_TOKEN")
    if not github_token:
        raise HTTPException(status_code=500, detail="GITHUB_TOKEN environment variable not set")
    
    try:
        response = requests.post(
            str(request.comment_url),
            headers={"Authorization": f"token {github_token}"},
            json={"body": "pong"},
            timeout=30
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to post comment: {str(e)}")
    
    return {"status": "sent"}
