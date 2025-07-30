import streamlit as st
import sys
import os

# Add the frontend directory to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.auth_utils import register_user, check_auth_status

def main():
    """Sign up page main function"""
    
    # Check if user is already authenticated
    if check_auth_status():
        st.success("You are already signed in!")
        st.rerun()
    
    # Initialize session state for form clearing and feedback
    if 'form_cleared' not in st.session_state:
        st.session_state.form_cleared = False
    if 'signup_success' not in st.session_state:
        st.session_state.signup_success = False
    if 'show_spinner' not in st.session_state:
        st.session_state.show_spinner = False
    
    # Reset form_cleared flag after form is displayed
    if st.session_state.form_cleared:
        st.session_state.form_cleared = False
    
    # Show success message and redirect after short delay
    if st.session_state.signup_success:
        st.success("Account created successfully! Redirecting...")
        import time
        time.sleep(2)
        st.session_state.signup_success = False
        st.rerun()
        return
    
    # Sign up form
    with st.form("signup_form"):
        st.markdown("""
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 style="color: #333; font-size: 2.5rem; margin-bottom: 10px;">Create Account</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem;">Join our community and start your journey!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Name field
        name = st.text_input(
            "Full Name",
            value="" if st.session_state.form_cleared else None,
            placeholder="Enter your full name",
            help="Please enter your full name as you'd like it to appear"
        )
        
        # Email field
        email = st.text_input(
            "Email Address",
            value="" if st.session_state.form_cleared else None,
            placeholder="Enter your email address",
            help="Please enter a valid email address"
        )
        
        # Password field
        password = st.text_input(
            "Password",
            type="password",
            value="" if st.session_state.form_cleared else None,
            placeholder="Create a strong password",
            help="Password must be at least 6 characters long"
        )
        
        # Confirm password field
        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            value="" if st.session_state.form_cleared else None,
            placeholder="Confirm your password",
            help="Please confirm your password"
        )
        
        # Role selection
        role = st.selectbox(
            "Select Your Role",
            options=["user", "community_manager"],
            index=0 if st.session_state.form_cleared else None,
            format_func=lambda x: "User" if x == "user" else "Community Manager",
            help="Choose your role"
        )
        
        # Terms and conditions
        agree_terms = st.checkbox(
            "I agree to the Terms of Service and Privacy Policy",
            value=False if st.session_state.form_cleared else None,
            help="You must agree to the terms to create an account"
        )
        
        # Submit button
        submit_button = st.form_submit_button(
            "Create Account",
            use_container_width=True,
            type="primary"
        )
        
        if submit_button:
            # Validation
            if not name or not email or not password or not confirm_password:
                st.error("Please fill in all required fields.")
            elif len(password) < 6:
                st.error("Password must be at least 6 characters long.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            elif not agree_terms:
                st.error("You must agree to the Terms of Service and Privacy Policy.")
            else:
                # Show spinner while registering
                with st.spinner("Creating your account..."):
                    result = register_user(name, email, password, role)
                if result:
                    st.session_state.form_cleared = True
                    st.session_state.signup_success = True
                    # Redirect to appropriate homepage based on role
                    user = st.session_state.user
                    if user.get('role') == 'user':
                        st.session_state.page = "user_home"
                    elif user.get('role') == 'community_manager':
                        st.session_state.page = "manager_home"
                    st.experimental_rerun()
                else:
                    st.error("Registration failed. Please try again.")
    
    # Additional options
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="text-align: center; margin-top: 30px;">
            <p style="color: #FFFFFF; margin-bottom: 20px;">Already have an account?</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Use Streamlit button instead of HTML anchor
        if st.button("Sign In", use_container_width=True, type="secondary"):
            st.session_state.page = "signin"
            st.rerun()

if __name__ == "__main__":
    main() 