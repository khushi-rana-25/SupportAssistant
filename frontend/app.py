"""
Main Application for ResiVoice
Entry point for the Streamlit application
"""

import streamlit as st
from datetime import datetime
import sys
import os

# Add the current directory to the path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import custom styles and components
from utils.ui_utils import load_css
from utils.auth_utils import check_auth_status
from components.navigation import (
    render_navbar,
    render_top_header,
    get_current_page
)

# Import page modules
from pages.complaint_page import complaint_page
from pages.tracki import tracking_page
from pages.feedback import feedback_page
from pages.signin import signin_page
from pages.signup import signup_page
# from pages.logout import logout_page

# Page configuration
st.set_page_config(
    page_title="ResiVoice",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Initialize session state
if 'complaints' not in st.session_state:
    st.session_state.complaints = []
if 'service_requests' not in st.session_state:
    st.session_state.service_requests = []
if 'tracking_data' not in st.session_state:
    st.session_state.tracking_data = []
if 'feedback' not in st.session_state:
    st.session_state.feedback = []

def main():
    """Main application function"""

    is_authenticated = check_auth_status()
    current_page = get_current_page()

    if is_authenticated:
        # Show header and navbar for authenticated users
        render_top_header()
        render_navbar(current_page)

        # Handle logout popup
        if st.session_state.get('show_logout_confirm', False):
            logout_page()
            return

        # Routing for authenticated users
        if current_page == "complaint":
            complaint_page()
        elif current_page == "tracking":
            tracking_page()
        elif current_page == "feedback":
            feedback_page()
        else:
            complaint_page()
    else:
        # Routing for unauthenticated users
        if current_page == "signup":
            signup_page()
        else:
            # Default to signin page
            signin_page()

if __name__ == "__main__":
    main()