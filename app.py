from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# --- CONFIGURATION ---
# Yahan apni Google API Key paste karein
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

# Google Gemini Setup
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    # Hum 'gemini-1.5-flash' use kar rahe hain (Ye sabse fast aur naya hai)
    model = genai.GenerativeModel('gemini-flash-latest')
    print("✅ Connected to Google Gemini successfully!")
except Exception as e:
    print(f"❌ Connection Error: {e}")

@app.route('/')
def home():
    return "THIA Brain is Active! 🤖"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # 1. Android se data aayega
        data = request.json
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({"reply": "Message khali tha Boss!"})

        print(f"📩 User bola: {user_message}")

        # 2. Gemini sochega
        response = model.generate_content(user_message)
        bot_reply = response.text

        print(f"📤 THIA boli: {bot_reply}")

        # 3. Jawab wapas bhejo
        return jsonify({"reply": bot_reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "Brain Error: Main soch nahi pa rahi."})

if __name__ == '__main__':
    # Server start hoga

    app.run(debug=True, host='0.0.0.0', port=5000)


