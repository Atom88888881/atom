from flask import Blueprint, request, jsonify
import requests

phone_bp = Blueprint('phone', __name__)

@phone_bp.route('/api/phone-lookup', methods=['POST'])
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
    
    response = requests.get("https://apitu.psnw.xyz/index.php", params=params, timeout=10)
    return jsonify(response.json())