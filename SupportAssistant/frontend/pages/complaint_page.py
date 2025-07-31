"""
Complaint Page for ResiVoice Application
Handles complaint filing functionality
"""

import streamlit as st
from datetime import datetime
import sys
import os

# Add the parent directory to the path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.navigation import render_voice_section

def complaint_page():
    """Main complaint page function"""
    st.markdown('<h2 class="page-header">📝 File a Complaint</h2>', unsafe_allow_html=True)
    
    # Voice Assistant Section
    render_voice_section(
        title="🎤 Voice Assistant",
        description="Click the button below to start voice interaction with Omnidim.io",
        examples="Say things like: \"I want to file a complaint about noise\", \"Report a maintenance issue\", etc."
    )
    
    # Instructions
    st.markdown("""
    ### How to use Voice Assistant:
    1. **Click the voice button** to activate Omnidim.io integration
    2. **Speak clearly** about your complaint
    3. **Provide details** like your unit number, issue description, priority level
    4. **Confirm** when the assistant asks for verification
    
    ### Example voice commands:
    - "I want to file a complaint about loud noise from apartment 205"
    - "Report a plumbing issue in unit 101, it's urgent"
    - "Submit a complaint about parking problems"
    """)
    
    # Display recent complaints
    if st.session_state.complaints:
        st.markdown('<h3 style="margin-top: 2rem;">📋 Recent Complaints</h3>', unsafe_allow_html=True)
        
        for complaint in reversed(st.session_state.complaints[-5:]):  # Show last 5 complaints
            with st.container():
                st.markdown(f"""
                <div class="card">
                    <h4>Complaint ID: {complaint['id']}</h4>
                    <p><strong>Category:</strong> {complaint['category']} | <strong>Priority:</strong> {complaint['priority']}</p>
                    <p><strong>Status:</strong> <span class="status-{complaint['status'].lower()}">{complaint['status']}</span></p>
                    <p><strong>Description:</strong> {complaint['description'][:100]}{'...' if len(complaint['description']) > 100 else ''}</p>
                    <p><strong>Submitted:</strong> {complaint['submitted_date'].strftime('%Y-%m-%d %H:%M')}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("📝 No complaints submitted yet. Use the voice assistant above to file your first complaint!")