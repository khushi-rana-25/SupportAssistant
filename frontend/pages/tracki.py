"""
Tracking Page for ResiVoice Application
Handles request tracking functionality
"""

import streamlit as st
import pandas as pd
import sys
import os

# Add the parent directory to the path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.navigation import render_voice_section

def tracking_page():
    """Main tracking page function"""
    st.markdown('<h2 class="page-header">📊 Track Your Requests</h2>', unsafe_allow_html=True)
    
    # Voice Assistant Section
    render_voice_section(
        title="🎤 Voice Assistant",
        description="Click the button below to start voice interaction with Omnidim.io",
        examples="Say things like: \"Track my complaint COMP-0001\", \"What's the status of my service request\", etc."
    )
    
    
    
    # Show all requests summary
    if st.session_state.complaints or st.session_state.service_requests:
        st.markdown('<h3 style="margin-top: 2rem;">📋 All Your Requests</h3>', unsafe_allow_html=True)
        
        # Create summary dataframe
        all_requests = []
        
        for complaint in st.session_state.complaints:
            all_requests.append({
                'ID': complaint['id'],
                'Type': 'Complaint',
                'Category': complaint['category'],
                'Status': complaint['status'],
                'Submitted': complaint['submitted_date'].strftime('%Y-%m-%d'),
                'Priority': complaint['priority']
            })
        
        for request in st.session_state.service_requests:
            all_requests.append({
                'ID': request['id'],
                'Type': 'Service Request',
                'Category': request['service_type'],
                'Status': request['status'],
                'Submitted': request['submitted_date'].strftime('%Y-%m-%d'),
                'Priority': request['urgency']
            })
        
        if all_requests:
            df = pd.DataFrame(all_requests)
            st.dataframe(df, use_container_width=True)
    else:
        st.info("📊 No requests to track yet. Submit a complaint or service request first!")