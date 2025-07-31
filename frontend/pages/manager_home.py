"""
Manager Home - Recommended Events Dashboard
"""

import streamlit as st
from datetime import datetime, timedelta

def manager_home():
    st.set_page_config(page_title="Manager Dashboard", page_icon="👨‍💼", layout="wide")
    
    # Custom CSS for styling
    st.markdown("""
        <style>
        .recommended-events-card {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            border: 2px solid #00d4aa;
            box-shadow: 0 8px 32px rgba(0, 212, 170, 0.2);
        }
        .event-item {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
            border-left: 4px solid #00d4aa;
            transition: all 0.3s ease;
        }
        .event-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(0, 212, 170, 0.3);
        }
        .add-event-btn {
            background: linear-gradient(45deg, #00d4aa, #00b8d4);
            border: none;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            font-size: 24px;
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 1rem auto;
        }
        .add-event-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 4px 20px rgba(0, 212, 170, 0.4);
        }
        .header-section {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
        }
        .floating-add-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: linear-gradient(45deg, #00d4aa, #00b8d4);
            border: none;
            border-radius: 50%;
            width: 70px;
            height: 70px;
            font-size: 28px;
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 6px 20px rgba(0, 212, 170, 0.4);
            z-index: 1000;
        }
        .floating-add-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 8px 25px rgba(0, 212, 170, 0.6);
        }
        .upcoming-events-section {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            border: 2px solid #00d4aa;
            box-shadow: 0 8px 32px rgba(0, 212, 170, 0.2);
        }
        /* Hide the Streamlit button that triggers the form */
        [data-testid="baseButton-secondary"] {
            display: none !important;
        }
        .stButton>button.fab-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: linear-gradient(45deg, #00d4aa, #00b8d4);
            border: none;
            border-radius: 50%;
            width: 70px;
            height: 70px;
            font-size: 32px;
            color: white;
            cursor: pointer;
            box-shadow: 0 6px 20px rgba(0, 212, 170, 0.4);
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
        }
        .stButton>button.fab-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 8px 25px rgba(0, 212, 170, 0.6);
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 style="color: #00d4aa; text-align: center;">👨‍💼 Manager Dashboard</h1>', unsafe_allow_html=True)
    
    # Initialize session state for upcoming events
    if 'upcoming_events' not in st.session_state:
        st.session_state.upcoming_events = [
            {
                'id': 'UP-001',
                'title': 'Community Safety Workshop',
                'description': 'Monthly safety awareness session for all residents',
                'date': datetime.now() + timedelta(days=7),
                'location': 'Community Hall',
                'type': 'Safety',
                'priority': 'High'
            },
            {
                'id': 'UP-002',
                'title': 'Maintenance Day',
                'description': 'Scheduled maintenance for common areas and facilities',
                'date': datetime.now() + timedelta(days=14),
                'location': 'Various Locations',
                'type': 'Maintenance',
                'priority': 'Medium'
            },
            {
                'id': 'UP-003',
                'title': 'Resident Meet & Greet',
                'description': 'Social gathering to foster community bonding',
                'date': datetime.now() + timedelta(days=21),
                'location': 'Garden Area',
                'type': 'Social',
                'priority': 'Low'
            }
        ]
    
    # Upcoming Events Section
    st.markdown("""
        <div class="upcoming-events-section">
            <div class="header-section">
                <h2 style="color: #00d4aa; margin: 0;">🚀 Upcoming Events</h2>
                <div style="text-align: right;">
                    <p style="color: #888; margin: 0;">Events scheduled for the future</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Display upcoming events (events with future dates)
    upcoming_events = [event for event in st.session_state.upcoming_events if event['date'] > datetime.now()]
    
    if upcoming_events:
        for event in upcoming_events:
            priority_color = {
                'High': '#ff6b6b',
                'Medium': '#ffd93d',
                'Low': '#6bcf7f'
            }
            
            st.markdown(f"""
                <div class="event-item">
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <div style="flex: 1;">
                            <h3 style="color: #00d4aa; margin: 0 0 0.5rem 0;">{event['title']}</h3>
                            <p style="color: #e0e0e0; margin: 0 0 1rem 0;">{event['description']}</p>
                            <div style="color: #888; font-size: 0.9rem;">
                                📅 {event['date'].strftime('%B %d, %Y')} • 📍 {event['location']} • 🏷️ {event['type']}
                            </div>
                        </div>
                        <div style="margin-left: 1rem;">
                            <span style="background: {priority_color[event['priority']]}; color: #000; padding: 0.3rem 0.8rem; border-radius: 12px; font-size: 0.8rem; font-weight: bold;">
                                {event['priority']} Priority
                            </span>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No upcoming events scheduled. Use the floating + button to add new events!")
    
    # Floating Action Button (real Streamlit button)
    fab_clicked = st.button("+", key="fab_add_btn", help="Add upcoming event", args=None, kwargs=None)
    # Patch the button class to look like a FAB
    st.markdown("""
        <script>
        const fabBtn = window.parent.document.querySelector('button[data-testid="baseButton-fab_add_btn"]');
        if (fabBtn) { fabBtn.classList.add('fab-btn'); }
        </script>
    """, unsafe_allow_html=True)

    if fab_clicked:
        st.session_state.show_add_form = True

    if st.session_state.get('show_add_form', False):
        with st.form("add_event_form"):
            st.markdown("### 🚀 Add Upcoming Event")
            new_title = st.text_input("Event Title")
            new_description = st.text_area("Event Description")
            default_date = datetime.now().date() + timedelta(days=1)
            new_date = st.date_input("Event Date", value=default_date, min_value=datetime.now().date())
            new_location = st.text_input("Event Location")
            new_type = st.selectbox("Event Type", ["Social", "Educational", "Maintenance", "Safety", "Other"])
            new_priority = st.selectbox("Priority", ["High", "Medium", "Low"])
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button("✅ Add Event", use_container_width=True):
                    if new_title and new_description:
                        new_event = {
                            'id': f'UP-{len(st.session_state.upcoming_events)+1:03d}',
                            'title': new_title,
                            'description': new_description,
                            'date': new_date,
                            'location': new_location,
                            'type': new_type,
                            'priority': new_priority
                        }
                        st.session_state.upcoming_events.append(new_event)
                        st.session_state.show_add_form = False
                        st.success("Event added successfully!")
                        st.rerun()
                    else:
                        st.error("Please fill in all required fields.")
            with col2:
                if st.form_submit_button("❌ Cancel", use_container_width=True):
                    st.session_state.show_add_form = False
                    st.rerun()

if __name__ == "__main__":
    manager_home()
