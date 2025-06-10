from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    return "OK", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received:", data)
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run(debug=True)
