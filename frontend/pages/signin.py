import streamlit as st
import sys
import os

# Add the frontend directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.auth_utils import login_user

def signin_page():
    """Sign in page function"""
    
    # Page header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="color: #333; font-size: 2.5rem; margin-bottom: 10px;">Sign In</h1>
        <p style="color: #666; font-size: 1.1rem;">Welcome back! Please sign in to your account.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sign in form
    with st.form("signin_form", clear_on_submit=True):
        # Email field
        email = st.text_input(
            "Email Address",
            placeholder="Enter your email address",
            help="Please enter your registered email address"
        )
        
        # Password field
        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            help="Please enter your password"
        )
        
        # Submit button
        submit_button = st.form_submit_button(
            "Sign In",
            use_container_width=True,
            type="primary"
        )
        
        if submit_button:
            if not email or not password:
                st.error("Please fill in all required fields.")
            else:
                # Attempt login
                if login_user(email, password):
                    st.success("Login successful!")
                    # Redirect to appropriate homepage based on role
                    user = st.session_state.user
                    if user.get('role') == 'user':
                        st.session_state.page = "user_home"
                    elif user.get('role') == 'community_manager':
                        st.session_state.page = "manager_home"
                    st.rerun()
    
    # Link to sign up
    st.markdown("""
    <div style="text-align: center; margin-top: 30px;">
        <p style="color: #666; margin-bottom: 20px;">Don't have an account?</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Use Streamlit button instead of HTML anchor

    if st.button("Create Account", use_container_width=True, type="secondary"):
        from pages.signup import signup_page  # Import moved here to avoid circular import
        st.session_state.page = "signup"
        st.rerun()

if __name__ == "__main__":
    signin_page() 