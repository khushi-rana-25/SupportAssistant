import streamlit as st
import sys
import os

# Add the frontend directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pages.signin import signin_page

def main():
    """Main application function"""
    
    # Initialize session state
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'token' not in st.session_state:
        st.session_state.token = None
    
    # Call the signin page function
    signin_page()

if __name__ == "__main__":
    main() 