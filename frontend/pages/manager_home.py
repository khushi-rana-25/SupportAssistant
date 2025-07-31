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
            padding-right: 90px;
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
            position: relative;
        }
        .section-add-btn {
            position: absolute;
            top: 1.5rem;
            right: 1.5rem;
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
            box-shadow: 0 4px 15px rgba(0, 212, 170, 0.3);
            z-index: 10;
        }
        .events-container {
            margin-top: 2rem;
            padding-top: 1rem;
        }
        .section-add-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 20px rgba(0, 212, 170, 0.5);
        }
        .event-card {
            position: relative;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            border-left: 4px solid #00d4aa;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }
        .event-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(0, 212, 170, 0.3);
        }
        .share-btn {
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: rgba(0, 212, 170, 0.2);
            border: 1px solid #00d4aa;
            border-radius: 50%;
            width: 35px;
            height: 35px;
            font-size: 14px;
            color: #00d4aa;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .share-btn:hover {
            background: rgba(0, 212, 170, 0.3);
            transform: scale(1.1);
        }
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.7);
            z-index: 10000;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .modal-content {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            border-radius: 20px;
            padding: 2rem;
            border: 2px solid #00d4aa;
            box-shadow: 0 8px 32px rgba(0, 212, 170, 0.3);
            max-width: 500px;
            width: 90%;
            max-height: 80vh;
            overflow-y: auto;
        }
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
        }
        .close-btn {
            background: none;
            border: none;
            color: #00d4aa;
            font-size: 24px;
            cursor: pointer;
            padding: 0;
            width: 30px;
            height: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .close-btn:hover {
            color: #fff;
        }
        .share-modal {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            border-radius: 15px;
            padding: 1.5rem;
            border: 1px solid #00d4aa;
            box-shadow: 0 4px 20px rgba(0, 212, 170, 0.3);
            max-width: 400px;
            width: 90%;
        }
        .share-option {
            display: flex;
            align-items: center;
            padding: 0.8rem;
            margin: 0.5rem 0;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 1px solid transparent;
        }
        .share-option:hover {
            background: rgba(0, 212, 170, 0.1);
            border-color: #00d4aa;
        }
        .copy-link {
            background: linear-gradient(45deg, #00d4aa, #00b8d4);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.8rem 1.5rem;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
            margin-top: 1rem;
        }
        .copy-link:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(0, 212, 170, 0.4);
        }
        /* Hide the Streamlit buttons that trigger the form */
        [data-testid="baseButton-secondary"] {
            display: none !important;
        }
        [data-testid="baseButton-section_add_btn"] {
            display: none !important;
        }
        /* Floating Action Button Styling */
        [data-testid="baseButton-fab_add_btn"] {
            position: fixed !important;
            bottom: 30px !important;
            right: 30px !important;
            background: linear-gradient(45deg, #00d4aa, #00b8d4) !important;
            border: none !important;
            border-radius: 50% !important;
            width: 70px !important;
            height: 70px !important;
            font-size: 32px !important;
            color: white !important;
            cursor: pointer !important;
            box-shadow: 0 6px 20px rgba(0, 212, 170, 0.4) !important;
            z-index: 1000 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            transition: all 0.3s ease !important;
            min-width: 70px !important;
            max-width: 70px !important;
            padding: 0 !important;
        }
        [data-testid="baseButton-fab_add_btn"]:hover {
            transform: scale(1.1) !important;
            box-shadow: 0 8px 25px rgba(0, 212, 170, 0.6) !important;
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
                'type': 'Safety'
            },
            {
                'id': 'UP-002',
                'title': 'Maintenance Day',
                'description': 'Scheduled maintenance for common areas and facilities',
                'date': datetime.now() + timedelta(days=14),
                'location': 'Various Locations',
                'type': 'Maintenance'
            },
            {
                'id': 'UP-003',
                'title': 'Resident Meet & Greet',
                'description': 'Social gathering to foster community bonding',
                'date': datetime.now() + timedelta(days=21),
                'location': 'Garden Area',
                'type': 'Social'
            }
        ]
    
    # Upcoming Events Section with Floating Add Button
    st.markdown("""
        <div class="upcoming-events-section">
            <div class="header-section">
                <h2 style="color: #00d4aa; margin: 0;">🚀 Upcoming Events</h2>
                <div style="text-align: right;">
                    <p style="color: #888; margin: 0;">Events scheduled for the future</p>
                </div>
            </div>
            <button class="section-add-btn" onclick="openAddEventModal()">+</button>
            <div class="events-container">
    """, unsafe_allow_html=True)
    
    # Display upcoming events (events with future dates)
    upcoming_events = [event for event in st.session_state.upcoming_events if event['date'] > datetime.now()]
    
    if upcoming_events:
        for event in upcoming_events:
            st.markdown(f"""
                <div class="event-card">
                    <button class="share-btn" onclick="openShareModal('{event['id']}')" title="Share Event">📤</button>
                    <div style="flex: 1;">
                        <h3 style="color: #00d4aa; margin: 0 0 0.5rem 0;">{event['title']}</h3>
                        <p style="color: #e0e0e0; margin: 0 0 1rem 0;">{event['description']}</p>
                        <div style="color: #888; font-size: 0.9rem;">
                            📅 {event['date'].strftime('%B %d, %Y')} • 📍 {event['location']} • 🏷️ {event['type']}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)
    else:
        st.markdown("</div></div>", unsafe_allow_html=True)
        st.info("No upcoming events scheduled. Use the floating + button to add new events!")
    
    # Add Event Modal and Share Modal JavaScript
    st.markdown("""
        <script>
        function openAddEventModal() {
            // Trigger the Streamlit button to show the form
            const addBtn = document.querySelector('button[data-testid="baseButton-section_add_btn"]');
            if (addBtn) {
                addBtn.click();
            }
        }
        
        function openShareModal(eventId) {
            const event = getEventById(eventId);
            const shareText = `Event: ${event.title}\\nDate: ${event.date}\\nLocation: ${event.location}\\nDescription: ${event.description}`;
            
            // Create share modal
            const modal = document.createElement('div');
            modal.className = 'modal-overlay';
            modal.innerHTML = `
                <div class="share-modal">
                    <div class="modal-header">
                        <h3 style="color: #00d4aa; margin: 0;">📤 Share Event</h3>
                        <button class="close-btn" onclick="closeModal()">×</button>
                    </div>
                    <div style="color: #e0e0e0; margin-bottom: 1rem;">
                        <strong>${event.title}</strong><br>
                        <small style="color: #888;">${event.date} • ${event.location}</small>
                    </div>
                    <div class="share-option" onclick="shareViaWhatsApp('${shareText}')">
                        <span style="margin-right: 10px;">📱</span> Share via WhatsApp
                    </div>
                    <div class="share-option" onclick="shareViaEmail('${shareText}')">
                        <span style="margin-right: 10px;">📧</span> Share via Email
                    </div>
                    <button class="copy-link" onclick="copyToClipboard('${shareText}')">
                        📋 Copy to Clipboard
                    </button>
                </div>
            `;
            document.body.appendChild(modal);
        }
        
        function closeModal() {
            const modal = document.querySelector('.modal-overlay');
            if (modal) {
                modal.remove();
            }
        }
        
        function shareViaWhatsApp(text) {
            const url = `https://wa.me/?text=${encodeURIComponent(text)}`;
            window.open(url, '_blank');
        }
        
        function shareViaEmail(text) {
            const url = `mailto:?subject=Upcoming Event&body=${encodeURIComponent(text)}`;
            window.open(url);
        }
        
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(() => {
                alert('Event details copied to clipboard!');
                closeModal();
            });
        }
        
        // Store event data for sharing
        window.eventData = {
            'UP-001': {
                title: 'Community Safety Workshop',
                date: '${(datetime.now() + timedelta(days=7)).strftime("%B %d, %Y")}',
                location: 'Community Hall',
                description: 'Monthly safety awareness session for all residents'
            },
            'UP-002': {
                title: 'Maintenance Day',
                date: '${(datetime.now() + timedelta(days=14)).strftime("%B %d, %Y")}',
                location: 'Various Locations',
                description: 'Scheduled maintenance for common areas and facilities'
            },
            'UP-003': {
                title: 'Resident Meet & Greet',
                date: '${(datetime.now() + timedelta(days=21)).strftime("%B %d, %Y")}',
                location: 'Garden Area',
                description: 'Social gathering to foster community bonding'
            }
        };
        
        function getEventById(eventId) {
            return window.eventData[eventId] || {
                title: 'Event Title',
                date: 'Event Date',
                location: 'Event Location',
                description: 'Event Description'
            };
        }
        
        // Close modal when clicking outside
        document.addEventListener('click', function(e) {
            if (e.target.classList.contains('modal-overlay')) {
                closeModal();
            }
        });
        </script>
    """, unsafe_allow_html=True)

    # Section Add Button (triggers the form)
    section_add_clicked = st.button("+", key="section_add_btn", help="Add event to section")

    if section_add_clicked:
        st.session_state.show_add_form = True

    # Floating Action Button (real Streamlit button)
    fab_clicked = st.button("+", key="fab_add_btn", help="Add upcoming event")

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
                            'type': new_type
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
