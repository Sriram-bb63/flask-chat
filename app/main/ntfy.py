import requests

def ntfy(message):
    requests.post(
        "https://ntfy.sh/Flask-SocketIO-Chat", 
        data=message.encode(encoding='utf-8')
    )