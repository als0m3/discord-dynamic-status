import json
import os
import requests

DISCORD_API_URL = "https://discord.com/api/v9/users/@me/settings"
USER_TOKEN = os.environ.get("DISCORD_USER_TOKEN")


def setStatus(text, status):
    if not USER_TOKEN:
        raise RuntimeError("Set DISCORD_USER_TOKEN before starting the program.")
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
        "PATCH", DISCORD_API_URL, headers=headers, data=payload, timeout=15)
    response.raise_for_status()
