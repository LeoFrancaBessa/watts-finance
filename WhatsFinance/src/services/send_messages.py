import requests


def send_message(to : str):
    headers = {'Authorization': 'Bearer EAAV8aQXqxK0BO9do08vZAN4vv0VkztWV90KVKDkIzI0cI0yAb5rkJL3l0fYeaB00eoj2woSCh5DWlkbPVELLABdYtG4X5cRZBs2NiEOWc1KBVOYEX0NR2CKB68tQUiTL8FETD6kw6TgM2Tiofnn7ZBoERohiKZADAslAaGknZBa9o2l6D19YmWgjs4xm7n66ZBDZANogwYZACinfclBPOv8bm8W8S9qk',
            'Content-Type': 'application/json'}
    body = { "messaging_product": "whatsapp", 
            "to": to, 
            "type": "template", 
            "template": { "name": "hello_world", 
                        "language": { "code": "en_US" } } }

    r = requests.post(url='https://graph.facebook.com/v21.0/488477227690162/messages', headers=headers, json=body)
    return r