"""
Contact Page for ResiVoice Application
Provides contact information and support options
"""

import streamlit as st
import sys
import os

# Add the parent directory to the path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.navigation import render_voice_section

def contact_page():
    """Main contact page function"""
    st.markdown('<h2 class="page-header">📞 Contact & Support</h2>', unsafe_allow_html=True)
    
    # Voice Assistant Section
    render_voice_section(
        title="🎤 Voice Support",
        description="Use voice commands to get help quickly",
        examples="Say things like: \"I need urgent help\", \"Contact maintenance\", etc."
    )
    
    # Contact information
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        ### 🏢 Management Office
        
        **Address:** Building A, Ground Floor  
        **Phone:** (555) 123-4567  
        **Email:** management@resivoice.com  
        **Hours:** Mon-Fri 9:00 AM - 6:00 PM
        
        ---
        
        ### 🔧 Maintenance Team
        
        **Emergency Hotline:** (555) 999-8888  
        **Email:** maintenance@resivoice.com  
        **Response Time:** Within 2 hours for emergencies
        
        ---
        
        ### 🚨 Emergency Contacts
        
        **Fire Department:** 911  
        **Police:** 911  
        **Building Security:** (555) 777-6666
        """)
    
    with col2:
        st.markdown("""
        ### 📧 Contact Form
        
        Need to reach us? Fill out the form below:
        """)
        
        # Contact form
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            unit = st.text_input("Unit Number")
            email = st.text_input("Email Address")
            phone = st.text_input("Phone Number")
            
            contact_type = st.selectbox(
                "Type of Inquiry",
                ["General Question", "Maintenance Issue", "Complaint", "Suggestion", "Emergency"]
            )
            
            message = st.text_area("Message", height=150)
            
            if st.form_submit_button("Send Message", use_container_width=True):
                if name and message:
                    st.success("✅ Message sent successfully! We'll get back to you within 24 hours.")
                else:
                    st.error("❌ Please fill in your name and message.")
    
    # Additional support options
    st.markdown("""
    ---
    
    ### 🆘 Additional Support Options
    
    **📱 Mobile App:** Download our mobile app for quick access  
    **💬 Live Chat:** Available during office hours  
    **📋 FAQ:** Check our frequently asked questions  
    **🎤 Voice Support:** Use voice commands for hands-free assistance
    
    ### 🕒 Response Times
    
    - **Emergency Issues:** Immediate response
    - **Urgent Maintenance:** Within 2 hours
    - **General Inquiries:** Within 24 hours
    - **Suggestions/Feedback:** Within 48 hours
    """) 