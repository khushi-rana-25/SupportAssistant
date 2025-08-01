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
        /* Upcoming Events Styling */
        .upcoming-events-section {
            background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            border: 2px solid #00d4aa;
            box-shadow: 0 8px 32px rgba(0, 212, 170, 0.2);
            position: relative;
        }
        
        .header-section {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
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
        
        .section-add-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 6px 20px rgba(0, 212, 170, 0.5);
        }
        
        .events-container {
            margin-top: 2rem;
            padding-top: 1rem;
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
             right: 3.5rem;
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
         
         .delete-btn {
             position: absolute;
             top: 1rem;
             right: 1rem;
             background: rgba(255, 107, 107, 0.2);
             border: 1px solid #ff6b6b;
             border-radius: 50%;
             width: 35px;
             height: 35px;
             font-size: 14px;
             color: #ff6b6b;
             cursor: pointer;
             transition: all 0.3s ease;
             display: flex;
             align-items: center;
             justify-content: center;
         }
         
         .delete-btn:hover {
             background: rgba(255, 107, 107, 0.3);
             transform: scale(1.1);
         }
        
        /* Modal Styling */
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
        
        /* Ticket Management Dashboard Styling */
        .ticket-table {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1rem;
            margin: 1rem 0;
            border-left: 4px solid #00d4aa;
            transition: all 0.3s ease;
        }
        
        .ticket-table:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(0, 212, 170, 0.3);
        }
        
        .status-pending {
            color: #ffd93d;
            font-weight: bold;
        }
        
        .status-progress {
            color: #00d4aa;
            font-weight: bold;
        }
        
        .status-resolved {
            color: #6bcf7f;
            font-weight: bold;
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
    
    # Initialize session state for tickets with sample data
    if 'tickets' not in st.session_state:
        st.session_state.tickets = [
            {
                'id': 'TCK1234',
                'username': 'john_doe',
                'location': 'Block A - Room 203',
                'issue_type': 'WiFi Issue',
                'status': 'Pending',
                'assigned_to': '',
                'created_at': '2024-01-15 10:30'
            },
            {
                'id': 'TCK1235',
                'username': 'sarah_wilson',
                'location': 'Block B - Room 101',
                'issue_type': 'Plumbing',
                'status': 'In Progress',
                'assigned_to': 'Manager',
                'created_at': '2024-01-14 15:45'
            },
            {
                'id': 'TCK1236',
                'username': 'mike_chen',
                'location': 'Block C - Room 302',
                'issue_type': 'Power Cut',
                'status': 'Resolved',
                'assigned_to': 'Admin',
                'created_at': '2024-01-13 09:20'
            },
            {
                'id': 'TCK1237',
                'username': 'emma_rodriguez',
                'location': 'Block A - Room 105',
                'issue_type': 'HVAC',
                'status': 'Pending',
                'assigned_to': '',
                'created_at': '2024-01-15 14:15'
            }
        ]
    
    # Navigation tabs
    tab1, tab2 = st.tabs(["🚀 Upcoming Events", "📨 Ticket Desk"])
    
    # Tab 1: Upcoming Events
    with tab1:
        # Upcoming Events Section
        st.markdown("""
            <div class="upcoming-events-section">
                <div class="header-section">
                    <h2 style="color: #00d4aa; margin: 0;">🚀 Upcoming Events</h2>
                    <div style="text-align: right;">
                        <p style="color: #888; margin: 0;">Events scheduled for the future</p>
                    </div>
                </div>
                <div class="events-container">
        """, unsafe_allow_html=True)
        
        # Add Event Form (Below the heading)
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
        
        # Direct Add Event Button (replaces the JavaScript approach)
        if st.button("➕ Add New Event", key="add_event_direct", use_container_width=True):
            st.session_state.show_add_form = True
            st.rerun()
    
        # Display upcoming events (events with future dates)
        # Convert all dates to datetime for consistent comparison
        current_datetime = datetime.now()
        upcoming_events = []
        for event in st.session_state.upcoming_events:
            event_date = event['date']
            # Convert date to datetime if it's a date object
            if hasattr(event_date, 'date'):  # It's a datetime object
                event_datetime = event_date
            else:  # It's a date object
                event_datetime = datetime.combine(event_date, datetime.min.time())
            
            if event_datetime > current_datetime:
                upcoming_events.append(event)
        
        if upcoming_events:
            for event in upcoming_events:
                # Create a container for each event
                with st.container():
                    col1, col2 = st.columns([0.9, 0.1])
                    
                    with col1:
                        st.markdown(f"""
                            <div class="event-card">
                                <button class="share-btn" onclick="openShareModal('{event['id']}')" title="Share Event">🔗</button>
                                <div style="flex: 1;">
                                    <h3 style="color: #00d4aa; margin: 0 0 0.5rem 0;">{event['title']}</h3>
                                    <p style="color: #e0e0e0; margin: 0 0 1rem 0;">{event['description']}</p>
                                    <div style="color: #888; font-size: 0.9rem;">
                                        📅 {event['date'].strftime('%B %d, %Y')} • 📍 {event['location']} • 🏷️ {event['type']}
                                    </div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        # Delete button using Streamlit's native button
                        if st.button("🗑️", key=f"delete_{event['id']}", help="Delete this event"):
                            # Remove the event from the list
                            st.session_state.upcoming_events = [e for e in st.session_state.upcoming_events if e['id'] != event['id']]
                            st.success(f"Event '{event['title']}' deleted successfully!")
                            st.rerun()
            st.markdown("</div></div>", unsafe_allow_html=True)
        else:
            st.markdown("</div></div>", unsafe_allow_html=True)
            st.info("No upcoming events scheduled. Use the floating + button to add new events!")
    
    # Tab 2: Ticket Desk
    with tab2:
        st.markdown('<h2 style="color: #00d4aa; margin-bottom: 2rem;">📨 Ticket Management Dashboard</h2>', unsafe_allow_html=True)
        
        # Filtering and Search
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            status_filter = st.selectbox(
                "Filter by Status",
                ["All", "Pending", "In Progress", "Resolved"],
                key="status_filter"
            )
        
        with col2:
            search_ticket = st.text_input("Search by Ticket Number", placeholder="e.g., TCK1234")
        
        with col3:
            st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)  # Reduced height for better alignment
            if st.button("🔍 Search", use_container_width=True):
                pass
        
        # Filter tickets based on search and status
        filtered_tickets = st.session_state.tickets.copy()
        
        if status_filter != "All":
            filtered_tickets = [ticket for ticket in filtered_tickets if ticket['status'] == status_filter]
        
        if search_ticket:
            filtered_tickets = [ticket for ticket in filtered_tickets if search_ticket.upper() in ticket['id'].upper()]
        
        # Display Tickets Dashboard
        if filtered_tickets:
            st.markdown("### 📋 User Tickets")
            
            # Display tickets with enhanced styling
            for i, ticket in enumerate(filtered_tickets):
                with st.container():
                    st.markdown(f"""
                        <div class="ticket-table">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                                <h4 style="color: #00d4aa; margin: 0;">#{ticket['id']}</h4>
                                <span style="color: #888; font-size: 0.9rem;">{ticket['created_at']}</span>
                            </div>
                            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                                <div>
                                    <strong style="color: #e0e0e0;">Username:</strong><br>
                                    <span style="color: #888;">{ticket['username']}</span>
                                </div>
                                <div>
                                    <strong style="color: #e0e0e0;">Location:</strong><br>
                                    <span style="color: #888;">{ticket['location']}</span>
                                </div>
                                <div>
                                    <strong style="color: #e0e0e0;">Issue Type:</strong><br>
                                    <span style="color: #888;">{ticket['issue_type']}</span>
                                </div>
                                <div>
                                    <strong style="color: #e0e0e0;">Assigned To:</strong><br>
                                    <span style="color: #888;">{ticket['assigned_to'] if ticket['assigned_to'] else 'Unassigned'}</span>
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Admin/Manager Controls
                    col1, col2, col3 = st.columns([1, 1, 2])
                    
                    with col1:
                        st.markdown("**Status:**")
                        new_status = st.selectbox(
                            "Update Status",
                            options=["Pending", "In Progress", "Resolved"],
                            index=["Pending", "In Progress", "Resolved"].index(ticket['status']),
                            key=f"status_{ticket['id']}"
                        )
                        if new_status != ticket['status']:
                            # Find the ticket in the original list and update it
                            for j, original_ticket in enumerate(st.session_state.tickets):
                                if original_ticket['id'] == ticket['id']:
                                    st.session_state.tickets[j]['status'] = new_status
                                    st.success(f"Status updated to {new_status}")
                                    st.rerun()
                    
                    with col2:
                        st.markdown("**Assign To:**")
                        new_assignment = st.selectbox(
                            "Assign Ticket",
                            options=["", "Admin", "Manager"],
                            index=["", "Admin", "Manager"].index(ticket['assigned_to']),
                            key=f"assign_{ticket['id']}"
                        )
                        if new_assignment != ticket['assigned_to']:
                            # Find the ticket in the original list and update it
                            for j, original_ticket in enumerate(st.session_state.tickets):
                                if original_ticket['id'] == ticket['id']:
                                    st.session_state.tickets[j]['assigned_to'] = new_assignment
                                    st.success(f"Assigned to {new_assignment if new_assignment else 'Unassigned'}")
                                    st.rerun()
                    
                    # Status indicator with color coding
                    status_color = {
                        "Pending": "#ffd93d",
                        "In Progress": "#00d4aa", 
                        "Resolved": "#6bcf7f"
                    }
                    
                    assignment_color = "#ff6b6b" if not ticket['assigned_to'] else "#6bcf7f"
                    
                    st.markdown(f"""
                        <div style="display: flex; justify-content: center; gap: 1rem; margin: 1rem 0;">
                            <span style="background: {status_color[ticket['status']]}; color: #000; padding: 0.5rem 1rem; border-radius: 20px; font-weight: bold;">
                                {ticket['status']}
                            </span>
                            <span style="background: {assignment_color}; color: #000; padding: 0.5rem 1rem; border-radius: 20px; font-weight: bold;">
                                {ticket['assigned_to'] if ticket['assigned_to'] else 'Unassigned'}
                            </span>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("---")
        else:
            if not st.session_state.tickets:
                st.info("No user tickets submitted yet.")
            else:
                st.info("No tickets match the current filter criteria")
    
    # Share Modal JavaScript (only for sharing events)
    st.markdown("""
        <script>
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


if __name__ == "__main__":
    manager_home()
