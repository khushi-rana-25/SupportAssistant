import streamlit as st
import sys
import os

# Add the frontend directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.ui_utils import load_css
from utils.auth_utils import check_auth_status, login_user, register_user

# Page configuration
st.set_page_config(
    page_title="Support Assistant",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
load_css()

def signin_page():
    """Sign in page"""
    # Initialize session state
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'token' not in st.session_state:
        st.session_state.token = None
    
    # Sign in form
    with st.form("signin_form"):
        st.markdown("""
        <div style="text-align: center; margin-bottom: 30px;">
            <h1 style="color: #333; font-size: 2.5rem; margin-bottom: 10px;">Sign In</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem;">Welcome back! Please sign in to your account.</p>
        </div>
        """, unsafe_allow_html=True)
        
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
        <p style="color: #FFFFFF; margin-bottom: 20px;">Don't have an account?</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Use Streamlit button instead of HTML anchor
    if st.button("Create Account", use_container_width=True, type="secondary"):
        st.session_state.page = "signup"
        st.rerun()

def signup_page():
    """Sign up page"""
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
                # Email validation
                is_valid_email, email_error = validate_email(email)
                if not is_valid_email:
                    st.error(email_error)
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

def user_home_page():
    """User homepage"""
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

def manager_home_page():
    """Community Manager homepage"""
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

def main():
    """Main application with routing"""
    
    # Initialize session state for navigation
    if 'page' not in st.session_state:
        st.session_state.page = "signin"
    
    # Debug: Show current page
    st.sidebar.write(f"Current page: {st.session_state.page}")
    
    # Check if user is authenticated and redirect to appropriate homepage
    if check_auth_status() and st.session_state.page in ["signin", "signup"]:
        user = st.session_state.user
        if user.get('role') == 'user':
            st.session_state.page = "user_home"
        elif user.get('role') == 'community_manager':
            st.session_state.page = "manager_home"
    
    # Route to appropriate page
    if st.session_state.page == "signin":
        signin_page()
    elif st.session_state.page == "signup":
        signup_page()
    elif st.session_state.page == "user_home":
        user_home_page()
    elif st.session_state.page == "manager_home":
        manager_home_page()
    else:
        st.error(f"Unknown page: {st.session_state.page}")
        st.session_state.page = "signin"
        st.rerun()

if __name__ == "__main__":
    main() 