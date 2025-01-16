import requests
from dotenv import load_dotenv
import os

load_dotenv()

def send_message(to : str, template_name : str):
    headers = {'Authorization': f'Bearer {os.getenv("META_ACCESS_TOKEN")}',
            'Content-Type': 'application/json'}
    body = { "messaging_product": "whatsapp", 
            "to": to, 
            "type": "template", 
            "template": { "name": template_name, 
                        "language": { "code": "pt_BR" } } }

    r = requests.post(url=f'https://graph.facebook.com/v21.0/{os.getenv("META_PHONE_NUMBER_ID")}/messages', headers=headers, json=body)
    return r