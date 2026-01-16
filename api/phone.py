from http.server import BaseHTTPRequestHandler
import json
import requests
import os

def handler(request):
    if request['method'] != 'POST':
        return {
            'statusCode': 405,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'Method not allowed'})
        }
    
    try:
        data = json.loads(request['body'])
        phone = data.get('phone', '').strip()
        
        if len(phone) != 10 or not phone.isdigit():
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({'error': 'Invalid phone number'})
            }
        
        url = "https://apitu.psnw.xyz/index.php"
        params = {
            'type': 'phone',
            'value': phone,
            'mode': 'sff'
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': response.text
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }