from flask import Blueprint, render_template, request, jsonify
from chatbot.bot import get_bot_response

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_bot_response(user_input)
    return jsonify({"response": response})
