from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)  # Allow frontend to access the API

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "Prompt is empty"}), 400

    response = ollama.chat(model="tinyllama", messages=[{"role": "user", "content": prompt}])

    return jsonify({"response": response["message"]["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
