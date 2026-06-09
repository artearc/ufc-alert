import requests
import os
from datetime import datetime

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

hora = datetime.utcnow().strftime("%H:%M:%S UTC")

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": f"⏰ Workflow ejecutado: {hora}"
    }
)
