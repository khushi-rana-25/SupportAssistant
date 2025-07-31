"""
Main Application for ResiVoice
Entry point for the Streamlit application
"""

import streamlit as st
from datetime import datetime
import sys
import os
from pages.manager_home import community_page

# Add the current directory to the path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import custom styles and components
from utils.styles import get_custom_css
from components.navigation import (
    render_sidebar_branding,
    render_sidebar_navigation,
    render_navbar,
    render_top_header,
    render_voice_section,
    get_current_page
)

# Import page modules
from pages.complaint_page import complaint_page
from pages.tracki import tracking_page
from pages.feedback import feedback_page
from pages.documentation import documentation_page
from pages.contact import contact_page

# Page configuration
st.set_page_config(
    page_title="ResiVoice",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

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
    
    # Render top header
    render_top_header()

    render_navbar(get_current_page())
    
    # # Configure sidebar
    # with st.sidebar:
    #     render_sidebar_branding()
    #     render_navbar(get_current_page())
    
    # Get current page from URL parameters or default to dashboard
    current_page = get_current_page()
    
    # Page routing
    if current_page == "dashboard" or current_page == "complaint":
        complaint_page()
    elif current_page == "tracking":
        tracking_page()
    elif current_page == "feedback":
        feedback_page()
    elif current_page == "documentation":
        documentation_page()
    elif current_page == "contact":
        contact_page()
    elif current_page == "community":
        community_page()
    elif current_page == "logout":
        # Clear session state and redirect to dashboard
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.query_params["nav"] = "dashboard"
        st.rerun()
    else:
        complaint_page()  # Default page

if __name__ == "__main__":
    main() 