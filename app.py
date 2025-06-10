@app.route("/slack-webhook", methods=["POST"])
def slack_webhook():
    data = request.get_json()
    
    if data.get("type") == "url_verification":
        return data.get("challenge"), 200  # ← Slack検証用
    
    return jsonify(data), 200  # ← 通常はそのままecho
