from flask import Flask, request, jsonify, send_from_directory
from google.cloud import dialogflowcx_v3 as dialogflow
import uuid
import os

app = Flask(__name__)

# ==============================
# CONFIGURATION
# ==============================

PROJECT_ID = "genaiguruyoutube"
LOCATION = "us"
AGENT_ID = "56f1bb1e-798c-4399-b79e-3d1009d86799"
DEPLOYMENT_ID = "e6ecdd16-b468-4ab7-b97b-e677e4f503bf"

# ==============================
# ROUTES
# ==============================

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    session_id = request.json.get("session_id")

    if not session_id:
        session_id = str(uuid.uuid4())

    client = dialogflow.SessionsClient()

    session_path = (
        f"projects/{PROJECT_ID}/locations/{LOCATION}"
        f"/agents/{AGENT_ID}/deployments/{DEPLOYMENT_ID}"
        f"/sessions/{session_id}"
    )

    request_dialogflow = dialogflow.RunSessionRequest(
        session=session_path,
        text_input=dialogflow.TextInput(text=user_message),
    )

    response = client.run_session(request=request_dialogflow)

    bot_reply = ""

    if response.response_messages:
        for msg in response.response_messages:
            if msg.text:
                bot_reply += " ".join(msg.text.text)

    return jsonify({
        "reply": bot_reply,
        "session_id": session_id
    })


if __name__ == "__main__":
    app.run(debug=True)