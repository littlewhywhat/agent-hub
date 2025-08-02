from fastapi import APIRouter, Request
import os, requests

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "healthy"}

@router.post("/ping")
async def ping(request: Request):
    data = await request.json()
    pr_number = data["pr"]
    repo = data["repo"]
    comment_url = data["comment_url"]

    github_token = os.environ["GITHUB_TOKEN"]

    requests.post(
        comment_url,
        headers={"Authorization": f"token {github_token}"},
        json={"body": "pong"}
    )
    return {"status": "sent"}
