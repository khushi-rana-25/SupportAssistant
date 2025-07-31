# OmniDimension SDK Integration Setup Guide

This guide will help you set up OmniDimension SDK integration with your ResiVoice application.

## 🚀 Quick Start

### 1. Get OmniDimension API Key

1. Visit [OmniDimension Dashboard](https://omnidim.io)
2. Sign up for an account
3. Navigate to your account settings
4. Generate an API key for your application
5. Copy the API key

### 2. Configure Environment Variables

Create a `.env` file in your project root:

```bash
# OmniDimension Configuration
OMNIDIM_API_KEY=your_api_key_here
```

Or set it directly in your terminal:

```bash
# Linux/macOS
export OMNIDIM_API_KEY="your_api_key_here"

# Windows (Command Prompt)
set OMNIDIM_API_KEY=your_api_key_here

# Windows (PowerShell)
$env:OMNIDIM_API_KEY="your_api_key_here"
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Test the Integration

Run your Streamlit application:

```bash
streamlit run frontend/app.py
```

## 🔧 Configuration

### SDK Features

The integration uses the official OmniDimension SDK with these features:

- **Agent Management**: List and manage AI voice agents
- **Session Management**: Create and manage voice sessions
- **Message Processing**: Send and receive messages through agents
- **Context Awareness**: Maintain conversation context

### Voice Commands

The voice assistant recognizes these command patterns:

#### Complaints
- "file a complaint"
- "report an issue"
- "make a complaint"
- "report noise"
- "report neighbor"

#### Tracking
- "track my request"
- "check status"
- "get update"
- "track complaint"

#### Services
- "request service"
- "maintenance request"
- "repair request"
- "plumbing service"
- "electrical service"

#### Feedback
- "give feedback"
- "rate service"
- "provide review"

## 🎤 Voice Assistant Features

### Real-time Voice Processing
- Start/stop voice sessions with AI agents
- Process voice commands through OmniDimension
- Intelligent responses from trained agents
- Session management and context preservation

### Command Recognition
- Natural language processing powered by OmniDimension
- Context-aware responses
- Multi-language support
- Custom command patterns

### Integration Points
- Complaint filing
- Request tracking
- Service requests
- Feedback collection

## 🔒 Security

### API Key Management
- Store API keys in environment variables
- Never commit API keys to version control
- Use secure key rotation practices

### Session Security
- Secure session management through OmniDimension
- Automatic session timeout
- Encrypted communication

## 🐛 Troubleshooting

### Common Issues

1. **API Key Not Found**
   ```
   Warning: OmniDimension not configured
   ```
   **Solution**: Check your environment variables and ensure `OMNIDIM_API_KEY` is set correctly.

2. **No Agents Available**
   ```
   Error: No agents available
   ```
   **Solution**: Create an AI agent in your OmniDimension dashboard first.

3. **Session Errors**
   ```
   Error: Failed to create session
   ```
   **Solution**: Check your API key and agent configuration in OmniDimension.

### Debug Mode

Enable debug logging by setting:

```bash
export OMNIDIM_DEBUG=true
```

## 📞 Support

For OmniDimension SDK support:
- Documentation: [docs.omnidim.io](https://docs.omnidim.io)
- SDK Documentation: [pypi.org/project/omnidimension](https://pypi.org/project/omnidimension)
- Support: [support@omnidim.io](mailto:support@omnidim.io)
- Community: [community.omnidim.io](https://community.omnidim.io)

## 🔄 Updates

Keep your integration updated:

```bash
pip install --upgrade omnidimension
```

Check for OmniDimension SDK updates regularly.

## 📝 License

This integration is part of the ResiVoice application. Please refer to the main project license for terms and conditions. 