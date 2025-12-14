import os
from flask import Flask, request, jsonify
from groq import Groq

app = Flask(__name__)

# Groq Client Setup (Key Render ke locker se lega)
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

@app.route('/')
def home():
    return "THIA Brain is Active on Groq! 🚀"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_data = request.json
        user_message = user_data.get('message')

        if not user_message:
            return jsonify({"reply": "Kuch toh bolo Boss! (Empty message)"})

        # Groq se jawab maangna (Llama 3 Model - Super Fast)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are THIA, a futuristic AI assistant with a personality like the Predator movie interface. You are loyal to your Boss. Keep answers short, crisp, and robotic."
                },
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            model="llama3-8b-8192",  # Ye model bohot fast aur free hai
        )

        bot_reply = chat_completion.choices[0].message.content
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"reply": f"System Error: {str(e)}"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
