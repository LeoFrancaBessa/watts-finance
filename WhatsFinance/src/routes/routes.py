from src.utils.messages_received_utils import MessagesReceivedUtils
from src.services.send_messages import send_message
from fastapi import Query, HTTPException, Request
from src.models.models import MessageReceived, User
from src.models.base_models import UserModel, SendMessageModel
from src.flow import flow
from fastapi import APIRouter

router = APIRouter()

@router.get("/receive-messages")
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


@router.post("/receive-messages")
async def receive_messages(request: Request):
    body = await request.json()
    try:
        messages_received_utils = MessagesReceivedUtils(body)
        message_received = await MessageReceived.create(**messages_received_utils.get_object())
        response_flow = await flow(message_received.contact_phone, message_received.message_body)
        if response_flow:
            await send_messages(message_received.contact_phone, SendMessageModel(template_name=response_flow))
        return {"success": True, "message_received": message_received}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/send-messages/{to}")
async def send_messages(to: str, send_message_model: SendMessageModel):
    template_name = send_message_model.template_name
    r = send_message(to, template_name)
    if r.status_code == 200:
        return {"success": True, "message": "Message sent successfully"}
    else:
        return {"success": False, "message": "Failed to send message", "error": r.text}, r.status_code


@router.post("/create-user")
async def create_user(user_model: UserModel):
    user = await User.create(**user_model.model_dump())
    return {"success": True, "user": user}