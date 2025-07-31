"""
OmniDimension SDK Integration for ResiVoice Application
Uses the official OmniDimension SDK for voice assistant functionality
"""

import os
import streamlit as st
from typing import Dict, Optional
from omnidimension import Client

class OmniDimensionManager:
    """Manager for OmniDimension SDK integration"""
    
    def __init__(self):
        """Initialize the OmniDimension manager"""
        self.api_key = os.environ.get('OMNIDIM_API_KEY')
        if self.api_key:
            self.client = Client(self.api_key)
            self.is_configured = True
        else:
            self.client = None
            self.is_configured = False
    
    def list_agents(self) -> list:
        """List all available agents"""
        if not self.is_configured:
            return []
        
        try:
            agents = self.client.agent.list()
            return agents
        except Exception as e:
            st.error(f"Failed to list agents: {str(e)}")
            return []
    
    def create_voice_session(self, agent_id: str = None) -> Dict:
        """Create a new voice session"""
        if not self.is_configured:
            return {"error": "OmniDimension not configured"}
        
        try:
            # If no agent_id provided, use the first available agent
            if not agent_id:
                agents = self.list_agents()
                if agents:
                    agent_id = agents[0].get('id')
                else:
                    return {"error": "No agents available"}
            
            # Create a session with the agent
            session = self.client.session.create(
                agent_id=agent_id,
                context="resivoice_residential_services"
            )
            
            return {
                "session_id": session.get('id'),
                "agent_id": agent_id,
                "status": "active"
            }
            
        except Exception as e:
            st.error(f"Failed to create voice session: {str(e)}")
            return {"error": "Failed to create session"}
    
    def send_message(self, session_id: str, message: str) -> Dict:
        """Send a message to the voice session"""
        if not self.is_configured:
            return {"error": "OmniDimension not configured"}
        
        try:
            response = self.client.session.send_message(
                session_id=session_id,
                message=message
            )
            
            return {
                "response": response.get('response', ''),
                "status": "success"
            }
            
        except Exception as e:
            st.error(f"Failed to send message: {str(e)}")
            return {"error": "Failed to send message"}
    
    def end_session(self, session_id: str) -> Dict:
        """End a voice session"""
        if not self.is_configured:
            return {"error": "OmniDimension not configured"}
        
        try:
            self.client.session.end(session_id=session_id)
            return {"status": "ended"}
            
        except Exception as e:
            st.error(f"Failed to end session: {str(e)}")
            return {"error": "Failed to end session"}
    
    def get_session_status(self, session_id: str) -> Dict:
        """Get the status of a session"""
        if not self.is_configured:
            return {"error": "OmniDimension not configured"}
        
        try:
            status = self.client.session.get(session_id=session_id)
            return status
            
        except Exception as e:
            return {"error": "Failed to get session status"}

def create_omnidim_manager() -> OmniDimensionManager:
    """Create and return an OmniDimension manager instance"""
    return OmniDimensionManager()

def handle_voice_command(command: str, session_state: Dict) -> str:
    """Handle voice commands and return appropriate responses"""
    command = command.lower().strip()
    
    # Complaint-related commands
    if any(word in command for word in ["complaint", "file", "report", "issue"]):
        if "noise" in command:
            return "I'll help you file a noise complaint. Please provide details about the noise issue, including the time, location, and nature of the disturbance."
        elif "maintenance" in command:
            return "I'll help you report a maintenance issue. Please describe the problem, its location, and any safety concerns."
        elif "neighbor" in command:
            return "I'll help you file a complaint about your neighbor. Please provide specific details about the issue and any previous attempts to resolve it."
        else:
            return "I'll help you file a complaint. Please provide details about the issue, including when it occurred and any relevant information."
    
    # Tracking-related commands
    elif any(word in command for word in ["track", "status", "update", "check"]):
        if "complaint" in command:
            return "I'll help you track your complaint. Please provide your complaint ID or describe the complaint you submitted."
        elif "request" in command:
            return "I'll help you check the status of your request. Please provide your request ID or describe the service you requested."
        else:
            return "I'll help you track your requests. Please provide the request ID or describe what you're looking for."
    
    # Service-related commands
    elif any(word in command for word in ["service", "maintenance", "repair", "fix"]):
        if "plumbing" in command:
            return "I'll help you request plumbing service. Please describe the issue, its location, and whether it's an emergency."
        elif "electrical" in command:
            return "I'll help you request electrical service. Please describe the issue and whether it poses any safety risks."
        elif "heating" in command or "ac" in command or "hvac" in command:
            return "I'll help you request HVAC service. Please describe the issue with your heating or air conditioning system."
        else:
            return "I'll help you request maintenance service. Please describe the issue, its location, and urgency level."
    
    # Community-related commands
    elif any(word in command for word in ["community", "forum", "post", "discussion"]):
        if "event" in command or "show events" in command:
            return "I'll take you to the community events section where you can see upcoming events and create new ones."
        elif "neighbor" in command or "find neighbors" in command:
            return "I'll help you connect with your neighbors. You can view nearby residents and build connections."
        elif "announcement" in command:
            return "I'll show you the latest community announcements and important updates from property management."
        elif "forum" in command or "discussion" in command:
            return "I'll take you to the community forums where you can discuss topics with your neighbors."
        else:
            return "I'll help you navigate the community features. You can access forums, events, announcements, and neighbor connections."
    
    # Feedback-related commands
    elif any(word in command for word in ["feedback", "review", "rating", "satisfaction"]):
        return "I'll help you provide feedback. Please rate your experience with our services and share any suggestions for improvement."
    
    # General help commands
    elif any(word in command for word in ["help", "assist", "support"]):
        return "I'm here to help! I can assist you with filing complaints, tracking requests, requesting maintenance services, providing feedback, and accessing community features. What would you like to do?"
    
    # Default response
    else:
        return "I didn't understand that command. You can say things like 'file a complaint', 'track my request', 'request service', 'show community events', or 'give feedback'." 