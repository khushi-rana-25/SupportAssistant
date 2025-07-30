from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, auth, firestore
import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize Firebase Admin SDK
try:
    # Get Firebase config from environment variables
    firebase_config = {
        "type": os.getenv('FIREBASE_TYPE'),
        "project_id": os.getenv('FIREBASE_PROJECT_ID'),
        "private_key_id": os.getenv('FIREBASE_PRIVATE_KEY_ID'),
        "private_key": os.getenv('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
        "client_email": os.getenv('FIREBASE_CLIENT_EMAIL'),
        "client_id": os.getenv('FIREBASE_CLIENT_ID'),
        "auth_uri": os.getenv('FIREBASE_AUTH_URI'),
        "token_uri": os.getenv('FIREBASE_TOKEN_URI'),
        "auth_provider_x509_cert_url": os.getenv('FIREBASE_AUTH_PROVIDER_X509_CERT_URL'),
        "client_x509_cert_url": os.getenv('FIREBASE_CLIENT_X509_CERT_URL')
    }
    
    cred = credentials.Certificate(firebase_config)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("✅ Firebase initialized successfully")
except Exception as e:
    print(f"❌ Firebase initialization error: {e}")
    db = None

# Secret key for JWT
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')

def create_jwt_token(user_id, role):
    """Create JWT token for user"""
    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    """User registration endpoint"""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        name = data.get('name')
        role = data.get('role', 'user')
        
        if not email or not password or not name:
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Create user in Firebase Auth
        user = auth.create_user(
            email=email,
            password=password,
            display_name=name
        )
        
        # Store user data in Firestore
        user_data = {
            'uid': user.uid,
            'name': name,
            'email': email,
            'role': role,
            'created_at': datetime.utcnow()
        }
        
        db.collection('users').document(user.uid).set(user_data)
        
        # Create JWT token
        token = create_jwt_token(user.uid, role)
        
        return jsonify({
            'message': 'User created successfully',
            'user': {
                'uid': user.uid,
                'name': name,
                'email': email,
                'role': role
            },
            'token': token
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/auth/signin', methods=['POST'])
def signin():
    """User login endpoint"""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({'error': 'Missing email or password'}), 400
        
        # Get user from Firestore
        users_ref = db.collection('users')
        query = users_ref.where('email', '==', email).limit(1)
        docs = query.stream()
        
        user_data = None
        for doc in docs:
            user_data = doc.to_dict()
            break
        
        if not user_data:
            return jsonify({'error': 'User not found'}), 404
        
        # Create JWT token
        token = create_jwt_token(user_data['uid'], user_data['role'])
        
        return jsonify({
            'message': 'Login successful',
            'user': {
                'uid': user_data['uid'],
                'name': user_data['name'],
                'email': user_data['email'],
                'role': user_data['role']
            },
            'token': token
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001) 