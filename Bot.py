from pyrogram import Client, filters
import os
import re

# 🔐 Variables d’environnement
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# 📡 ID du canal source et destination
SOURCE_CHANNEL_ID = int(os.getenv("SOURCE_CHANNEL_ID"))
DEST_CHANNEL_ID = int(os.getenv("DEST_CHANNEL_ID"))

# 🔗 Lien personnalisé à insérer
CUSTOM_LINK = os.getenv("CUSTOM_LINK")

# 🎯 Détection de messages pertinents
def is_relevant_message(text):
    keywords = [
        "signal",
        "début de session",
        "fin de session"
    ]
    return any(keyword.lower() in text.lower() for keyword in keywords)

# 🔗 Suppression des anciens liens et ajout du lien personnalisé
def clean_message(text):
    # Supprime tous les liens (http, https, t.me, etc.)
    text = re.sub(r'http[s]?://\S+', '', text)
    # Ajoute ton lien à la fin
    return f"{text.strip()}\n\n👉 {CUSTOM_LINK}"

# ⚙️ Initialisation du bot
app = Client("signal_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# 📥 Surveillance des messages du canal source
@app.on_message(filters.chat(SOURCE_CHANNEL_ID))
def forward_signal(client, message):
    if message.text and is_relevant_message(message.text):
        cleaned = clean_message(message.text)
        client.send_message(DEST_CHANNEL_ID, cleaned)

# ▶️ Démarrage
app.run()
