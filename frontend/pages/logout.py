import streamlit as st
import sys
import os

# Add the frontend directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

def logout_page():
    """Logout page function"""
    
    # Page header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="color: #333; font-size: 2.5rem; margin-bottom: 10px;">Logout</h1>
        <p style="color: #666; font-size: 1.1rem;">Are you sure you want to logout?</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Confirmation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("Yes, Logout", use_container_width=True, type="primary"):
            if logout_user():
                st.success("Successfully logged out!")
                st.rerun()
    
    with col1:
        if st.button("Cancel", use_container_width=True, type="secondary"):
            # Go back to previous page or user home
            if 'user' in st.session_state and st.session_state.user:
                user = st.session_state.user
                if user.get('role') == 'user':
                    st.session_state.page = "user_home"
                elif user.get('role') == 'community_manager':
                    st.session_state.page = "manager_home"
            else:
                st.session_state.page = "signin"
            st.rerun()

def quick_logout():
    """Quick logout function for sidebar or navigation"""
    if st.button("Logout", key="quick_logout"):
        if logout_user():
            st.success("Successfully logged out!")
            st.rerun()

if __name__ == "__main__":
    logout_page() 