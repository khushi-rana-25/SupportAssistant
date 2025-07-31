"""
Community Engagement Page for ResiVoice Application
Handles community forums, events, announcements, and neighbor connections
"""

import streamlit as st
import sys
import os
from datetime import datetime, timedelta
import pandas as pd

# Add the parent directory to the path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from components.navigation import render_voice_section

def community_page():
    """Main community engagement page function"""
    st.markdown('<h2 class="page-header">🏘️ Community Engagement</h2>', unsafe_allow_html=True)
    
    # Voice Assistant Section
    render_voice_section(
        title="🎤 Community Voice Assistant",
        description="Use voice commands to navigate community features",
        examples="Say: \"Show community events\", \"Post in forum\", \"Find neighbors\""
    )
    
    # Initialize session state for community features
    if 'community_posts' not in st.session_state:
        st.session_state.community_posts = []
    if 'community_events' not in st.session_state:
        st.session_state.community_events = []
    if 'announcements' not in st.session_state:
        st.session_state.announcements = []
    if 'neighbor_connections' not in st.session_state:
        st.session_state.neighbor_connections = []
    
    # Create tabs for different community features
    tab1, tab2, tab3, tab4 = st.tabs(["📢 Forums", "📅 Events", "📢 Announcements", "👥 Neighbors"])
    
    with tab1:
        render_forums_tab()
    
    with tab2:
        render_events_tab()
    
    with tab3:
        render_announcements_tab()
    
    with tab4:
        render_neighbors_tab()

