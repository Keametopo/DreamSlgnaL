from pyrogram import Client, filters
import re

# 🔐 Informations de connexion
api_id = 24354172
api_hash = "9d13f76e75c73e7126fad766268c021f"
bot_token = "7739084760:AAEYsme7r5pi2i_kGZysMGQxLriVFcZRSNg"

# 🟢 ID du canal source et destination
SOURCE_CHANNEL_ID = -1002078184249
DEST_CHANNEL_ID = -1002894104847

# 🔁 Lien personnalisé à insérer
CUSTOM_LINK = "http://bit.ly/4lK5wUR"

# 🎯 Détection de messages pertinents
def is_relevant_message(text):
    keywords = [
        "signal", 
        "entrée", 
        "session", 
        "start", 
        "begin", 
        "end", 
        "TP", 
        "SL"
    ]
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in keywords)

# 🔧 Fonction de nettoyage des liens
def clean_links(text):
    # Supprimer tous les liens
    text = re.sub(r'https?://\S+', CUSTOM_LINK, text)
    return text

# 🔁 Client Pyrogram
app = Client("dream_signal_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# 🎣 Écoute des messages
@app.on_message(filters.chat(SOURCE_CHANNEL_ID))
def forward_filtered(client, message):
    if message.text and is_relevant_message(message.text):
        cleaned_text = clean_links(message.text)
        client.send_message(DEST_CHANNEL_ID, cleaned_text)

# ▶️ Lancement
print("✅ Bot démarré... en attente de messages.")
app.run()
