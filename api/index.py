from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Phone Lookup API is running"

# Import routes
from api.phone import phone_bp
app.register_blueprint(phone_bp)