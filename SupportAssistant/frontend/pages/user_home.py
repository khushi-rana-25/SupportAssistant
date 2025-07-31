import streamlit as st
import sys
import os

# Add the frontend directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.auth_utils import check_auth_status

def main():
    """User homepage main function"""
    
    # Check if user is authenticated and has user role
    if not check_auth_status():
        st.error("Please sign in to access this page.")
        st.session_state.page = "signin"
        st.rerun()
        return
    
    user = st.session_state.user
    if user.get('role') != 'user':
        st.error("Access denied. This page is for users only.")
        st.rerun()
        return
    
    # User homepage content
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="color: #333; font-size: 2.5rem; margin-bottom: 10px;">Welcome, User!</h1>
        <p style="color: #666; font-size: 1.1rem;">Here's your personalized dashboard</p>
    </div>
    """, unsafe_allow_html=True)
    
    # User information
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.info(f"**Name:** {user['name']}")
        st.info(f"**Email:** {user['email']}")
        st.info(f"**Role:** {user['role'].title()}")
    
    # User-specific features
    st.markdown("## 🎯 Your Dashboard")
    
    # Quick actions
    st.markdown("### Quick Actions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📝 Create Support Ticket", use_container_width=True):
            st.info("Support ticket creation feature coming soon!")
    
    with col2:
        if st.button("📋 View My Tickets", use_container_width=True):
            st.info("Ticket history feature coming soon!")
    
    with col3:
        if st.button("⚙️ Account Settings", use_container_width=True):
            st.info("Account settings feature coming soon!")
    
    # Recent activity placeholder
    st.markdown("### Recent Activity")
    st.info("No recent activity to display.")
    
    # Sign out button
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("Sign Out", use_container_width=True, type="secondary"):
            st.session_state.user = None
            st.session_state.token = None
            st.session_state.page = "signin"
            st.rerun()

if __name__ == "__main__":
    main() 