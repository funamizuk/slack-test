from flask import Flask, request

app = Flask(__name__)


@app.route('/slack-webhook', methods=['POST'])
def slack_webhook():
    data = request.get_json()
    
    if data.get("type") == "url_verification":
        return data.get("challenge"), 200  # ← Slack検証用
    
    return jsonify(data), 200  # ← 通常はそのままecho


@app.route('/')
def health_check():
    return 'OK', 200
