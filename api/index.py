import json
import requests

def handler(request):
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    if request['method'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'status': 'ok'})
        }
    
    if request['method'] != 'POST':
        return {
            'statusCode': 405,
            'headers': headers,
            'body': json.dumps({'error': 'POST method required'})
        }
    
    try:
        body = request.get('body', '{}')
        data = json.loads(body)
        phone = data.get('phone', '').strip()
        
        if not phone or len(phone) != 10 or not phone.isdigit():
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Invalid phone number'})
            }
        
        url = "https://apitu.psnw.xyz/index.php"
        params = {
            'type': 'phone',
            'value': phone,
            'mode': 'sff'
        }
        
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(result)
        }
        
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps({'error': 'Invalid JSON'})
        }
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': f'API error: {str(e)}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': f'Server error: {str(e)}'})
        }