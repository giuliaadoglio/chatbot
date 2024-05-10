from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/message', methods=['POST'])
def handle_message():
    user_message = request.json['message']
    # Here you would typically process the message through your chatbot script.
    # For testing, we'll just echo the user message.
    chatbot_response = f"Echo: {user_message}"
    return jsonify(response=chatbot_response)

if __name__ == "__main__":
    app.run(debug=True)
