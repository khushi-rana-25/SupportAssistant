"""
Navigation Component for ResiVoice Application
Simple, reliable navigation using Streamlit components
"""

import streamlit as st
import sys
import os

# Add the parent directory to the path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.omnidim_client import create_omnidim_manager, handle_voice_command

def render_sidebar_branding():
    """Renders the ResiVoice branding in the sidebar"""
    st.markdown("### 🏠 ResiVoice")
    st.markdown("*Your Voice, Our Solution*")
    st.markdown("---")

def render_sidebar_navigation(active_page):
    """Renders navigation using Streamlit buttons"""
    st.markdown("### Navigation")
    
    if st.button("📊 Dashboard", key="nav_dashboard", use_container_width=True):
        st.query_params["nav"] = "dashboard"
        st.rerun()
    
    if st.button("🏘️ Community", key="nav_community", use_container_width=True):
        st.query_params["nav"] = "community"
        st.rerun()
    
    if st.button("📖 Documentation", key="nav_docs", use_container_width=True):
        st.query_params["nav"] = "documentation"
        st.rerun()
    
    if st.button("📞 Contact", key="nav_contact", use_container_width=True):
        st.query_params["nav"] = "contact"
        st.rerun()
    
    st.markdown("---")
    
    if st.button("🚪 Sign Out", key="nav_signout", use_container_width=True):
        # Clear session state and redirect to dashboard
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.query_params["nav"] = "dashboard"
        st.rerun()

def render_navbar(active_page):
    """Renders a horizontal navbar at the top of the main page"""
    nav_items = [
        ("📊 Dashboard", "dashboard"),
        ("🏘️ Community", "community"),
        ("📖 Documentation", "documentation"),
        ("📞 Contact", "contact"),
        ("🚪 Sign Out", "signout"),
    ]
    cols = st.columns(len(nav_items))
    for idx, (label, nav_key) in enumerate(nav_items):
        if cols[idx].button(label, key=f"nav_{nav_key}"):
            if nav_key == "signout":
                # Clear session state and redirect to dashboard
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.query_params["nav"] = "dashboard"
            else:
                st.query_params["nav"] = nav_key
            st.rerun()

def get_current_page():
    """Get current page from URL query or default"""
    return st.query_params.get("nav", ["dashboard"])[0]

def render_top_header():
    """Renders a simple top header"""
    st.markdown("## 🏠 ResiVoice - Your Voice, Our Solution")
    st.markdown("---")

def render_voice_section(title="🎤 Voice Assistant", 
                        description="Click the button below to start voice interaction with OmniDimension",
                        examples="Say: \"File a complaint about water\", \"Track my request\""):
    """Voice section with OmniDimension SDK integration"""
    st.markdown(f"### {title}")
    st.markdown(description)
    
    # Initialize OmniDimension manager
    omnidim_manager = create_omnidim_manager()
    
    # Initialize session state for voice assistant
    if 'voice_session_id' not in st.session_state:
        st.session_state.voice_session_id = None
    if 'voice_active' not in st.session_state:
        st.session_state.voice_active = False
    if 'voice_messages' not in st.session_state:
        st.session_state.voice_messages = []
    
    # Check if OmniDimension is configured
    if not omnidim_manager.is_configured:
        st.warning("⚠️ OmniDimension not configured. Please set your OMNIDIM_API_KEY environment variable.")
        st.info("Get your API key from the [OmniDimension Dashboard](https://omnidim.io)")
        return
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if not st.session_state.voice_active:
            if st.button("🎤 Start Voice Assistant", key="voice_start_btn", use_container_width=True):
                # Create voice session
                result = omnidim_manager.create_voice_session()
                
                if "session_id" in result:
                    st.session_state.voice_session_id = result["session_id"]
                    st.session_state.voice_active = True
                    st.session_state.voice_messages.append({
                        "type": "assistant",
                        "message": "Voice assistant activated! I'm ready to help you with complaints, tracking, and more."
                    })
                    st.rerun()
                else:
                    st.error(f"Failed to start voice session: {result.get('error', 'Unknown error')}")
        else:
            if st.button("🛑 Stop Voice Assistant", key="voice_stop_btn", use_container_width=True):
                # End voice session
                if st.session_state.voice_session_id:
                    omnidim_manager.end_session(st.session_state.voice_session_id)
                
                st.session_state.voice_session_id = None
                st.session_state.voice_active = False
                st.session_state.voice_messages = []
                st.rerun()
    
    with col2:
        if st.session_state.voice_active:
            if st.button("🎙️ Voice Command", key="voice_command_btn", use_container_width=True):
                st.info("🎙️ Listening... Please speak your command.")
                # In a real implementation, this would capture audio
                # For now, we'll use a text input as a placeholder
                st.session_state.show_voice_input = True
    
    # Show voice input if active
    if st.session_state.voice_active and st.session_state.get('show_voice_input', False):
        st.markdown("---")
        st.markdown("### Voice Command")
        
        # Text input as placeholder for voice input
        voice_text = st.text_input("Type your command (or speak it):", 
                                  placeholder="e.g., 'file a complaint about noise'")
        
        if st.button("Send Command", key="send_voice_cmd"):
            if voice_text:
                # Send message to OmniDimension
                result = omnidim_manager.send_message(st.session_state.voice_session_id, voice_text)
                
                if "response" in result:
                    # Use OmniDimension's response
                    response = result["response"]
                else:
                    # Fallback to local command handling
                    response = handle_voice_command(voice_text, st.session_state)
                
                st.session_state.voice_messages.append({
                    "type": "user",
                    "message": voice_text
                })
                st.session_state.voice_messages.append({
                    "type": "assistant", 
                    "message": response
                })
                st.session_state.show_voice_input = False
                st.rerun()
    
    # Display voice messages
    if st.session_state.voice_messages:
        st.markdown("---")
        st.markdown("### Voice Assistant Chat")
        
        for msg in st.session_state.voice_messages:
            if msg["type"] == "user":
                st.markdown(f"**You:** {msg['message']}")
            else:
                st.markdown(f"**Assistant:** {msg['message']}")
    
    st.markdown(f"*{examples}*")
    
    # Show connection status
    if st.session_state.voice_active:
        st.success("🟢 Connected to OmniDimension")
    else:
        st.info("⚪ Voice assistant ready to connect") 