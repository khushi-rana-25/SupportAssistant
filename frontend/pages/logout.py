import streamlit as st
from utils.auth_utils import logout_user

def logout_popup():
    """Renders a simple logout confirmation popup"""
    # Create a container for the popup
    with st.container():
        st.markdown("---")
        
        # Popup content
        st.markdown("### Logout Confirmation")
        st.markdown("Are you sure you want to logout?")
        
        # Buttons in columns
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            if st.button("Cancel", key="cancel_logout", type="secondary"):
                st.session_state.show_logout_popup = False
                st.rerun()
        
        with col2:
            if st.button("Logout", key="confirm_logout", type="primary"):
                if logout_user():
                    st.success("Successfully logged out!")
                    st.session_state.show_logout_popup = False
                    st.rerun()
        
        # Add helpful message below the popup
        st.markdown("---")
        st.warning("Please click 'Cancel' above to return to the dashboard and access other tabs.") 