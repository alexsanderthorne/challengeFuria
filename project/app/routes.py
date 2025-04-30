from flask import Blueprint, render_template, request, jsonify
from chatbot.bot import get_bot_response
from .models import Message
from . import db


main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_bot_response(user_input)

    # Salva no banco
    message = Message(user_message=user_input, bot_response=response)
    db.session.add(message)
    db.session.commit()

    return jsonify({"response": response})

