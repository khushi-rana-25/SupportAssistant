"""
Documentation Page for ResiVoice Application
Provides help and documentation for users
"""

import streamlit as st
import sys
import os

# Add the parent directory to the path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.navigation import render_voice_section

def documentation_page():
    """Main documentation page function"""
    st.markdown('<h2 class="page-header">📖 Documentation & Help</h2>', unsafe_allow_html=True)
    
    # Voice Assistant Section
    render_voice_section(
        title="🎤 Voice Assistant Help",
        description="Learn how to use voice commands effectively",
        examples="Say things like: \"How do I file a complaint?\", \"What services are available?\", etc."
    )
    
    # Documentation sections
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        ### 📝 Filing Complaints
        
        **How to file a complaint:**
        1. Navigate to the Complaint page
        2. Fill out the complaint form
        3. Select the appropriate category
        4. Provide detailed description
        5. Submit your complaint
        
        **Voice Command:** "I want to file a complaint about noise"
        
        ---
        
        ### 🔧 Service Requests
        
        **How to request services:**
        1. Go to the Service Request page
        2. Choose service type (plumbing, electrical, etc.)
        3. Set urgency level
        4. Describe the issue
        5. Submit request
        
        **Voice Command:** "I need plumbing service for a leaky faucet"
        """)
    
    with col2:
        st.markdown("""
        ### 📊 Tracking Requests
        
        **How to track your requests:**
        1. Visit the Tracking page
        2. View all your submitted requests
        3. Check status updates
        4. Use voice commands for quick access
        
        **Voice Command:** "Track my complaint COMP-0001"
        
        ---
        
        ### 💬 Feedback System
        
        **How to provide feedback:**
        1. Access the Feedback page
        2. Rate your experience
        3. Share suggestions
        4. Help improve our services
        
        **Voice Command:** "I want to give feedback about my recent service"
        """)
    
    # Quick tips section
    st.markdown("""
    ---
    
    ### 💡 Quick Tips
    
    - **Be specific** when describing issues
    - **Include relevant details** like location and time
    - **Use voice commands** for hands-free interaction
    - **Check tracking** for status updates
    - **Provide feedback** to help improve services
    
    ### 🆘 Need More Help?
    
    If you need additional assistance, please contact our support team through the Contact page.
    """) 