def render_forums_tab():
    """Render the community forums tab"""
    st.markdown("### 📢 Community Forums")
    st.markdown("Connect with your neighbors, share ideas, and discuss community matters.")
    
    # Forum categories
    categories = ["General Discussion", "Maintenance Tips", "Social Events", "Safety & Security", "Suggestions"]
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Categories")
        selected_category = st.selectbox("Choose a category:", categories)
        
        st.markdown("---")
        st.markdown("#### Quick Stats")
        st.metric("Total Posts", len(st.session_state.community_posts))
        st.metric("Active Users", "24")
        st.metric("This Week", "12 new posts")
    
    with col2:
        st.markdown(f"#### {selected_category}")
        
        # Create new post
        with st.expander("📝 Create New Post", expanded=False):
            with st.form("new_post_form"):
                post_title = st.text_input("Post Title")
                post_content = st.text_area("Post Content", height=150)
                post_category = st.selectbox("Category", categories)
                
                if st.form_submit_button("Post", use_container_width=True):
                    if post_title and post_content:
                        new_post = {
                            'id': f"POST-{len(st.session_state.community_posts) + 1:04d}",
                            'title': post_title,
                            'content': post_content,
                            'category': post_category,
                            'author': 'You',
                            'timestamp': datetime.now(),
                            'likes': 0,
                            'comments': []
                        }
                        st.session_state.community_posts.append(new_post)
                        st.success("Post created successfully!")
                        st.rerun()
        
        # Display posts
        if st.session_state.community_posts:
            filtered_posts = [post for post in st.session_state.community_posts if post['category'] == selected_category]
            
            for post in filtered_posts:
                with st.container():
                    st.markdown(f"""
                    <div style="
                        background: #1a1a1a;
                        padding: 1rem;
                        border-radius: 8px;
                        margin-bottom: 1rem;
                        border-left: 4px solid #00d4aa;
                    ">
                        <h4 style="color: #00d4aa; margin-bottom: 0.5rem;">{post['title']}</h4>
                        <p style="color: #e0e0e0; margin-bottom: 0.5rem;">{post['content']}</p>
                        <div style="color: #888888; font-size: 0.8rem;">
                            By {post['author']} • {post['timestamp'].strftime('%Y-%m-%d %H:%M')} • 
                            👍 {post['likes']} • 💬 {len(post['comments'])}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Like and comment buttons
                    col1, col2, col3 = st.columns([1, 1, 3])
                    with col1:
                        if st.button(f"👍 Like", key=f"like_{post['id']}"):
                            post['likes'] += 1
                            st.rerun()
                    with col2:
                        if st.button(f"💬 Comment", key=f"comment_{post['id']}"):
                            st.session_state.show_comment_input = post['id']
                            st.rerun()
                    
                    # Comment input
                    if st.session_state.get('show_comment_input') == post['id']:
                        comment_text = st.text_input("Add a comment:", key=f"comment_input_{post['id']}")
                        if st.button("Post Comment", key=f"post_comment_{post['id']}"):
                            if comment_text:
                                post['comments'].append({
                                    'author': 'You',
                                    'content': comment_text,
                                    'timestamp': datetime.now()
                                })
                                st.session_state.show_comment_input = None
                                st.rerun()
        else:
            st.info("No posts yet. Be the first to start a conversation!")

def render_events_tab():
    """Render the community events tab"""
    st.markdown("### 📅 Community Events")
    st.markdown("Discover and participate in community events and activities.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Create Event")
        with st.form("new_event_form"):
            event_title = st.text_input("Event Title")
            event_description = st.text_area("Event Description", height=100)
            event_date = st.date_input("Event Date")
            event_time = st.time_input("Event Time")
            event_location = st.text_input("Event Location")
            event_type = st.selectbox("Event Type", ["Social", "Educational", "Maintenance", "Safety", "Other"])
            
            if st.form_submit_button("Create Event", use_container_width=True):
                if event_title and event_description:
                    new_event = {
                        'id': f"EVENT-{len(st.session_state.community_events) + 1:04d}",
                        'title': event_title,
                        'description': event_description,
                        'date': event_date,
                        'time': event_time,
                        'location': event_location,
                        'type': event_type,
                        'organizer': 'You',
                        'attendees': ['You'],
                        'max_attendees': 50
                    }
                    st.session_state.community_events.append(new_event)
                    st.success("Event created successfully!")
                    st.rerun()
        
        st.markdown("---")
        st.markdown("#### Event Stats")
        st.metric("Upcoming Events", len([e for e in st.session_state.community_events if e['date'] >= datetime.now().date()]))
        st.metric("Total Events", len(st.session_state.community_events))
        st.metric("Your Events", len([e for e in st.session_state.community_events if e['organizer'] == 'You']))
    
    with col2:
        st.markdown("#### Upcoming Events")
        
        if st.session_state.community_events:
            upcoming_events = [e for e in st.session_state.community_events if e['date'] >= datetime.now().date()]
            upcoming_events.sort(key=lambda x: x['date'])
            
            for event in upcoming_events:
                with st.container():
                    st.markdown(f"""
                    <div style="
                        background: #1a1a1a;
                        padding: 1rem;
                        border-radius: 8px;
                        margin-bottom: 1rem;
                        border-left: 4px solid #00d4aa;
                    ">
                        <h4 style="color: #00d4aa; margin-bottom: 0.5rem;">{event['title']}</h4>
                        <p style="color: #e0e0e0; margin-bottom: 0.5rem;">{event['description']}</p>
                        <div style="color: #888888; font-size: 0.8rem;">
                            📅 {event['date'].strftime('%B %d, %Y')} • 🕐 {event['time'].strftime('%I:%M %p')} • 
                            📍 {event['location']} • 👥 {len(event['attendees'])}/{event['max_attendees']} attending
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # RSVP buttons
                    if 'You' in event['attendees']:
                        if st.button("❌ Cancel RSVP", key=f"cancel_{event['id']}"):
                            event['attendees'].remove('You')
                            st.rerun()
                    else:
                        if st.button("✅ RSVP", key=f"rsvp_{event['id']}"):
                            event['attendees'].append('You')
                            st.rerun()
        else:
            st.info("No upcoming events. Create the first community event!")

def render_announcements_tab():
    """Render the announcements tab"""
    st.markdown("### 📢 Community Announcements")
    st.markdown("Stay updated with important community news and announcements.")
    
    # Sample announcements
    if not st.session_state.announcements:
        st.session_state.announcements = [
            {
                'id': 'ANN-0001',
                'title': 'New Community Guidelines',
                'content': 'We have updated our community guidelines to ensure a better living experience for everyone. Please review the new policies.',
                'priority': 'High',
                'timestamp': datetime.now() - timedelta(days=2),
                'author': 'Property Management'
            },
            {
                'id': 'ANN-0002',
                'title': 'Pool Maintenance Schedule',
                'content': 'The community pool will be closed for maintenance from June 15-20. We apologize for any inconvenience.',
                'priority': 'Medium',
                'timestamp': datetime.now() - timedelta(days=5),
                'author': 'Maintenance Team'
            },
            {
                'id': 'ANN-0003',
                'title': 'Community BBQ Event',
                'content': 'Join us for our monthly community BBQ this Saturday at 6 PM in the courtyard. All residents welcome!',
                'priority': 'Low',
                'timestamp': datetime.now() - timedelta(days=7),
                'author': 'Community Events'
            }
        ]
    
    # Filter by priority
    priority_filter = st.selectbox("Filter by Priority:", ["All", "High", "Medium", "Low"])
    
    for announcement in st.session_state.announcements:
        if priority_filter == "All" or announcement['priority'] == priority_filter:
            priority_color = {
                'High': '#ff6b6b',
                'Medium': '#ffd93d',
                'Low': '#6bcf7f'
            }.get(announcement['priority'], '#00d4aa')
            
            st.markdown(f"""
            <div style="
                background: #1a1a1a;
                padding: 1rem;
                border-radius: 8px;
                margin-bottom: 1rem;
                border-left: 4px solid {priority_color};
            ">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                    <h4 style="color: #00d4aa; margin: 0;">{announcement['title']}</h4>
                    <span style="
                        background: {priority_color};
                        color: #0a0a0a;
                        padding: 0.2rem 0.5rem;
                        border-radius: 4px;
                        font-size: 0.7rem;
                        font-weight: bold;
                    ">{announcement['priority']}</span>
                </div>
                <p style="color: #e0e0e0; margin-bottom: 0.5rem;">{announcement['content']}</p>
                <div style="color: #888888; font-size: 0.8rem;">
                    By {announcement['author']} • {announcement['timestamp'].strftime('%Y-%m-%d %H:%M')}
                </div>
            </div>
            """, unsafe_allow_html=True)

def render_neighbors_tab():
    """Render the neighbors tab"""
    st.markdown("### 👥 Connect with Neighbors")
    st.markdown("Build connections with your neighbors and create a stronger community.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Your Profile")
        with st.form("neighbor_profile"):
            name = st.text_input("Your Name", value="John Doe")
            unit = st.text_input("Unit Number", value="101")
            interests = st.multiselect("Interests", [
                "Gardening", "Cooking", "Fitness", "Reading", "Music", 
                "Sports", "Technology", "Art", "Pets", "Travel"
            ])
            bio = st.text_area("Bio", placeholder="Tell your neighbors about yourself...")
            
            if st.form_submit_button("Update Profile", use_container_width=True):
                st.success("Profile updated!")
        
        st.markdown("---")
        st.markdown("#### Community Stats")
        st.metric("Total Residents", "156")
        st.metric("Active Profiles", "89")
        st.metric("Your Connections", "12")
    
    with col2:
        st.markdown("#### Nearby Neighbors")
        
        # Sample neighbor data
        neighbors = [
            {"name": "Sarah Johnson", "unit": "102", "interests": ["Gardening", "Cooking"], "connected": True},
            {"name": "Mike Chen", "unit": "103", "interests": ["Fitness", "Sports"], "connected": False},
            {"name": "Emily Davis", "unit": "104", "interests": ["Reading", "Art"], "connected": False},
            {"name": "David Wilson", "unit": "105", "interests": ["Technology", "Music"], "connected": True},
        ]
        
        for neighbor in neighbors:
            with st.container():
                st.markdown(f"""
                <div style="
                    background: #1a1a1a;
                    padding: 1rem;
                    border-radius: 8px;
                    margin-bottom: 1rem;
                    border-left: 4px solid #00d4aa;
                ">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <h4 style="color: #00d4aa; margin-bottom: 0.2rem;">{neighbor['name']}</h4>
                            <p style="color: #888888; margin-bottom: 0.5rem;">Unit {neighbor['unit']}</p>
                            <p style="color: #e0e0e0; font-size: 0.8rem;">
                                Interests: {', '.join(neighbor['interests'])}
                            </p>
                        </div>
                        <div style="text-align: right;">
                            {'✅ Connected' if neighbor['connected'] else '🔗 Connect'}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if not neighbor['connected']:
                    if st.button(f"Connect with {neighbor['name']}", key=f"connect_{neighbor['name']}"):
                        neighbor['connected'] = True
                        st.success(f"Connected with {neighbor['name']}!")
                        st.rerun()
                else:
                    if st.button(f"Message {neighbor['name']}", key=f"message_{neighbor['name']}"):
                        st.info(f"Messaging feature coming soon!") 