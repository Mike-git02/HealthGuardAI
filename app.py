from flask import Flask, render_template, request, jsonify
from health_monitor import get_health_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_reply = get_health_response(user_message)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
