from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_URL = "https://apitu.psnw.xyz/index.php"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/phone-lookup', methods=['POST'])
def phone_lookup():
    data = request.json
    phone = data.get('phone')
    
    if not phone or len(phone) != 10 or not phone.isdigit():
        return jsonify({"error": "Invalid phone number"}), 400
    
    params = {
        'type': 'phone',
        'value': phone,
        'mode': 'sff'
    }
    
    response = requests.get(API_URL, params=params, timeout=10)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)