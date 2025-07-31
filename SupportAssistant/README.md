# ResiVoice - Modular Streamlit Application

A modern, modular Streamlit application for residential property management with voice assistant integration.

## 🏗️ Project Structure

```
SupportAssistant/
├── frontend/
│   ├── app.py                 # Main application entry point
│   ├── components/
│   │   └── navigation.py      # Navigation and header components
│   ├── pages/
│   │   ├── complaint_page.py      # Complaint filing page
│   │   ├── service_request_service.py  # Service request page
│   │   ├── tracki.py              # Request tracking page
│   │   └── feedback.py            # Feedback submission page
│   └── utils/
│       └── styles.py          # Custom CSS styles
├── run.py                     # Application runner script
├── requirements.txt           # Python dependencies
└── README.md                 # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   # If you have the project files, navigate to the directory
   cd SupportAssistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python run.py
   ```

   Or alternatively:
   ```bash
   cd frontend
   streamlit run app.py
   ```

4. **Open your browser**
   The application will open automatically at `http://localhost:8501`

## 📱 Features

### 🎤 Voice Assistant Integration
- Voice-activated complaint filing
- Voice service requests
- Voice tracking queries
- Integration with Omnidim.io voice platform

### 📝 Complaint Management
- File complaints with voice or manual input
- Track complaint status
- View complaint history
- Priority-based categorization

### 🔧 Service Requests
- Request maintenance services
- Schedule appointments
- Track service progress
- Urgency-based prioritization

### 📊 Request Tracking
- Real-time status updates
- Comprehensive request history
- Visual status indicators
- Performance analytics

### 💬 Feedback System
- Multi-choice feedback forms
- Satisfaction ratings
- Service quality assessment
- Analytics and charts
- Anonymous submission option

## 🎨 Design Features

### Modern UI/UX
- Elegant gradient designs
- Responsive layout
- Smooth animations
- Professional typography
- Status-based color coding

### Custom Styling
- Google Fonts integration (Playfair Display, Inter)
- CSS animations and transitions
- Card-based layouts
- Consistent color scheme
- Mobile-friendly design

## 🔧 Technical Details

### Modular Architecture
- **Components**: Reusable UI components
- **Pages**: Individual page modules
- **Utils**: Shared utilities and styles
- **Main App**: Central routing and configuration

### Session State Management
- Complaint data persistence
- Service request tracking
- Feedback storage
- User session management

### Navigation System
- URL-based routing
- Query parameter navigation
- Persistent page state
- Smooth page transitions

## 🛠️ Customization

### Adding New Pages
1. Create a new file in `frontend/pages/`
2. Define a page function (e.g., `def new_page():`)
3. Import and add to routing in `app.py`
4. Add navigation button in `navigation.py`

### Modifying Styles
1. Edit `frontend/utils/styles.py`
2. Add new CSS classes as needed
3. Apply classes in your components

### Voice Assistant Integration
1. Modify voice section content in `navigation.py`
2. Update voice commands and examples
3. Integrate with Omnidim.io API

## 📊 Data Management

The application uses Streamlit's session state for data persistence:
- `st.session_state.complaints`: Complaint records
- `st.session_state.service_requests`: Service request records
- `st.session_state.feedback`: Feedback submissions
- `st.session_state.tracking_data`: Tracking information

## 🎯 Voice Commands Examples

### Complaint Filing
- "I want to file a complaint about noise from apartment 205"
- "Report a plumbing issue in unit 101, it's urgent"
- "Submit a complaint about parking problems"

### Service Requests
- "I need plumbing service for a leaky faucet in unit 203"
- "Request HVAC maintenance, it's not cooling properly"
- "Schedule cleaning service for next week"

### Tracking
- "Track my complaint COMP-0001"
- "What's the status of my service request SRV-0002"
- "Show me all my recent requests"

## 🔮 Future Enhancements

- Database integration for persistent storage
- User authentication system
- Email notifications
- Mobile app development
- Advanced analytics dashboard
- Multi-language support
- API integration for external services

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For support or questions, please contact the development team or create an issue in the project repository.

---

**ResiVoice** - Your Voice, Our Solution 🏠

// haha 