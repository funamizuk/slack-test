import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    return "OK", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received:", data)

    # challengeがある場合はその値を返す
    if "challenge" in data:
        return jsonify({"challenge": data["challenge"]}), 200

    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Renderが用意するPORTを取得
    app.run(host="0.0.0.0", port=port)
