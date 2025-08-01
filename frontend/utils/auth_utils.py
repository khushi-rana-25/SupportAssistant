import requests
import streamlit as st

from pages.signup import signup_page
from pages.signin import signin_page

# API base URL
API_BASE_URL = "http://localhost:5001/api"

def login_user(email, password):
    """Login user with email and password"""
    try:
        response = requests.post(f"{API_BASE_URL}/auth/signin", json={
            'email': email,
            'password': password
        })
        
        if response.status_code == 200:
            data = response.json()
            st.session_state.user = data['user']
            st.session_state.token = data['token']
            return True
        else:
            error_data = response.json()
            st.error(error_data.get('error', 'Login failed'))
            return False
            
    except Exception as e:
        st.error(f"Connection error: {str(e)}")
        return False

def register_user(name, email, password, role):
    """Register new user"""
    try:
        response = requests.post(f"{API_BASE_URL}/auth/signup", json={
            'name': name,
            'email': email,
            'password': password,
            'role': role
        })
        
        if response.status_code == 201:
            data = response.json()
            st.session_state.user = data['user']
            st.session_state.token = data['token']
            return True
        else:
            error_data = response.json()
            st.error(error_data.get('error', 'Registration failed'))
            return False
            
    except Exception as e:
        st.error(f"Connection error: {str(e)}")
        return False

def check_auth_status():
    """Check if user is authenticated"""
    return 'user' in st.session_state and st.session_state.user is not None

def logout_user():
    """Logout user and clear session state"""
    # Clear user session data
    if 'user' in st.session_state:
        del st.session_state.user
    if 'token' in st.session_state:
        del st.session_state.token
    
    # Reset page to signin
    st.session_state.page = "signin"
    
    return True 