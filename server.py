import os
from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/api/translate", methods=["POST"])
def translate():
    data = request.get_json()
    prompt = f"Translate this text to {data['targetLang']}:\n\n{data['text']}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

@app.route("/api/correct", methods=["POST"])
def correct():
    data = request.get_json()
    prompt = "Correct grammar and spelling. Highlight spelling as ++word++ and grammar as **phrase**.\n\n" + data["text"]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

@app.route("/api/explain", methods=["POST"])
def explain():
    data = request.get_json()
    prompt = f"Explain this sentence in {data['targetLang']} like a dictionary:\n\n{data['text']}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

@app.route("/")
def home():
    return "888 AI Server is Running ✅"

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))