import os
from flask import Flask, request, jsonify
from groq import Groq

app = Flask(__name__)

# Groq Client Setup
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

@app.route('/')
def home():
    # Aapke kehne par yahan bhi exact naam likh diya hai
    return "THIA Brain is Active: Model [llama-3.1-8b-instant] 🚀"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_data = request.json
        user_message = user_data.get('message')

        if not user_message:
            return jsonify({"reply": "Kuch toh bolo Boss! (Empty message)"})

        # --- YAHAN HAI ASLI SETTING ---
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are THIA, a futuristic AI assistant with a personality like the Predator movie interface. You are loyal only to your Boss. Keep answers short, crisp, tactical, and robotic."
                },
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            # 👉 Ye hai wo Model ID jo list mein aayi thi
            model="llama-3.1-8b-instant",
        )

        bot_reply = chat_completion.choices[0].message.content
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"reply": f"System Failure: {str(e)}"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
