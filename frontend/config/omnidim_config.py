"""
Configuration for Omnidim.io Integration
Contains settings and endpoints for the Omnidim.io API
"""

import os
from typing import Dict, Any

# Omnidim.io API Configuration
OMNIDIM_CONFIG = {
    "base_url": "https://api.omnidim.io/v1",
    "timeout": 30,
    "max_retries": 3,
    "application": "resivoice",
    "context": "residential_services"
}

# Voice Assistant Configuration
VOICE_CONFIG = {
    "session_timeout": 300,  # 5 minutes
    "max_session_duration": 1800,  # 30 minutes
    "audio_format": "wav",
    "sample_rate": 16000,
    "channels": 1
}

# Command Patterns for Voice Recognition
VOICE_COMMANDS = {
    "complaint": [
        "file a complaint",
        "report an issue", 
        "make a complaint",
        "submit a complaint",
        "report noise",
        "report neighbor"
    ],
    "tracking": [
        "track my request",
        "check status",
        "get update",
        "track complaint",
        "status update"
    ],
    "service": [
        "request service",
        "maintenance request",
        "repair request",
        "plumbing service",
        "electrical service"
    ],
    "feedback": [
        "give feedback",
        "rate service",
        "provide review",
        "share experience"
    ],
    "help": [
        "help",
        "assist",
        "support",
        "what can you do"
    ]
}

# Response Templates
RESPONSE_TEMPLATES = {
    "welcome": "Welcome to ResiVoice! I'm your voice assistant powered by Omnidim.io. I can help you file complaints, track requests, request services, and provide feedback. What would you like to do?",
    "complaint_help": "I'll help you file a complaint. Please provide details about the issue, including the type of problem and any relevant information.",
    "tracking_help": "I'll help you track your requests. Please provide your request ID or describe what you're looking for.",
    "service_help": "I'll help you request maintenance service. Please describe the issue and specify the type of service needed.",
    "feedback_help": "I'll help you provide feedback. Please rate your experience and share your thoughts about our services.",
    "error": "I'm sorry, I couldn't process your request. Please try again or contact support for assistance.",
    "not_understood": "I didn't understand that command. You can say things like 'file a complaint', 'track my request', or 'request service'."
}

def get_omnidim_api_key() -> str:
    """Get Omnidim.io API key from environment variables"""
    return os.getenv('OMNIDIM_API_KEY', '')

def get_voice_settings() -> Dict[str, Any]:
    """Get voice assistant settings"""
    return {
        **VOICE_CONFIG,
        "api_key": get_omnidim_api_key(),
        **OMNIDIM_CONFIG
    }

def is_omnidim_configured() -> bool:
    """Check if Omnidim.io is properly configured"""
    return bool(get_omnidim_api_key()) 