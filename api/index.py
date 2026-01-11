from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")
    return jsonify({
        "reply": "✅ Deployed on Vercel! You said: " + msg
    })

# Required for Vercel
def handler(request, context):
    return app(request, context)
