"""
Feedback Page for ResiVoice Application
Handles feedback submission and analytics
"""

import streamlit as st
import pandas as pd
from datetime import datetime

def feedback_page():
    """Main feedback page function"""
    st.markdown('<h2 class="page-header">💬 Give Feedback</h2>', unsafe_allow_html=True)
    
    st.markdown('<h3 style="margin-top: 2rem;">📝 Feedback Form (MCQ)</h3>', unsafe_allow_html=True)
    
    # Feedback Form with MCQ
    with st.form("feedback_mcq_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name *", key="feedback_name", placeholder="Enter your full name")
            email = st.text_input("Email Address *", key="feedback_email", placeholder="Enter your email")
            unit_number = st.text_input("Unit/Apartment Number", key="feedback_unit", placeholder="e.g., 101, A-5")
        
        with col2:
            feedback_type = st.selectbox("Feedback Type *", [
                "General Feedback",
                "Service Quality",
                "Staff Performance",
                "Facility Improvement",
                "Suggestion",
                "Complaint",
                "Appreciation"
            ])
            overall_rating = st.selectbox("Overall Satisfaction Rating *", [
                "1 - Very Dissatisfied",
                "2 - Dissatisfied", 
                "3 - Neutral",
                "4 - Satisfied",
                "5 - Very Satisfied"
            ])
        
        st.markdown("### Service Quality Assessment")
        
        col1, col2 = st.columns(2)
        with col1:
            response_time = st.selectbox("How would you rate our response time? *", [
                "Excellent",
                "Good",
                "Average",
                "Poor",
                "Very Poor"
            ])
            
            staff_courtesy = st.selectbox("How would you rate staff courtesy? *", [
                "Excellent",
                "Good", 
                "Average",
                "Poor",
                "Very Poor"
            ])
            
            work_quality = st.selectbox("How would you rate the quality of work done? *", [
                "Excellent",
                "Good",
                "Average", 
                "Poor",
                "Very Poor"
            ])
        
        with col2:
            communication = st.selectbox("How would you rate our communication? *", [
                "Excellent",
                "Good",
                "Average",
                "Poor",
                "Very Poor"
            ])
            
            cleanliness = st.selectbox("How would you rate facility cleanliness? *", [
                "Excellent",
                "Good",
                "Average",
                "Poor", 
                "Very Poor"
            ])
            
            value_for_money = st.selectbox("How would you rate value for money? *", [
                "Excellent",
                "Good",
                "Average",
                "Poor",
                "Very Poor"
            ])
        
        st.markdown("### Additional Questions")
        
        col1, col2 = st.columns(2)
        with col1:
            would_recommend = st.selectbox("Would you recommend our services to others? *", [
                "Definitely Yes",
                "Probably Yes",
                "Not Sure",
                "Probably No",
                "Definitely No"
            ])
            
            frequency_of_issues = st.selectbox("How often do you experience issues? *", [
                "Never",
                "Rarely",
                "Sometimes",
                "Often",
                "Very Often"
            ])
        
        with col2:
            preferred_contact = st.selectbox("What's your preferred contact method? *", [
                "Phone Call",
                "Email",
                "Text Message",
                "In-Person",
                "Voice Assistant"
            ])
            
            improvement_priority = st.selectbox("What should we prioritize for improvement? *", [
                "Response Time",
                "Service Quality",
                "Communication",
                "Facility Maintenance",
                "Staff Training",
                "Technology/App Features"
            ])
        
        feedback_title = st.text_input("Feedback Title *", key="feedback_title", placeholder="Brief title for your feedback")
        
        additional_comments = st.text_area("Additional Comments", 
                                         placeholder="Any additional comments, suggestions, or specific feedback...",
                                         height=150,
                                         key="feedback_comments")
        
        anonymous = st.checkbox("Submit anonymously")
        
        submit_button = st.form_submit_button("Submit Feedback", type="primary")
        
        if submit_button:
            if name and email and feedback_title:
                feedback_id = f"FB-{len(st.session_state.feedback) + 1:04d}"
                feedback_entry = {
                    "id": feedback_id,
                    "name": "Anonymous" if anonymous else name,
                    "email": email,
                    "unit_number": unit_number,
                    "feedback_type": feedback_type,
                    "overall_rating": overall_rating,
                    "title": feedback_title,
                    "additional_comments": additional_comments,
                    "anonymous": anonymous,
                    "submitted_date": datetime.now(),
                    # MCQ Responses
                    "response_time": response_time,
                    "staff_courtesy": staff_courtesy,
                    "work_quality": work_quality,
                    "communication": communication,
                    "cleanliness": cleanliness,
                    "value_for_money": value_for_money,
                    "would_recommend": would_recommend,
                    "frequency_of_issues": frequency_of_issues,
                    "preferred_contact": preferred_contact,
                    "improvement_priority": improvement_priority
                }
                st.session_state.feedback.append(feedback_entry)
                st.success(f"✅ Feedback submitted successfully! Thank you for your detailed input.")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields marked with *")
    
    # Display recent feedback
    if st.session_state.feedback:
        st.markdown('<h3 style="margin-top: 2rem;">📊 Feedback Analytics & Charts</h3>', unsafe_allow_html=True)
        
        # Create charts
        col1, col2 = st.columns(2)
        
        with col1:
            # Overall Satisfaction Chart
            st.markdown("### 📈 Overall Satisfaction Distribution")
            satisfaction_data = {}
            for feedback in st.session_state.feedback:
                rating = feedback.get('overall_rating', 'Not Rated')
                satisfaction_data[rating] = satisfaction_data.get(rating, 0) + 1
            
            if satisfaction_data:
                satisfaction_df = pd.DataFrame(list(satisfaction_data.items()), columns=['Rating', 'Count'])
                st.bar_chart(satisfaction_df.set_index('Rating'))
            else:
                st.info("No satisfaction data available yet.")
        
        with col2:
            # Would Recommend Chart
            st.markdown("### 👍 Recommendation Likelihood")
            recommend_data = {}
            for feedback in st.session_state.feedback:
                recommend = feedback.get('would_recommend', 'Not Answered')
                recommend_data[recommend] = recommend_data.get(recommend, 0) + 1
            
            if recommend_data:
                recommend_df = pd.DataFrame(list(recommend_data.items()), columns=['Response', 'Count'])
                st.bar_chart(recommend_df.set_index('Response'))
            else:
                st.info("No recommendation data available yet.")
        
        # Service Quality Metrics
        st.markdown("### 🔍 Service Quality Analysis")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Response Time Chart
            response_data = {}
            for feedback in st.session_state.feedback:
                response = feedback.get('response_time', 'Not Rated')
                response_data[response] = response_data.get(response, 0) + 1
            
            if response_data:
                response_df = pd.DataFrame(list(response_data.items()), columns=['Rating', 'Count'])
                st.markdown("**Response Time Ratings**")
                st.bar_chart(response_df.set_index('Rating'))
        
        with col2:
            # Staff Courtesy Chart
            courtesy_data = {}
            for feedback in st.session_state.feedback:
                courtesy = feedback.get('staff_courtesy', 'Not Rated')
                courtesy_data[courtesy] = courtesy_data.get(courtesy, 0) + 1
            
            if courtesy_data:
                courtesy_df = pd.DataFrame(list(courtesy_data.items()), columns=['Rating', 'Count'])
                st.markdown("**Staff Courtesy Ratings**")
                st.bar_chart(courtesy_df.set_index('Rating'))
        
        with col3:
            # Work Quality Chart
            quality_data = {}
            for feedback in st.session_state.feedback:
                quality = feedback.get('work_quality', 'Not Rated')
                quality_data[quality] = quality_data.get(quality, 0) + 1
            
            if quality_data:
                quality_df = pd.DataFrame(list(quality_data.items()), columns=['Rating', 'Count'])
                st.markdown("**Work Quality Ratings**")
                st.bar_chart(quality_df.set_index('Rating'))
        
        # Improvement Priorities
        st.markdown("### 🎯 Improvement Priorities")
        priority_data = {}
        for feedback in st.session_state.feedback:
            priority = feedback.get('improvement_priority', 'Not Specified')
            priority_data[priority] = priority_data.get(priority, 0) + 1
        
        if priority_data:
            priority_df = pd.DataFrame(list(priority_data.items()), columns=['Priority', 'Count'])
            st.bar_chart(priority_df.set_index('Priority'))
        
        # Satisfaction Summary
        st.markdown("### 📊 Satisfaction Summary")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_feedback = len(st.session_state.feedback)
            st.metric("Total Feedback", total_feedback)
        
        with col2:
            satisfied_count = sum(1 for f in st.session_state.feedback 
                                if f.get('overall_rating', '').startswith(('4', '5')))
            satisfaction_rate = (satisfied_count / total_feedback * 100) if total_feedback > 0 else 0
            st.metric("Satisfaction Rate", f"{satisfaction_rate:.1f}%")
        
        with col3:
            recommend_count = sum(1 for f in st.session_state.feedback 
                                if f.get('would_recommend', '').startswith(('Definitely Yes', 'Probably Yes')))
            recommend_rate = (recommend_count / total_feedback * 100) if total_feedback > 0 else 0
            st.metric("Recommendation Rate", f"{recommend_rate:.1f}%")
        
        with col4:
            avg_rating = 0
            rating_count = 0
            for f in st.session_state.feedback:
                rating = f.get('overall_rating', '')
                if rating.startswith(('1', '2', '3', '4', '5')):
                    avg_rating += int(rating[0])
                    rating_count += 1
            avg_rating = avg_rating / rating_count if rating_count > 0 else 0
            st.metric("Average Rating", f"{avg_rating:.1f}/5")
        
        # Recent Feedback List
        st.markdown('<h3 style="margin-top: 2rem;">📋 Recent Feedback Details</h3>', unsafe_allow_html=True)
        
        for feedback in reversed(st.session_state.feedback[-5:]):  # Show last 5 feedback
            with st.container():
                st.markdown(f"""
                <div class="card">
                    <h4>{feedback['title']}</h4>
                    <p><strong>Type:</strong> {feedback['feedback_type']} | <strong>Overall Rating:</strong> {feedback['overall_rating']}</p>
                    <p><strong>From:</strong> {feedback['name']} | <strong>Date:</strong> {feedback['submitted_date'].strftime('%Y-%m-%d %H:%M')}</p>
                    <p><strong>Response Time:</strong> {feedback.get('response_time', 'N/A')} | <strong>Staff Courtesy:</strong> {feedback.get('staff_courtesy', 'N/A')}</p>
                    <p><strong>Would Recommend:</strong> {feedback.get('would_recommend', 'N/A')} | <strong>Improvement Priority:</strong> {feedback.get('improvement_priority', 'N/A')}</p>
                    <p><strong>Additional Comments:</strong> {feedback.get('additional_comments', 'No additional comments')[:100]}{'...' if len(feedback.get('additional_comments', '')) > 100 else ''}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("💬 No feedback submitted yet. Use the form above to share your first feedback!")
    
    # Close the feedback-page div
    st.markdown('</div>', unsafe_allow_html=True)