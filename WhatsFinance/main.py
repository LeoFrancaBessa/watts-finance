from contextlib import asynccontextmanager
from fastapi import FastAPI, Query, HTTPException, Request
from tortoise import Tortoise
from src.models.models import MessageReceived, MessageSent
from src.utils.messages_received_utils import MessagesReceivedUtils
from src.services.send_messages import send_message

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["src.models.models"]}
    )
    await Tortoise.generate_schemas()
    yield
    # Shutdown
    await Tortoise.close_connections()

app = FastAPI(lifespan=lifespan)

@app.get("/receive-messages")
async def receive_messages(
    hub_mode: str = Query(..., alias="hub.mode"), 
    hub_token: str = Query(..., alias="hub.verify_token"), 
    hub_challenge: str = Query(..., alias="hub.challenge")
):
    verify_token = "58809e614c0491b273aff7eeaf21d3e070c9a89b"
    if hub_mode == "subscribe" and hub_token == verify_token:
        return int(hub_challenge)
    else:
        raise HTTPException(status_code=403, detail="Invalid token")


@app.post("/receive-messages")
async def receive_messages(request: Request):
    body = await request.json()
    try:
        messages_received_utils = MessagesReceivedUtils(body)
        message_received = await MessageReceived.create(**messages_received_utils.get_object())
        return {"success": True, "message_received": message_received}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/send-messages/{to}")
async def send_messages(to: str):
    r = send_message(to)
    if r.status_code == 200:
        return {"success": True, "message": "Message sent successfully"}
    else:
        return {"success": False, "message": "Failed to send message", "error": r.text}, r.status_code
