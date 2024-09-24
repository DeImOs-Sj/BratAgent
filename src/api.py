# app.py (Flask application)
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_URL = "https://0x89ec2a98d96cdc102214b18f6a5cfbd8e9024f63.us.gaianet.network/v1/chat/completions"

@app.route('/query', methods=['POST'])
def query_api():
    data = request.json
    user_prompt = data.get('prompt')
    model_type = data.get('model')

    # Prepare the payload based on the model type and user prompt
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_prompt}
        ],
        "model": model_type  # Optionally, you can change the model field as per API's specification
    }

    try:
        response = requests.post(API_URL, json=payload)
        response_data = response.json()
        result =response_data.get('choices')[0].get('message').get('content')
        return jsonify(result), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
