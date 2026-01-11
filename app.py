from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

import os
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-1.0-pro:generateContent"
        "?key=" + GOOGLE_API_KEY
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_message}
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)
    result = response.json()

    print("RAW GEMINI RESPONSE:", result)

    if "candidates" in result:
        reply = result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        reply = "Gemini API error: " + str(result)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
