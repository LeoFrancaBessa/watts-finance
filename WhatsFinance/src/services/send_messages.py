import requests


def send_message(to : str, template_name : str):
    headers = {'Authorization': 'Bearer EAAV8aQXqxK0BO3GIrfcZCHNFZB9ZCQVmk16XKESAeblPaMBBZBul2ltuidogIqIZCyzxjVidd3xpxPqgBiGNtDWgstsoZBBJvkmzma5nSZCeedqyJ1YOAh6poUB4wvCFwguerCaZAIMU7BrgR6LjCsAHTiRULb1qpmZCL14YxFxPkZA2crgTzsGEEZACEtwtWJAg4iKwqySLcbH8ZCi9XW4NshgSmSufoNIZD',
            'Content-Type': 'application/json'}
    body = { "messaging_product": "whatsapp", 
            "to": to, 
            "type": "template", 
            "template": { "name": template_name, 
                        "language": { "code": "pt_BR" } } }

    r = requests.post(url='https://graph.facebook.com/v21.0/488477227690162/messages', headers=headers, json=body)
    return r