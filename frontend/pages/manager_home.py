import streamlit as st
import sys
import os


# Add the frontend directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.auth_utils import check_auth_status

def main():
    """Community Manager homepage main function"""
    
    # Check if user is authenticated and has community_manager role
    if not check_auth_status():
        st.error("Please sign in to access this page.")
        st.session_state.page = "signin"
        st.rerun()
        return
    
    user = st.session_state.user
    if user.get('role') != 'community_manager':
        st.error("Access denied. This page is for community managers only.")
        st.rerun()
        return
    
    # Community Manager homepage content
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="color: #333; font-size: 2.5rem; margin-bottom: 10px;">Community Manager Dashboard</h1>
        <p style="color: #666; font-size: 1.1rem;">Manage your community and support tickets</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Manager information
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.info(f"**Name:** {user['name']}")
        st.info(f"**Email:** {user['email']}")
        st.info(f"**Role:** Community Manager")
    
    # Manager-specific features
    st.markdown("## 🛠️ Management Dashboard")
    
    # Quick stats
    st.markdown("### Quick Stats")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Open Tickets", "12")
    
    with col2:
        st.metric("Resolved Today", "5")
    
    with col3:
        st.metric("Total Users", "156")
    
    with col4:
        st.metric("Response Time", "2.3h")
    
    # Management actions
    st.markdown("### Management Actions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📋 View All Tickets", use_container_width=True):
            st.info("Ticket management feature coming soon!")
    
    with col2:
        if st.button("👥 Manage Users", use_container_width=True):
            st.info("User management feature coming soon!")
    
    with col3:
        if st.button("📊 Analytics", use_container_width=True):
            st.info("Analytics dashboard coming soon!")
    
    # Recent tickets
    st.markdown("### Recent Support Tickets")
    st.info("No recent tickets to display.")
    
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