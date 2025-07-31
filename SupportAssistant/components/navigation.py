import streamlit as st

def create_navigation():
    """Create the navigation header and menu"""
    
    # Main header with logo and branding
    st.markdown("""
    <div style="
        background: #2c3e50;
        padding: 0.8rem 0;
        margin-bottom: 2rem;
        border-top: 3px solid #e74c3c;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    ">
        <div style="
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 2rem;
        ">
            <!-- Left Section: Logo and Branding -->
            <div style="
                display: flex;
                align-items: center;
                gap: 1.5rem;
            ">
                <!-- Logo -->
                <div style="
                    display: flex;
                    align-items: center;
                    gap: 0.8rem;
                ">
                    <div style="
                        width: 50px;
                        height: 50px;
                        background: linear-gradient(135deg, #e74c3c, #f39c12, #f1c40f, #3498db);
                        border-radius: 50%;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 1.5rem;
                        color: white;
                        font-weight: bold;
                    ">🏠</div>
                    <div>
                        <h2 style="
                            color: white; 
                            font-family: 'Inter', sans-serif; 
                            font-weight: 700; 
                            margin: 0; 
                            font-size: 1.8rem;
                            text-transform: uppercase;
                            letter-spacing: 1px;
                        ">ResiVoice</h2>
                        <p style="
                            color: rgba(255,255,255,0.8); 
                            font-family: 'Inter', sans-serif; 
                            font-size: 0.75rem; 
                            margin: 0;
                            text-transform: uppercase;
                            letter-spacing: 0.5px;
                        ">Your Voice, Our Solution</p>
                    </div>
                </div>
                
                <!-- API Status Indicator -->
                <div id="api-status" class="api-status connected">
                    🟢 API Connected
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation buttons
    st.markdown("""
    <div style="
        background: #2c3e50;
        padding: 0.5rem 0;
        margin-bottom: 1rem;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    ">
        <div style="
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: flex-end;
            gap: 2rem;
            padding: 0 2rem;
        ">
    """, unsafe_allow_html=True)
    
    # Create navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("📝 Complaint", key="nav_complaint_btn", use_container_width=True):
            st.query_params["nav"] = "complaint"
            st.rerun()
    
    with col2:
        if st.button("📊 Tracking", key="nav_tracking_btn", use_container_width=True):
            st.query_params["nav"] = "tracking"
            st.rerun()
    
    with col3:
        if st.button("💬 Feedback", key="nav_feedback_btn", use_container_width=True):
            st.query_params["nav"] = "feedback"
            st.rerun()
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)

def create_breadcrumb(current_page: str):
    """Create breadcrumb navigation"""
    page_names = {
        "complaint": "File Complaint",
        "tracking": "Track Requests",
        "feedback": "Give Feedback"
    }
    
    st.markdown(f"""
    <div style="
        margin-bottom: 1rem;
        padding: 0.5rem 1rem;
        background: rgba(52, 152, 219, 0.1);
        border-radius: 8px;
        border-left: 4px solid #3498db;
    ">
        <span style="color: #7f8c8d; font-size: 0.9rem;">
            🏠 Home > {page_names.get(current_page, current_page.title())}
        </span>
    </div>
    """, unsafe_allow_html=True)

def show_api_status(is_connected: bool):
    """Show API connection status"""
    status_class = "connected" if is_connected else "disconnected"
    status_text = "🟢 API Connected" if is_connected else "🔴 API Disconnected"
    
    st.markdown(f"""
    <script>
        const statusElement = document.getElementById('api-status');
        if (statusElement) {{
            statusElement.className = 'api-status {status_class}';
            statusElement.innerHTML = '{status_text}';
        }}
    </script>
    """, unsafe_allow_html=True)