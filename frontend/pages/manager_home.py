"""
Combined Community Engagement + Support Ticket Manager for ResiVoice Application
"""

import streamlit as st
import sys
import os
from datetime import datetime, timedelta
import pandas as pd

# Voice assistant UI (stub)
def render_voice_section(title, description, examples):
    st.markdown(f"### {title}")
    st.markdown(f"**{description}**")
    st.markdown(f"_e.g._ {examples}")
    st.markdown("---")

def community_page():
    st.set_page_config(page_title="ResiVoice Community", page_icon="🏘️", layout="wide")
    # Animated Gradient Background wrapper start
    st.markdown("""
        <style>
        .dynamic-bg {
            position: relative;
            overflow: hidden;
            border-radius: 18px;
            margin-bottom: 2rem;
            z-index: 1;
        }
        .dynamic-bg::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(270deg, #00d4aa, #0a232e, #00b8d4, #10141a, #00d4aa);
            background-size: 400% 400%;
            animation: gradientMove 12s ease-in-out infinite;
            z-index: 0;
            opacity: 0.25;
        }
        @keyframes gradientMove {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        .dynamic-bg > * {
            position: relative;
            z-index: 1;
        }
        </style>
        <div class="dynamic-bg">
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="page-header">🏘️ Community Engagement</h2>', unsafe_allow_html=True)

    # Voice Assistant
    render_voice_section(
        title="🎤 Community Voice Assistant",
        description="Use voice commands to navigate community features",
        examples="Say: 'Show community events', 'Find neighbors'"
    )

    # Initialize session state
    if 'community_events' not in st.session_state:
        st.session_state.community_events = []
    if 'tickets' not in st.session_state:
        st.session_state.tickets = pd.DataFrame([
            {"Ticket ID": "TCK-001", "Username": "vishakha_m", "Issue Type": "WiFi Issue", "Location": "Block A - Room 203", "Status": "Assigned"},
            {"Ticket ID": "TCK-002", "Username": "john_doe", "Issue Type": "Plumbing", "Location": "Block B - Room 101", "Status": "In Progress"},
            {"Ticket ID": "TCK-003", "Username": "meera_98", "Issue Type": "Power Cut", "Location": "Block C - Room 302", "Status": "Resolved"},
        ])

    # Tabs: Only Events and Support Tickets
    tab1, tab2 = st.tabs(["📅 Events", "📋 Support Tickets"])

    with tab1:
        render_events_tab()

    with tab2:
        render_support_tickets_tab()

    # Animated Gradient Background wrapper end
    st.markdown("</div>", unsafe_allow_html=True)

# === Events Tab ===
def render_events_tab():
    st.markdown("### 📅 Community Events")
    col1, col2 = st.columns([1, 2])
    with col1:
        with st.form("new_event_form"):
            title = st.text_input("Event Title")
            desc = st.text_area("Event Description")
            date = st.date_input("Event Date")
            time = st.time_input("Event Time")
            location = st.text_input("Event Location")
            etype = st.selectbox("Event Type", ["Social", "Educational", "Maintenance", "Safety", "Other"])
            if st.form_submit_button("Create Event", use_container_width=True):
                st.session_state.community_events.append({
                    'id': f"EVT-{len(st.session_state.community_events)+1:04d}",
                    'title': title, 'description': desc,
                    'date': date, 'time': time,
                    'location': location, 'type': etype,
                    'organizer': 'You',
                    'attendees': ['You'],
                    'max_attendees': 50
                })
                st.success("Event created!")
                st.rerun()
        st.metric("Upcoming", len([e for e in st.session_state.community_events if e['date'] >= datetime.now().date()]))

    with col2:
        upcoming = sorted([e for e in st.session_state.community_events if e['date'] >= datetime.now().date()], key=lambda x: x['date'])
        if not upcoming:
            st.info("No upcoming events.")
        for event in upcoming:
            st.markdown(f"""
                <div style="background: #1a1a1a; padding: 1rem; margin-bottom: 1rem; border-left: 4px solid #00d4aa; border-radius: 8px;">
                    <h4 style="color:#00d4aa;">{event['title']}</h4>
                    <p style="color:#e0e0e0;">{event['description']}</p>
                    <div style="color:#888; font-size: 0.8rem;">📅 {event['date']} • 🕐 {event['time']} • 📍 {event['location']}</div>
                </div>
            """, unsafe_allow_html=True)
            if 'You' in event['attendees']:
                if st.button("❌ Cancel RSVP", key=f"cancel_{event['id']}"):
                    event['attendees'].remove('You')
                    st.rerun()
            else:
                if st.button("✅ RSVP", key=f"rsvp_{event['id']}"):
                    event['attendees'].append('You')
                    st.rerun()

# === Support Tickets ===
def render_support_tickets_tab():
    st.markdown("### 📋 Support Ticket Dashboard")
    status_options = ["Assigned", "In Progress", "Resolved"]

    for i, row in st.session_state.tickets.iterrows():
        with st.container():
            col1, col2 = st.columns([2, 5])
            with col1:
                new_status = st.selectbox(
                    f"Update Status for {row['Ticket ID']}",
                    options=status_options,
                    index=status_options.index(row["Status"]),
                    key=f"status_select_{i}"
                )
                if st.button("Update Status", key=f"update_btn_{i}"):
                    st.session_state.tickets.at[i, "Status"] = new_status
                    st.success(f"✅ `{row['Ticket ID']}` status updated to **{new_status}**")
            with col2:
                st.markdown(f"""
                    <div style="
                        background: linear-gradient(135deg, #181c20 80%, #00d4aa22 100%);
                        border-radius: 18px;
                        box-shadow: 0 4px 24px #00d4aa33, 0 1.5px 8px #0008;
                        border: 2px solid #00d4aa;
                        margin-bottom: 2rem;
                        padding: 2rem 2.5rem;
                        position: relative;
                        transition: box-shadow 0.3s;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                    ">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <h3 style="color:#00d4aa; margin-bottom: 0;">🎫 Ticket ID: {row['Ticket ID']}</h3>
                            <span style="background: #222; color: #fff; padding: 0.4rem 1.2rem; border-radius: 8px; font-size: 1.1rem; border: 1px solid #00d4aa;">{row['Status']}</span>
                        </div>
                        <div style="margin-top: 0.7rem; color: #e0e0e0;">
                            <b>👤 Username:</b> {row['Username']}<br/>
                            <b>📍 Location:</b> {row['Location']}<br/>
                            <b>🛠️ Issue Type:</b> {row['Issue Type']}<br/>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    community_page()
