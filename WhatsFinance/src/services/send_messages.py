import requests


def send_message(to, text):
    headers = {'Authorization': 'Bearer EAAV8aQXqxK0BO3Jd8b48iVK75eFYa3xU9VZAK5VypoqniVaUTCaAt6KsdMGzLuVhPZBnNOVsA5bHrokZCvaXgfavtK6ge7JAsVsORL6XOctVAouNrCFlXRMRJMDamBBVXyLXRbPoy1Ye0yeQ67Sd0h8zTsspTIcIl0PQHBLRbA7N4iJPDZChc1WO86a57hgirDZByDz0jEIfZAUvGuh3F67UTzjv4ZD',
            'Content-Type': 'application/json'}
    body = { "messaging_product": "whatsapp", 
            "to": to, 
            "type": "template", 
            "template": { "name": "hello_world", 
                        "language": { "code": "en_US" } } }

    r = requests.post(url='https://graph.facebook.com/v21.0/488477227690162/messages', headers=headers, json=body)
    return r