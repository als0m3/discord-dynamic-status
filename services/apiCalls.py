import json
import requests

DISCORD_API_URL = "https://discord.com/api/v9/users/@me/settings"
USER_TOKEN = "YOUR_TOKEN"


def setStatus(text, status):
    payload = json.dumps({
        "status": status,
        "custom_status": {
            "text": text
        }
    })
    headers = {
        'Authorization': USER_TOKEN,
        'Content-Type': 'application/json',
    }

    response = requests.request(
        "PATCH", DISCORD_API_URL, headers=headers, data=payload)
