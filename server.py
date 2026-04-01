from flask import Flask, request, jsonify
from telethon.sync import TelegramClient

app = Flask(__name__)

# 🔹 Вставь сюда свои данные из App Configuration
api_id = 31907235           # <- твой api_id
api_hash = 'b8b7963d9163d7f63d4e1f2f1c125ee2'  # <- твой api_hash

client = TelegramClient('session', api_id, api_hash)

@app.route('/parse', methods=['POST'])
def parse_channel():
    data = request.json
    channel = data.get('channel')

    if not channel:
        return jsonify({"success": False, "error": "Нет канала"}), 400

    try:
        with client:
            participants = client.get_participants(channel)
            count = len(participants)
        return jsonify({"success": True, "users": count})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
