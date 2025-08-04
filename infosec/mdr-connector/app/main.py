
app/main.py
from fastapi import FastAPI, Request
import httpx, os
app = FastAPI()

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    async with httpx.AsyncClient() as client:
        await client.post(os.getenv("SLACK_URL"), json={"text": str(data)})
    return {"status": "ok"}