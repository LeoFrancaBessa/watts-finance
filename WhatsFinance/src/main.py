from flask import Flask, request
from models.messages_received import MessagesReceived

app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET':  # Verificação do Webhook
        verify_token = "58809e614c0491b273aff7eeaf21d3e070c9a89b"  # Token configurado no Meta
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if mode == 'subscribe' and token == verify_token:
            return challenge, 200
        else:
            return 'Erro de validação', 403
    if request.method == 'POST':
        messagereceive = MessagesReceived(request.json)
        print(messagereceive.get_object())
        return 'sucess', 200

app.run('0.0.0.0', port='8080')