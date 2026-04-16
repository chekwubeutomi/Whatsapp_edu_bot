import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from bots import ask_tutor
from utils import get_curriculum_context

app = Flask(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "../data/curriculum.pdf")

CONTEXT = get_curriculum_context(file_path)

@app.route("/")
def home():
    return "The Edu-Bot Server is LIVE! Send a WhatsApp message to test."




@app.route("/webhook", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    answer = ask_tutor(incoming_msg, CONTEXT)

    resp = MessagingResponse()
    resp.message(answer)
    return str(resp)

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)